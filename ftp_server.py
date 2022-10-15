from ftplib import FTP
import security as pw
import sys
import os
import parameters as p
sys.path.insert(0, 'C:\\Repositorios\\Projetos_Python\\')
import function_models.function_models as fm

ftp_70 = FTP()

# Evite adicionar senha aqui
# Se adicionado no arquivo security.py você poderá chamá-lo assim como fiz aqui

def copy_70(concessionaria):

    global str_log
    str_log = ""

    folder_136 = f'C:\\{concessionaria}\\Retorno\\'
    path_70 = f'/Cobranca/{concessionaria}/Retorno'
 
    try:
        ftp_70.connect(pw.ftp70_host, pw.ftp70_porta)
        ftp_70.login(pw.ftp70_username, pw.ftp70_password)
        ftp_70.encoding = 'utf-8' 
        str_log += fm.LogMensagem('C_SFTP',servidor=pw.ftp70_host)
        ftp_70.nlst()

        ftp_70.cwd(f'/Cobranca/{concessionaria}/Retorno')

        list_files = os.listdir(folder_136)

        qtd_file = 0

        for file in list_files:
            if '.TXT' in file:
                fileObject  = open(folder_136 + file, 'rb')
                ftp_70.storlines('STOR ' + file, fileObject)
                ftp_70.retrbinary('RETR ' + file,
                                  open(folder_136 + 'Baixados\\' + file, 'wb').write)
                fileObject.close()

                str_log += fm.LogMensagem('SCA',filename=file,servidor=p.folder_70 + path_70)
                qtd_file+=1 

                if os.path.exists(folder_136 + file):
                    os.remove(folder_136 + file)

        if qtd_file == 0:
            str_log += fm.LogMensagem(tipo='P', mensagem='Site verificado, porém, nenhum retorno para ser baixado.')

        fm.EnviaEmail(destinatario=pw.email_cobranca, assunto_email='Log Retorno ' + concessionaria, modelo_html='', mensagem=str_log, 
        cabecalho=True, titulo_cabecalho=concessionaria)
     
    except Exception as ex:
        str_log += fm.LogMensagem('E_SFTP',servidor=pw.ftp70_host,erro=ex)

if __name__ == '__main__':
    
    copy_70('Bandeirante')
    copy_70('ESCELSA')