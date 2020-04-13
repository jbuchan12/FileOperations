from Models import DBEntity

class Movie(DBEntity.DbEntity):
    Name : str
    FileSize : int
    def __init__(self, name):
        self.Name = name
        super().__init__()