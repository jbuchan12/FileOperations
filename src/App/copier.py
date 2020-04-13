import sys
from Services import FileService

def copy(srcDir : str, destDir : str):
    srcFiles = FileService.getFiles(srcDir)
    destFiles = FileService.getFiles(destDir)

def program():

    if len(sys.argv) < 2:
        print("Command not provided")
        return
    command = sys.argv[1].lower()

    if command == "copy" and len(sys.argv) == 4:
        copy(sys.argv[2],sys.argv[3])
        return
    
    print("Command not found, exiting")

program()
