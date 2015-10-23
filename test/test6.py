#!/usr/bin/python

import os
import platform
import sys
import subprocess

def clear_screen():
    if os.name.lower() == 'posix':
        subprocess.Popen('clear')
    elif os.name.lower() in ('nt', 'dos', 'ce'):
        # subprocess.Popen('cls')
        os.system('cls')

def print_docs():
    print "printing daily check sheets:"
    subprocess.Popen(["C:\\Program Files (x86)\Microsoft Office\Office12\winword.exe", "F:\\test.doc", "/mFilePrintDefault", "/mFileExit"]).communicate()

def euroclear_docs():
    subprocess.Popen('"C:\\Program Files\\Internet Explorer\\iexplore.exe"' '"f:\\test.doc"')

if __name__ == "__main__":
    clear_screen()
    # print_docs()
    euroclear_docs()