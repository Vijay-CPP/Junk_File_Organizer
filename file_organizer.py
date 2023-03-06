# Importing the libraries
import os
from pathlib import Path

DIRECTORIES = {
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif", ".psd",],

    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp",],

    "Documents": [
        ".csv", ".oxps", ".epub", ".pages",".docx", ".doc", ".fdf", ".ods",".odt", ".pwi", ".xsn", ".xps",".dotx", ".docm", ".dox", ".rvg",
        ".rtf", ".rtfd", ".wpd", ".xls",".xlsx", ".ppt", ".pptx", ".pptm",".xml",],

    "Archives": [".a", ".ar", ".cpio", ".iso",".tar", ".gz", ".rz", ".7z",".dmg", ".rar", ".xar", ".zip",],

    "Audio": [".aac", ".aa", ".aac", ".dvf",".m4a", ".m4b", ".m4p", ".mp3",".msv", "ogg", "oga", ".raw",".vox", ".wav", ".wma",],

    "Text Files": [".txt"],
    
    "PDF Files": [".pdf"],
    
    "Source Codes": [".py", ".c", ".cpp", ".java", ".css", ".js", ".jsx", ".html5", ".html", ".htm", ".xhtml", ".go",".o", ".php", ".ejs", ".coffee",
        ".cmd", ".asp", ".aspx", ".atom",".vscode", ],
    
    "Font Files" : [
        ".abf", ".otf", ".ttf", ".woff"],

    "Programs": [".exe", ".msi"],
    
    "Command Shell": [".sh"],

    "MATLAB Source Files" : [".m"],

    "PSpice Source Files" : [".sch", ".dat", ".csd", 
        ".out", ".cir", ".sim", ".slb"],

    "Temporary Files" : [".tmp", ".temp"]
}

FILE_FORMATS = {}
# Creating the file format dictionary || Key -> Extension || Value -> Folder Name
for i in DIRECTORIES:
    for j in DIRECTORIES[i]:
        FILE_FORMATS[j] = i


def organize_junk():
    # Deletes the empty folders
    for dir in os.scandir():
        try:
            os.rmdir(dir)
        except:
            pass

    for entry in os.scandir():
        # Entry -> Directory Entry Name

        # If directory is itself a folder then leave
        if entry.is_dir():
            continue

        # File name -> Actuall name of the file
        file_name = Path(entry)

        # Fetching the file extension
        file_extension = file_name.suffix.lower()

        if file_extension in FILE_FORMATS:
            # Fetching Name of the folder
            folder_name = Path(FILE_FORMATS[file_extension])

            # Creating the actual folder
            folder_name.mkdir(exist_ok=True)

            # Moving that file to particular folder
            file_name.rename(folder_name.joinpath(file_name))

# Function
organize_junk()

