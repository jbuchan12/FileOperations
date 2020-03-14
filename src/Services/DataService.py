import sqlite3

dataFolderPath = "/Users/jbuchan12/Documents/Source/FileOperations/Data/Data.db"

#Create a database at the location
def createDatabase():
    __conn = sqlite3.connect(dataFolderPath)
    