import glob

#Get all the files in a given directory
def get_files(path : str):
    dirs = glob.glob(path)
    return dirs