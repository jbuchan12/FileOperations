from Services import FileService

#Get all the files from a given directory
def main():
    files = FileService.get_files("/Users/jbuchan12/Documents/Video/*.*")

main()