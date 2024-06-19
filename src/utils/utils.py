import os

def clear():
    '''Cleans terminal screen'''
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")