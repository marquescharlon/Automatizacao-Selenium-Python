import os.path
import parameters as p

def result_qtd(source_folder, file_begin, file_end):
    list_files = os.listdir(source_folder)

    qtd_file = 0

    for file in list_files:
        if file_end in file:
            if file_begin in file:        
                qtd_file += 1 

    return qtd_file

def result_file(source_folder):
    list_files = os.listdir(source_folder)
    return list_files

def duplicate_qtd(source_folder,identify_duplicate, identify_duplicate_final):
    list_files = os.listdir(source_folder)
    
    qtd_file = 0

    for file in list_files:
        if identify_duplicate in file:
            if identify_duplicate_final in file:        
                qtd_file += 1 

    return qtd_file

def await_file(source_folder, file_begin, file_end):
    list_files = os.listdir(source_folder)

    qtd_file = 0
    
    for file in list_files:
        if file_begin in file:
            if file_end in file:
                qtd_file+=1
    return qtd_file


if __name__ == '__main__':

    concessionaria = 'Bandeirante'

    print(
      duplicate_qtd(
          p.downloads_folder, 
          p.identify_file(concessionaria, 'begin', duplicate=True), 
          p.identify_file(concessionaria, 'end', duplicate=True)
      )
    )

    print(
      result_qtd(
          p.downloads_folder, 
          p.identify_file(concessionaria, 'begin'), 
          p.identify_file(concessionaria, 'end')
      )
    )

    print(await_file(
        p.downloads_folder,
        p.identify_file(concessionaria, 'begin'), 
        ".ZIP.crdownload"
    ))