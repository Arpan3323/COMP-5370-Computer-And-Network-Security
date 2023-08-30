'''
Created on August 20, 2023

@author: Arpan Srivastava
'''
import sys
import re
import urllib.parse


def readFile(fileContents):
    #key, value = unpackObject(fileContents)
    writeToStdout = "begin-map\n"
    #sys.stdout.write("begin-map\n")
    for key, value in unpackObject(fileContents).items():
        if checkEmptyMap(key, value):
            writeToStdout += " -- -- " + "\n"
            #sys.stdout.write(" -- -- " + "\n")
        elif validateKey(key):
            if validateMap(value):
                #sys.stdout.write(f"{key} -- map -- " + "\n")
                writeToStdout += f"{key} -- map -- " + "\n"
                writeToStdout += readFile(value)
                #readFile(value)
            elif validateNum(value):
                parsedNum = unpackNum(value)
                #sys.stdout.write(f"{key} -- num -- {parsedNum}" + "\n")
                writeToStdout += f"{key} -- num -- {parsedNum}" + "\n"
            elif validateSimpleString(value):
                parsedString = unpackSimpleString(value)
                writeToStdout += f"{key} -- string -- {parsedString}" + "\n"
                #sys.stdout.write(f"{key} -- string -- {parsedString}" + "\n")
            elif validateComplexString(value):
                parsedString = unpackComplexString(value)
                writeToStdout += f"{key} -- string2 -- {parsedString}" + "\n"
                #sys.stdout.write(f"{key} -- string2 -- {parsedString}" + "\n")
    #sys.stdout.write("end-map\n")
    writeToStdout += "end-map\n"
    return writeToStdout

def writeToStdout(parsedObject):
    parsedObject += parsedObject 

    
    #sys.stdout.write(f"{key} -- {value}" + "\n")

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
    return simpleString.replace('s', '', 1)

def unpackComplexString(complexString):
    return urllib.parse.unquote(complexString)
    #pattern = r'%[0-9A-Fa-f]{2}'
    #return bool(re.search(pattern, complexString))

def validateMap(map):
    pattern = r'^<<[a-z]+:.*>>$'
    return bool(re.match(pattern, map))

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




def unpackObject(fileContents):
    if not validateMap:
        return
    contentDictionary = {}
    removedTopMap = re.sub(r'^<<(.*)>>$', r'\1', fileContents)
    if ',' in removedTopMap:
        keyValuePairs = removedTopMap.split(',')
        uniqueKeys = set()
        for pair in keyValuePairs:
            key, value = pair.split(':', 1)
            if key in uniqueKeys:
                error.write(f"ERROR -- Duplicate key found: {key}\n")
                exit(66)
            uniqueKeys.add(key)
            contentDictionary[key] = value
        return contentDictionary
    if removedTopMap == "":
        contentDictionary[""] = removedTopMap
    else:
        keyValuePairs = removedTopMap.split(':', 1)
        contentDictionary[keyValuePairs[0]] = keyValuePairs[1]
    return contentDictionary


def checkEmptyMap(key, value):
    if key == "" and value == "":
        return True
        
if __name__ == "__main__":
    error = sys.stderr
    output = sys.stdout

    if len(sys.argv) != 2:
       error.write("ERROR -- Invalid number of arguments\n")
       exit(66)

    fileToRead = sys.argv[1]

    try:
        file = open(fileToRead, "r")
        fileContents = file.read()
        output.write(readFile(fileContents))
    except Exception as e:
        error.write(f"ERROR -- Invalid file name. Please re-check the file name and try again. -- {e}\n")
        exit(66)

        #vmware workstation player