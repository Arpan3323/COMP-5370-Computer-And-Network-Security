import sys

toBeOutputted = ""
emailName = "azs0239"
toBeOutputted += emailName
length = 3
nullByte = "\0"
toBeOutputted += nullByte*length
grade = "A+"
toBeOutputted +=  grade
sys.stdout.write(toBeOutputted)

