from Services import Utils
from Models import DBEntity
import sqlite3

__dataFolderPath = "/Users/jbuchan12/Documents/Source/FileOperations/Data/Data.db"
__conn : sqlite3.Connection = sqlite3.connect(__dataFolderPath)

def createTable(obj : DBEntity.DbEntity):

    classProperties = Utils.getPublicProperties(obj)
    className = obj.__class__.__name__
    columnsString = ""

    index = 0
    for prop in classProperties:
        if(len(classProperties) - 1 == index):
            columnsString += f"{prop} text "
            break
        columnsString += f"{prop} text, "
        index += 1

    sql = f"CREATE TABLE {className} ({columnsString})"

    c = __conn.cursor()
    c.execute(sql)

def insertInto(obj : DBEntity.DbEntity):

    tableName = obj.__class__.__name__

    sql = f"INSERT INTO {tableName} (Id,Name) VALUES ('{obj.Id}','{obj.Name}')"

    c = __conn.cursor()
    c.execute(sql)
    __conn.commit()

    