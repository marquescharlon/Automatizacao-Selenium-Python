import os.path
import language
from pathlib import Path

def create_folder(folder_local:str='', folder_name:str=''):

    """
    folder_local='Downloads', 'Documentos', 'Imagens' ou 'Videos' \n
    folder_name='TESTE' \n
    folder_name='TESTE/Subpasta'
    """

    def folder_name_local(folder_local):
        folder_ = language.translation(folder_local)
        return folder_

    folder_path = os.path.expanduser(rf"~\{folder_name_local(folder_local)}")
        
    print(folder_path)

    def folder_mount(folder_path, folder_name):
        print(folder_name)
        
        _path = folder_path
        _path = os.path.join(rf'{_path}',folder_name)
        print(_path)
        if Path(_path).is_dir():
            print("Diretório '%s' já existe." %_path)
        try:
            os.makedirs(_path)
        except FileExistsError as erro:
            print(erro)

    folder_mount(folder_path, folder_name)


if __name__ == '__main__':

    create_folder("Documentos", "EDP/Temp/Duplicados")