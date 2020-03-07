from Services import FileService
from enum import Enum
from typing import List

#Enum for type of difference between directories
class DifferenceType(Enum):
    Addition = 1
    Subtraction = 2

#A difference between two directories
class DirDifference:
    fileName : str
    diffType : DifferenceType
    def __init__(self, file,diffType):
        self.fileName = file
        self.diffType = diffType

#The comparer that does comparisons between two directories
class DirComparer:
    __DirPathA : str
    __DirPathB : str
    __Diffences : List[DirDifference]

    #Constructor
    def __init__(self, dirPathA,dirPathB):
        self.__DirPathA = dirPathA
        self.__DirPathB = dirPathB
        if len(dirPathA) == 0 or len(dirPathB) == 0:
            raise NameError("Dir paths cannot be empty strings")
        self.__Diffences = self.__getDifferences()

    #Get the differences between the two directories
    def __getDifferences(self):
        results = []
        diffA = FileService.getFiles(self.__DirPathA)
        diffB = FileService.getFiles(self.__DirPathB)

        if len(diffA) == 0:
            for diff in diffB:
                d = DirDifference(diff,DifferenceType.Addition)
                results.append(d)
            return results

        if len(diffB) == 0:
            for diff in diffA:
                d = DirDifference(diff,DifferenceType.Subtraction)
                results.__add__(d)
            return results

        ignoreList = []

        for diff in diffA:
            if not any(diff in d for d in diffB):
                d = DirDifference(diff,DifferenceType.Addition)
                results.append(d)
                ignoreList.append(diff)
        
        for diff in diffB:
            if not any(diff in d for d in diffA) and not any(diff in d for d in ignoreList):
                d = DirDifference(diff,DifferenceType.Subtraction)
                results.append(d) 

        return results
    
    #Log the differences between the two directories
    def logDifferences(self):
        if len(self.__Diffences) == 0:
            print("No differences detected")
        for difference in self.__Diffences:
            operator = ""

            if difference.diffType == DifferenceType.Addition:
                operator = "+"
            else:
                operator = "-"

            print(difference.fileName + " " + operator)
                

