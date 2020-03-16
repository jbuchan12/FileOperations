from typing import List
import inspect

def getPublicProperties(obj : object) -> List[str]:
    classProps = []
    for prop  in inspect.getmembers(obj):
        if not prop[0].startswith("__"):
            classProps.append(prop[0])
    return classProps