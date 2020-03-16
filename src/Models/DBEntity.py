import uuid
import datetime
from abc import ABCMeta

class DbEntity(metaclass=ABCMeta):
    Id : uuid
    Created : datetime