from Services import FileService
import DirectoryComparer

#Get all the files from a given directory
def main():
    FileService.removeSmallFiles("/Users/jbuchan12/Documents/Video/Once Upon A Time ... In Hollywood/")
    
main()