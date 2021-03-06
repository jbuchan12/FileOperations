import glob
import os
from shutil import copyfile
from typing import List

#Get all the files in a given directory
def getFiles(path : str) -> List[str]:
    dirs = glob.glob(path + "*.*")
    return dirs

#Get only the directories in a given directory
def getDirs(path : str) -> List[str]:
    dirs = glob.glob(path + "/*/")
    return dirs

#Recursively loop through a directory returning all directories
def tree(path : str) -> List[str]:
    result = []
    dirs = getDirs(path)
    if len(dirs) == 0:
        return result

    for dir in dirs:
        result.append(dir)
        subdirs = tree(dir)
        if len(subdirs) == 0:
            continue
        result = result + subdirs

    return result

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

def tidyFileName(filename : str):
    result = ""

#todo swap out .for whitespace
    slashSplit = filename.split("/")
    file = slashSplit[len(slashSplit) - 2]
    spaceSplit = file.split(" ")

    index = 0
    for string in spaceSplit:
        
        string = string.replace("(","")
        string = string.replace(")","")

        if string.isupper():
            continue
        if index > 1 and string.isdigit():
            break

        result += string + " "
        index = index + 1

    result = result.rstrip()
    
    newPath = filename.replace(file + "/","")
    os.rename(filename,newPath + result)

def getLowestDirectory(path : str) -> str:
    slashSplit = path.split("/")
    return slashSplit[len(slashSplit) - 2]



    

    