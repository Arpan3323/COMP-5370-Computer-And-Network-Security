'''
Created on August 20, 2023

@author: Arpan Srivastava
'''
import sys

def readFile(fileContents):
    checkEmptyMap(fileContents)
    #for content in fileContents:
     #   if content[0:2] == "<<" and content[-1:] == ">>":
      #      print(" -- -- ")

def checkEmptyMap(fileContents):
    if fileContents == "<<>>":
        sys.stdout.write(" -- -- \n")
        
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
        readFile(fileContents)
    except:
        error.write("ERROR -- Invalid file name. Please re-check the file name and try again.\n")
        exit(66)