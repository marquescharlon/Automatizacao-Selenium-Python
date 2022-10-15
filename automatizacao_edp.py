
import download_files
import ftp_server

def main() -> None:

    download_files.download('Bandeirante')
    download_files.download('ESCELSA')

    ftp_server.copy_70('Bandeirante')
    ftp_server.copy_70('ESCELSA')

if __name__ == '__main__':
    main()