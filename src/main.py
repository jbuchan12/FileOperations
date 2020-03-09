from Services import FileService
import DirectoryComparer

#Get all the files from a given directory
def main():

    videoFolderUri = "/Users/jbuchan12/Documents/Video/"
    dirs = FileService.getDirs(videoFolderUri)

    for d in dirs:
        FileService.tidyFileName(d)
        # FileService.removeSmallFiles(d)

    #TODO Need to fix the filename to remove brackets etc
    
main()