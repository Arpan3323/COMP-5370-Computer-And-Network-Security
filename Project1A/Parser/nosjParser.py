'''
Created on August 20, 2023

@author: Arpan Srivastava
'''
import sys
import re
import urllib.parse

def readFile(fileContents):
    #key, value = unpackObject(fileContents)
    for key, value in unpackObject(fileContents).items():
        if validateKey(key):
            sys.stdout.write("begin-map\n")
            if validateMap(value):
                #sys.stdout.write(f"begin-map\n")
                sys.stdout.write(f"{key} -- map -- " + "\n")
                #sys.stdout.write(f"end-map\n")
                readFile(value)
            elif validateNum(value):
                parsedNum = unpackNum(value)
                sys.stdout.write(f"{key} -- num -- {parsedNum}" + "\n")
            elif validateSimpleString(value):
                parsedString = unpackSimpleString(value)
                sys.stdout.write(f"{key} -- string -- {parsedString}" + "\n")
            elif validateComplexString(value):
                parsedString = unpackComplexString(value)
                sys.stdout.write(f"{key} -- string2 -- {parsedString}" + "\n")
        
        sys.stdout.write("end-map\n")
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

def validateSimpleString(simpleString):
    pattern = r'^[a-zA-Z0-9\s\t]+s$'
    return bool(re.match(pattern, simpleString))

def unpackSimpleString(simpleString):
    return simpleString.replace('s', '')

def validateComplexString(complexString):
    pattern = r'%[0-9A-F]{2}'
    searchIndexes = []
    if '%' in complexString:
        for i in range(len(complexString)):
            if complexString[i:i+1] == '%':
                searchIndexes.append(i)
        
        for index in searchIndexes:
            if index + 3 > len(complexString):
                return False  # Not enough characters left for valid encoding
            
            match = re.match(pattern, complexString[index:index+3])
            if not match:
                return False  # Invalid percent encoding found
        
        return True  # All percent encodings are valid

def unpackComplexString(complexString):
    return urllib.parse.unquote(complexString)
    #pattern = r'%[0-9A-Fa-f]{2}'
    #return bool(re.search(pattern, complexString))

def validateMap(map):
    pattern = r'^<<[a-z]+:.*>>$'
    return bool(re.match(pattern, map))



def unpackObject(fileContents):
    keys = []
    values = []
    contentDictionary = {}
    removeTopMapPattern = r'^<<(.*)>>$'
    removedTopMap = re.sub(removeTopMapPattern, r'\1', fileContents)
    if ',' in removedTopMap:
        keyValuePairs = removedTopMap.split(',')
        for pair in keyValuePairs:
            key, value = pair.split(':', 1)
            contentDictionary[key] = value
            #keys.append(key)
            #values.append(value)
        return contentDictionary
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
            sys.stdout.write("begin-map\n")
            sys.stdout.write(" -- -- \n")
            sys.stdout.write("end-map\n")
        else:
            readFile(fileContents)
    except Exception as e:
        error.write(f"ERROR -- Invalid file name. Please re-check the file name and try again. -- {e}\n")
        exit(66)