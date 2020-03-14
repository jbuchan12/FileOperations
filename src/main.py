from Services import FileService
from Services import DataService
import DirectoryComparer

#Get all the files from a given directory
def main():

    DataService.createDatabase()

    
    # videoFolderUri = "/Users/jbuchan12/Documents/Video/"
    # dirs = FileService.getDirs(videoFolderUri)

    # for d in dirs:
    #     FileService.tidyFileName(d)
    #     # FileService.removeSmallFiles(d)

    # #TODO Need to fix the filename to remove brackets etc
    
main()