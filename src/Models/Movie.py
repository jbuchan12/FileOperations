from Models import DBEntity

class Movie(DBEntity.DbEntity):
    name : str
    fileSize : int
    def __init__(self, name):
        self.name = name