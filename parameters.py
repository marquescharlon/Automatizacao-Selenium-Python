# Instalação

# pip install selenium
# pip install requests
# pip install bs4
# pip install pathlib
# pip install sleep

import os.path
import security as pw # Interessante toda senha que necessitar utilizar adicionar em um arquivo protegido

folder_70 = fr''
folder_siparq = fr''
link = ''
page_files = '' 
executable_path = r'C:\WebScraping-Selenium-Python\selenium_webdriver\chromedriver.exe'
    

# Obter o caminho das pastas
downloads_folder = os.path.expanduser(r"~\Downloads")
temp_folder = os.path.expanduser(r"~\Documents/EDP/Temp")
temp_duplicados = os.path.expanduser(r"~\Documents/EDP/Temp/Duplicados")


def return_folder(concessionaria:'str'=''):
    """
    Informar o nome da concessionária: concessionaria='Nome'
    """
    if concessionaria == 'Bandeirante':
        path = os.path.expanduser(r"C:\Bandeirante\Retorno")
        return path
    if concessionaria == 'ESCELSA':
        path = os.path.expanduser(r"C:\ESCELSA\Retorno")
        return path

def identify_file(concessionaria:'str'='', position:'str'='', unzip=False, duplicate=False):
    """
    Informar o nome da concessionária: concessionaria='Nome' \n
    Pesquisar pelo início do arquivo: position='begin' \n
    Pesquisar pelo final do arquivo: position='end' \n
    Se o arquivo estiver descompactado informe: unzip=True \n
    Se a busca é por arquivos duplicados informe: duplicate=True
    """

    # Utilizado para identificar arquivos que pertencem a cada fornecedor
    if concessionaria == 'Bandeirante':
        if position == 'begin':
            if unzip == True:
                file_begin_unzip_band = "CARTAO_"
                return file_begin_unzip_band
            if duplicate == True:
                identify_duplicate = "CARTAO_TODOS_"
                return identify_duplicate
            else:
                file_begin_band = "CARTAO_"
                return file_begin_band
        elif position == 'end':
            if unzip == True:
                file_end_unzip_band = "_CONV.TXT"
                return file_end_unzip_band
            if duplicate == True:
                identify_duplicate_final = ").ZIP"
                return identify_duplicate_final
            else:
                file_end_band = "_CONV.ZIP"
                return file_end_band
    if concessionaria == 'ESCELSA':
        if position == 'begin':
            if unzip == True:
                file_begin_escelsa = "498_COBR_"
                return file_begin_escelsa
            if duplicate == True:
                identify_duplicate = "498_COBR_"
                return identify_duplicate
            else:
                file_begin_escelsa = "498_COBR_"
                return file_begin_escelsa
        elif position == 'end':
            if unzip == True:
                file_end_unzip_escelsa = "_CONV.TXT"
                return file_end_unzip_escelsa
            if duplicate == True:
                identify_duplicate_final = ").ZIP"
                return identify_duplicate_final
            else:
                file_end_escelsa = "_CONV.ZIP"
                return file_end_escelsa

if __name__ == '__main__':

    print(identify_file('Bandeirante', 'begin'))
    print(identify_file('Bandeirante', 'end', unzip=True))
    print(identify_file('Bandeirante', 'begin', duplicate=True))

    print(return_folder('Bandeirante'))
