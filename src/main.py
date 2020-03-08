from Services import FileService
import DirectoryComparer

#Get all the files from a given directory
def main():

    videoFolderUri = "/Users/jbuchan12/Documents/Video/"
    dirs = FileService.getDirs(videoFolderUri)

    for d in dirs:
        FileService.removeSmallFiles(d)
    
main()