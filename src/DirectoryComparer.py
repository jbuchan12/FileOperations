from Services import FileService
from typing import List

class DirectoryComparer:
    m_DirPathA : str
    m_DirPathB : str
    m_Diffences : List[str]

    #Constructor
    def __init__(self, dirPathA,dirPathB):
        self.m_DirPathA = dirPathA
        self.m_DirPathB = dirPathB

    def getDifferences(self, parameter_list):
        pass
