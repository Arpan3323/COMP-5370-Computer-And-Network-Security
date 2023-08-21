'''
Created on August 20, 2023

@author: Arpan Srivastava
'''
import sys

if __name__ == "__main__":
    error = sys.stderr
    output = sys.stdout

    if len(sys.argv) != 2:
       error.write("ERROR -- Invalid number of arguments\n")
       exit(66)
    
    fileToRead = sys.argv[1]

    try:
        file = open(fileToRead, "r")
    except:
        error.write("ERROR -- Invalid file name. Please re-check the file name and try again.\n")
        exit(66)