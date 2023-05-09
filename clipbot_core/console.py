#!/usr/bin/env python

from enum import Enum
import os
os.system('color')  # enable color in the console

# Global Variables
INFOMATION = True
UPDATES = True
WARNINGS = True
ERRORS = True

class color(Enum):
    UPDATE = '\033[92m'
    INFO = '\033[94m'   # default blue
    WARNING = '\033[93m'    # default yellow
    FAIL = '\033[91m'   # default red
    END = '\033[0m'


def error(s: str = 'Some error has occurred') -> None:
    """error message. Exits out of program
    
    Args:
        s (str, optional): error message to print. Defaults to 'Some error has occurred'.
    """
    if ERRORS:
        # pick whatever error message you think looks coolest
        print(f"{color.FAIL.value}(!) error:{color.END.value} {s}")
        #print(f"{color.FAIL.value}[ERROR]{color.END.value} {s}")


def warning(s: str) -> None:
    """warning message

    Args:
        s (str): warning message to print
    """
    if WARNINGS:
        print(f"{color.WARNING.value}(!) warning:{color.END.value} {s}") 


def info(s: str) -> None:
    """info message

    Args:
        s (str): info message to print
    """
    if INFOMATION:
        print(f"{color.INFO.value}(-){color.END.value} {s}")


def update(s: str) -> None:
    """update message

    Args:
        s (str): update message to print
    """
    if UPDATES:   
        print(f"{color.UPDATE.value}(+){color.END.value} {s}")


def print_info(b: bool) -> None:
    global INFOMATION
    INFOMATION = b


def print_updates(b: bool) -> None:
    global UPDATES
    UPDATES = b


def print_warnings(b: bool) -> None:
    global WARNINGS
    WARNINGS = b


def print_errors(b: bool) -> None:
    global ERRORS
    ERRORS = b


def clear() -> None:
    """clears console screen
    """
    os.system('cls') if os.name == 'nt' else os.system('clear')


def display() -> None:
    """display screen for console cli
    """    
    clear()
    print(R'''Welcome to clipbot!
     ____
 ___/    \___
/ . '----' . \
'--________--'
     //\\
    ///\\\
   ////\\\\
  /////\\\\\
''')

__all__ = ['error', 'warning', 'info', 'update',
           'clear', 'display', 'print_info', 'print_updates', 
           'print_warnings', 'print_errors']
