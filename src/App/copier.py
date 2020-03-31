import sys

def copy():
    print("Copying...")

def program():

    if len(sys.argv) < 2:
        print("Command not provided")
        return
    command = sys.argv[1].lower()
    if(command == "copy"):
        copy()
        return
    
    print("Command not found, exiting")

program()
