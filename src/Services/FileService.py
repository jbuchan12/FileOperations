import glob
import os
from shutil import copyfile
from typing import List

#Get all the files in a given directory
def getFiles(path : str) -> List[str]:
    dirs = glob.glob(path + "*.*")
    return dirs

#Create directory with the directory name at the given location
def createDirectory(path : str, directoryName : str):
    try:
        os.mkdir(path + directoryName)
    except FileExistsError:
        print(directoryName + " already exists in " + path + " skipping")

#Copies a file from one dir to another
def copyFile(fileName : str, fromPath : str, toPath : str, overwriteExistingFiles = False):
    if not doesDirContainFile(fromPath,fileName):
        raise NameError(fileName + " Not found in " + fromPath)
    if doesDirContainFile(toPath,fileName) and not overwriteExistingFiles:
        raise NameError(toPath + " already contains " + fileName)
    copyfile(fromPath + fileName,toPath + fileName)

#Remove a file from the system
def delFile(file):
    os.remove(file)

#Does the given directory contain the given file
def doesDirContainFile(directory : str, fileName : str) -> bool:
    fromFiles = getFiles(directory)
    if len(fromFiles) < 1:
        raise NameError("No files in" + directory)
    for path in fromFiles:
        if path == directory + fileName:
            return True
    return False

#Remove all files in a directory smaller than a certain size
def removeSmallFiles(dir : str, minFileSizeMb = 100):
    files = getFiles(dir)
    if len(files) < 1:
        return

    minByteSize = minFileSizeMb * 1024 * 1024

    for file in files:
        if os.path.getsize(file) < minByteSize:
            delFile(file)

    

    