import os.path
import os
import zipfile as zf

def files(source_folder:str='', file_begin:str='', file_end:str='', delete_file=False):

    """
    Pasta onde se encontram os arquivos: source_folder='' \n
    Pesquisar pelo início do arquivo: file_begin='' \n
        p.identify_file(concessionaria, 'begin') \n
    Pesquisar pelo final do arquivo: file_end='' \n
        p.identify_file(concessionaria, 'end') \n
    Deseja excluir o arquivo .ZIP? delete_file=True
    """

    files = os.listdir(source_folder)

    for file in files:
        if file_begin in file:
            if file_end in file:

                path = os.path.join(rf'{source_folder}', file)

                with zf.ZipFile(rf"{path}") as z:
                    z.extractall(rf'{source_folder}')

                if delete_file == True:
                    os.remove(rf"{path}")

if __name__ == '__main__':

    import parameters as p

    concessionaria = ''

    files(
        p.temp_folder, 
        p.identify_file(concessionaria, 'begin'), 
        p.identify_file(concessionaria, 'end'), 
        delete_file=False
    )