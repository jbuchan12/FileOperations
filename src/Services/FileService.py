import glob
from shutil import copyfile

#Get all the files in a given directory
def getFiles(path : str):
    dirs = glob.glob(path + "*.*")
    return dirs

#Copies a file from one dir to another
def copyFile(fileName : str, fromPath : str, toPath : str, overwriteExistingFiles = False):
    if not doesDirContainFile(fromPath,fileName):
        raise NameError(fileName + " Not found in " + fromPath)
    if doesDirContainFile(toPath,fileName) and not overwriteExistingFiles:
        raise NameError(toPath + " already contains " + fileName)
    copyfile(fromPath + fileName,toPath + fileName)

#Does the given directory contain the given file
def doesDirContainFile(directory : str, fileName : str):
    fromFiles = getFiles(directory)
    if len(fromFiles) < 1:
        raise NameError("No files in" + directory)
    for path in fromFiles:
        if path == directory + fileName:
            return True
    return False