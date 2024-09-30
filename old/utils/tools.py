import os, time
from typing import Optional

def clear():
    '''Cleans terminal screen'''
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def singleton(cls):
    instances = {}

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrap

def int_input(input_msg: str = "") -> Optional[int]:
    """
    Prompts the user for an integer value.
    If the input is not a valid integer, returns None.

    :param input_msg: The message to display to the user.
    :return: The integer value entered by the user or None if it is not a valid integer.
    """
    try:
        opt = int(input(input_msg))
        return opt
    except ValueError:
        return None
    
def wait(sec: int):
    '''
    Alias for time.sleep()
    :params: sec: Time in seconds to insert in time.sleep()
    '''
    time.sleep(sec)
