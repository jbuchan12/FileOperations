from Services import FileService
from enum import Enum

class DifferenceType(Enum):
    Addition = 1
    Subtraction = 2

class DirDifference:
    fileName : str
    diffType : DifferenceType
    def __init__(self, file,diffType):
        self.fileName = file
        self.diffType = diffType

class DirComparer:
    __DirPathA : str
    __DirPathB : str
    __Diffences : list

    #Constructor
    def __init__(self, dirPathA,dirPathB):
        self.__DirPathA = dirPathA
        self.__DirPathB = dirPathB
        if len(dirPathA) == 0 or len(dirPathB) == 0:
            raise NameError("Dir paths cannot be empty strings")
        self.__Diffences = self.__getDifferences()

    #Get the differences between the two directories
    def __getDifferences(self):
        results = list
        diffA = FileService.getFiles(self.__DirPathA)
        diffB = FileService.getFiles(self.__DirPathB)

        if len(diffA) == 0:
            for diff in diffB:
                d = DirDifference(diff,DifferenceType.Addition)
                results.append(d)
            pass

        if len(diffB) == 0:
            for diff in diffA:
                d = DirDifference(diff,DifferenceType.Subtraction)
                results.append(d)
            pass

        for diff in diffA:
            if not any(diff in d for d in diffB):
                d = DirDifference(diff,DifferenceType.Addition)
                results.append(d)
        
        for diff in diffB:
            if not any(diff in d for d in diffA):
                d = DirDifference(diff,DifferenceType.Subtraction)
                results.append(d) 

        return results
    
    #Log the differences between the two directories
    def logDifferences(self):
        diffList = self.__Diffences.copy()
        if len(diffList) == 0:
            print("No differences detected")
        for difference in diffList:
            operator = ""

            if difference.diffType == DifferenceType.Addition:
                operator = "+"
            else:
                operator = "-"

            print(difference + " " + operator)
                

