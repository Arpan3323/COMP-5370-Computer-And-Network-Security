#!/usr/bin/python3

import hashlib
import random
import string
import sys
import base64

def generateRandomInput():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

def bruteForce(emailwithNullByte):
    randomCharOne = generateRandomInput()
    inputOne = emailwithNullByte + randomCharOne
    inputOneB64 = base64.b64encode(inputOne.encode()).decode()
    hashOne = hashlib.sha256(inputOneB64.encode()).hexdigest()
    firstThreeBytesOfHashOne = bytes.fromhex(hashOne)[:3]
    while True:
        randomCharTwo = generateRandomInput()
        inputTwo = emailwithNullByte + randomCharTwo
        inputTwoB64 = base64.b64encode(inputTwo.encode()).decode()
        hashTwo = hashlib.sha256(inputTwoB64.encode()).hexdigest()
        firstThreeBytesOfHashTwo = bytes.fromhex(hashTwo)[:3]
        if firstThreeBytesOfHashOne == firstThreeBytesOfHashTwo:
            sys.stdout.write(inputOneB64 + "\n" + inputTwoB64 + "\n")
            exit(0)

def main():
    email = "azs0239@auburn.edu"
    nullByte = '\x00'
    emaiWithNullByte = email[:3] + nullByte + email[3:]
    bruteForce(emaiWithNullByte)

if __name__ == "__main__":
    main()

