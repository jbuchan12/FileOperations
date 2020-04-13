import uuid
import time

class DbEntity():
    Id : uuid
    Created : float
    def __init__(self):
        self.Id = uuid.uuid1().hex
        self.Created = time.time