'''
Created on August 20, 2023

@author: Arpan Srivastava
'''
import sys
import re

def readFile(fileContents):
    key, value = unpackObject(fileContents)
    
    sys.stdout.write(key + " -- type -- " + value + "\n")

def validateKey(key):
    pattern = r'^[a-z]+$'
    if re.match(pattern, key):
        return True
    else:
        return False

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
    except:
        error.write("ERROR -- Invalid file name. Please re-check the file name and try again.\n")
        exit(66)