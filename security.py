# FTP
ftp70_host = ""
ftp70_username = ""
ftp70_password = ""
ftp70_porta = 0

# Servidor
siparq = ""

# Conexão com o Banco  
driver = "{SQL Server Native Client 11.0}"
name_db = ""
user_db = ""
password_db = ""

# E-mail
email_cobranca = ""
email_teste = ""

def user(concessionaria, tipo):
    if concessionaria == 'Bandeirante':
        if tipo == 'User':
            username_field = ''
            return str(username_field)
        if tipo == 'Password':
            password_field = ''
            return str(password_field)
    if concessionaria == 'ESCELSA':
        if tipo == 'User':
            username_field = ''
            return str(username_field)
        if tipo == 'Password':
            password_field = ''
            return str(password_field)