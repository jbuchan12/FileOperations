from Services import Utils
from Models import DBEntity
import sqlite3

__dataFolderPath = "/Users/jbuchan12/Documents/Source/FileOperations/Data/Data.db"
__conn : sqlite3.Connection = sqlite3.connect(__dataFolderPath)

def createTable(obj : DBEntity.DbEntity):

    classProperties = Utils.getPublicProperties(obj)
    className = obj.__class__.__name__
    columnsString = ""

    for prop in classProperties:
        columnsString += f"{prop} text "

    sql = f"CREATE TABLE {className} ( {columnsString} )"

    c = __conn.cursor()
    c.execute(sql)
    