from contextlib import nullcontext
import os.path
from pathlib import Path
import consult_folder
import parameters as p

def move_files(source_folder:str='', file_begin:str='', file_end:str='', destination_folder:str='', qtd_site=0):

    """
    Pasta onde se encontram os arquivos: source_folder='' \n
        Pasta Downloads: p.downloads_folder \n
        Pasta Temp: p.temp_folder \n
        Pasta Temp/Duplicados: p.temp_duplicados \n
        Ou a pasta de retorno: return_folder(concessionaria) \n
    Pesquisar pelo início do arquivo: file_begin='' \n
        p.identify_file(concessionaria, 'begin') \n
        p.identify_file(concessionaria, 'begin', duplicate=True) \n
        p.identify_file(concessionaria, 'begin', unzip=True) \n
    Pesquisar pelo final do arquivo: file_end='' \n
        p.identify_file(concessionaria, 'end') \n
        p.identify_file(concessionaria, 'end', duplicate=True) \n
        p.identify_file(concessionaria, 'end', unzip=True) \n
    Pasta de destino: destination_folder='' \n
    Verificar se a quantidade baixada é o mesmo que consta na pasta: qtd_site=''
    """

    qtd_site_ = qtd_site

    files_folder = consult_folder.result_qtd(source_folder, file_begin, file_end)
    qtd_files_folder = 0

    list_files =  consult_folder.result_file(source_folder)

    if qtd_site_ != 0:

        if int(qtd_site) != int(files_folder):
            qtd_files_folder = files_folder
            
            while qtd_site > qtd_files_folder:
                qtd_files_folder = 0
                for file in list_files:
                    if file_begin in file:
                        if file_end in file:
                            print(file)
                            qtd_files_folder += 1
                            list_files =  consult_folder.result_file(source_folder)

        if int(qtd_site) == int(qtd_files_folder) or int(qtd_site) == int(files_folder):
            list_files = os.listdir(source_folder)
            print(list_files)
            for file in list_files:
                if file_begin in file:
                    if file_end in file:
                        try:
                            if os.path.exists(f"{destination_folder}/{file}"):
                                os.remove(f"{destination_folder}/{file}")
                            os.rename(f"{source_folder}/{file}", f"{destination_folder}/{file}")
                        except FileNotFoundError as erro:
                            print(erro)
                        except TypeError as erro:
                            print(erro)
                        except Exception as erro:
                            print("Ocorreu um erro diferente dos que já foram tratados ao tentar mover arquivo(s)")
    else:
        list_files = os.listdir(source_folder)
        for file in list_files:
            if file_begin in file:
                if file_end in file:
                    try:
                        if os.path.exists(f"{destination_folder}/{file}"):
                            os.remove(f"{destination_folder}/{file}")
                        os.rename(f"{source_folder}/{file}", f"{destination_folder}/{file}")
                    except FileNotFoundError as erro:
                        print(erro)
                    except TypeError as erro:
                        print(erro)
                    except Exception as erro:
                        print("Ocorreu um erro diferente dos que já foram tratados ao tentar mover arquivo(s)")

def move_files_duplicates(source_folder:str='',identify_duplicate:str='', identify_duplicate_final:str='', destination_folder:str=''):

    """
    Pasta onde se encontram os arquivos: source_folder='' \n
        Pasta Downloads: p.downloads_folder \n
        Pasta Temp: p.temp_folder \n
        Pasta Temp/Duplicados: p.temp_duplicados \n
        Ou a pasta de retorno: return_folder(concessionaria) \n
    Pesquisar pelo início do arquivo: identify_duplicate='' \n
        p.identify_file(concessionaria, 'begin', duplicate=True) \n
    Pesquisar pelo final do arquivo: identify_duplicate_final='' \n
        p.identify_file(concessionaria, 'end', duplicate=True) \n
    Pasta de destino: destination_folder=''
    """

    list_files = os.listdir(source_folder)

    for file in list_files:
        if identify_duplicate in file:
            if identify_duplicate_final in file:        
                try:
                    if os.path.exists(f"{destination_folder}/{file}"):
                        os.remove(f"{destination_folder}/{file}")
                    os.rename(f"{source_folder}/{file}", f"{destination_folder}/{file}")
                except FileNotFoundError as erro:
                    print(erro)
                except FileExistsError as erro:
                    print(erro)

if __name__ == '__main__':

    concessionaria = ''

    move_files(
        p.downloads_folder, 
        p.identify_file(concessionaria, 'begin'), 
        p.identify_file(concessionaria, 'end'),
        p.temp_folder,
        9
    )

    move_files_duplicates(
        p.downloads_folder,
        p.identify_file(concessionaria, 'begin', duplicate=True), 
        p.identify_file(concessionaria, 'end', duplicate=True), 
        p.temp_duplicados
    )

    move_files(
        p.temp_folder, 
        p.identify_file(concessionaria, 'begin', unzip=True), 
        p.identify_file(concessionaria, 'end', unzip=True), 
        p.return_folder(concessionaria)
    )