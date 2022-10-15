from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
import security as pw
import pandas as pd
import create_folder as cf
import move_files as mf
import consult_folder
import parameters as p
import unzip_files

def download(concessionaria:str=''):

    """
    Informar o nome da concessionária: concessionaria=''
    """

    username_field = pw.user(concessionaria, 'User')
    password_field = pw.user(concessionaria, 'Password')

    options = Options()
    # options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')  # usado apenas no windows
    # options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    navegador = webdriver.Chrome(p.executable_path, chrome_options=options)
    navegador.minimize_window()
    navegador.get(url=p.link)
    print ("Headless Chrome Initialized on Windows OS")

    # Por questões de segurança algumas informações foram excluídas como xPath
    # Nota que o xPath não é simplesmente '//*[@id=""]', ele possui mais informações dentro das ""

    input_email = navegador.find_element("xpath", '//*[@id=""]') 
    input_email.send_keys(username_field)

    input_password = navegador.find_element("xpath", '//*[@id=""]')
    input_password.send_keys(password_field)

    button_enter = navegador.find_element("xpath", '//*[@id=""]')
    button_enter.click()

    navegador.get(p.page_files)

    qtd_site = 0

    def get_FezDownload(line):
        xpath = '//*[@id="TableIndex"]/tbody/tr['+line+']'
        file = navegador.find_element("xpath", xpath)
        html_returns = file.get_attribute('innerHTML')
        records = BeautifulSoup(html_returns, 'html.parser')
        for row in records.find_all("td", attrs={"class": "text-center"}):
            x = row.text
            x = ''.join(filter(str.isalnum, x))
            if x == "Sim":
                return 1
            if x == "Não":
                return 0

    # log temporário, até que desenvolva com as informações do ZipFile
    file_df = {'file_name': []}
    file_df = pd.DataFrame(file_df)

    for i in range(10):
        line = str(i+1)
        xpath = '//*[@id="TableIndex"]/tbody/tr['+line+']/td[1]/a'
        file = navegador.find_element("xpath", xpath)

        soup = BeautifulSoup(file.text, 'html.parser')
        file_df.loc[i] = [str(soup)]

        if get_FezDownload(line) == 0:
            file.click()
            qtd_site += 1
            sleep(5)
        
    cf.create_folder("Documentos", "EDP/Temp")
    cf.create_folder("Documentos", "EDP/Temp/Duplicados")

    files_folder_ = consult_folder.result_qtd(
        p.downloads_folder,
        p.identify_file(concessionaria, 'begin'),  
        p.identify_file(concessionaria, 'end')
    )

    duplicate_qtd = consult_folder.duplicate_qtd(
        p.downloads_folder, 
        p.identify_file(concessionaria, 'begin', duplicate=True), 
        p.identify_file(concessionaria, 'end', duplicate=True)
    )

    qtd_site -= duplicate_qtd

    await_file_ = consult_folder.await_file(
            p.downloads_folder,
            p.identify_file(concessionaria, 'begin'), 
            ".ZIP.crdownload"
        )

    if files_folder_ >=  qtd_site:
        if await_file_ >= 1:
            sleep(15)
        sleep(2)
        mf.move_files(
            p.downloads_folder, 
            p.identify_file(concessionaria, 'begin'), 
            p.identify_file(concessionaria, 'end'), 
            p.temp_folder, 
            qtd_site
        )
        sleep(2)
        mf.move_files_duplicates(
            p.downloads_folder,
            p.identify_file(concessionaria, 'begin', duplicate=True), 
            p.identify_file(concessionaria, 'end', duplicate=True), 
            p.temp_duplicados
        )      
        unzip_files.files(
            p.temp_folder, 
            p.identify_file(concessionaria, 'begin'), 
            p.identify_file(concessionaria, 'end'), 
            delete_file=True
        )
        mf.move_files(
            p.temp_folder, 
            p.identify_file(concessionaria, 'begin', unzip=True), 
            p.identify_file(concessionaria, 'end', unzip=True), 
            p.return_folder(concessionaria)
        )

    navegador.quit()

if __name__ == '__main__':
    
    download('Bandeirantes')
    download('ESCELSA')