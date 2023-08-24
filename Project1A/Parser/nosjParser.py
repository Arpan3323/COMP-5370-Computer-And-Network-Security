'''
Created on August 20, 2023

@author: Arpan Srivastava
'''
import sys
import re

def readFile(fileContents):
    key, value = unpackObject(fileContents)
    if validateKey(key):
        if validateNum(value):
            parsedNum = unpackNum(value)
            sys.stdout.write(f"{key} -- num -- {parsedNum}" + "\n")
        '''else:
            sys.stdout.write("begin-map\n")
            readFile(value)
            sys.stdout.write("end-map\n")'''

def validateKey(key):
    pattern = r'^[a-z]+$'
    return bool(re.match(pattern, key))

def validateNum(num):
    pattern = r'^f-?[0-9]+\.[0-9]+f$'
    return bool(re.match(pattern, num))
    
def unpackNum(num):
    return num.replace('f', '')

def unpackObject(fileContents):
    keys = []
    values = []
    removeTopMapPattern = r'^<<(.*)>>$'
    removedTopMap = re.sub(removeTopMapPattern, r'\1', fileContents)
    keyValuePairs = removedTopMap.split(':', 1)
    return keyValuePairs[0], keyValuePairs[1]


def checkEmptyMap(fileContents):
    if fileContents == "<<>>":
        return True
        
if __name__ == "__main__":
    error = sys.stderr
    #output = sys.stdout

    if len(sys.argv) != 2:
       error.write("ERROR -- Invalid number of arguments\n")
       exit(66)

    fileToRead = sys.argv[1]

    try:
        file = open(fileToRead, "r")
        fileContents = file.read()
        if fileContents == "<<>>":
            sys.stdout.write(" -- -- \n")
        else:
            readFile(fileContents)
    except Exception:
        error.write("ERROR -- Invalid file name. Please re-check the file name and try again.\n")
        exit(66)