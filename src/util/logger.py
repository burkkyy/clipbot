'''
@file util/logger.py
@author Caleb Burke
@date 2024-02-15

A simple logger class impl.

TODO Make logger class singleton
TODO Add storing logs in files
TODO Run logger in a seperate thread
'''

import os
os.system('color')

class Logger:
    def __init__(self):
        # set severity default colors
        self.FATAL      = "\033[91m"    # default red
        self.ERROR      = "\033[91m"    # default red
        self.WARNING    = "\033[93m"    # default yellow
        self.INFO       = "\033[92m"    # default green
        self.VERBOSE    = "\033[96m"    # default cyan
        self.DEBUG      = "\033[37m"    # default gray
        self.TRACE      = "\033[90m"    # default light gray       
        self.END_COLOR  = "\033[0m"     # For "exiting" out of color text

    def console_print(self, msg: str, severity: str, severity_color: str) -> None:
        print(f"{severity_color}[{severity}]{self.END_COLOR} {msg}")

    def fatal(self, msg: str) -> None:
        # just print to screen for now
        self.console_print(msg, "FATAL", self.FATAL)

    def error(self, msg: str) -> None:
        # just print to screen for now
        self.console_print(msg, "ERROR", self.ERROR)

    def warning(self, msg: str) -> None:
        # just print to screen for now
        self.console_print(msg, "WARNING", self.WARNING)

    def info(self, msg: str) -> None:
        # just print to screen for now
        self.console_print(msg, "INFO", self.INFO)

    def verbose(self, msg: str) -> None:
        # just print to screen for now
        self.console_print(msg, "VERBOSE", self.VERBOSE)

    def debug(self, msg: str) -> None:
        # just print to screen for now
        self.console_print(msg, "DEBUG", self.DEBUG)

    def trace(self, msg: str) -> None:
        # just print to screen for now
        self.console_print(msg, "TRACE", self.TRACE)

