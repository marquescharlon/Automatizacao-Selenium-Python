
def translation(folder):
    if folder == "Downloads":
        return "Downloads"
    elif folder == "Documentos" or folder == "Documents":
        return "Documents"
    elif folder == "Imagens" or folder == "Pictures":
        return "Pictures"
    elif folder == "Videos":
        return "Videos"
    else:
        return folder