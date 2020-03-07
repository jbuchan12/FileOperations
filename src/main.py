from Services import FileService
import DirectoryComparer

#Get all the files from a given directory
def main():
    comparer = DirectoryComparer.DirComparer("/Users/jbuchan12/Documents/Source/FileOperations/","/Users/jbuchan12/Downloads/")
    comparer.logDifferences()
    
main()