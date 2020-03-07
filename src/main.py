import glob

#Get all the files from a given directory
def main():
    files = get_files("/Users/jbuchan12/Documents/Video/*.*")

#Get all the files in a given directory
def get_files(path : str):
    dirs = glob.glob(path)
    return dirs

main()