'''
Created on August 20, 2023

@author: Arpan Srivastava
'''

import sys
sys.path.append('.\Project1A')
import unittest
import subprocess
import Parser.nosjParser as njp

#   Analysis: Project1A.nosjParser
#        inputs:
#            file: a nosj formatted input file (passed as the first command line argument)
#        output: 
#            side-effects:
#
#            nominal: 
#                     deserealize the input file and print the description to standard output (stdout). 
#                     The description should be formatted as follows: "key-name -- type -- value" 
#                     (no trailing or leading spaces other than trailing newline).
#                     If the object is a map, In the case that a map is encountered, your implementation MUST leave 
#                     the value field of the above line empty and output a stand-alone line of "begin-map".
#                     When the end of a map is encountered, your implementation MUST output a stand-alone line of "end-map'.
#
#            abnormal: 
#                     if input errors are encountered, print a one line error message to standard error (stderr) and exit with
#                     a status code of 66. The error message must begin with the string "ERROR -- " (and end with a single trailing newline).
#
#   happy path tests:
#                100: valid file with an empty map. print " -- -- " to stdout
#                101: valid file with a nosj num object in a map. print "key-name -- type -- 0.0" to stdout
#                102: return true if the key is valid. map keys MUST be an ascii-string 
#                     consisting of one or more lowercase letters ("a" through "z") only
#                103: determine if the value is a num. num consists of the ascii-character "f", an
#                     optional ascii-dash representing a negative-sign ("-"), one or more
#                     ascii-digits ("0" through "9"), a decimal point, one or more ascii-digits ("0"
#                     through "9"), and the ascii-character "f"
#
#    sad path tests:
#                901: file not found. print "ERROR -- Invalid file name. Please re-check the file name and try again." to stderr and exit with status code 66
#
#    evil path test:
#                none


class nosjParserTest(unittest.TestCase):
    
    def test901_invalidFile(self):
        result = subprocess.run(['python', 'Project1A\Parser\\nosjParser.py', 'nosjParserTest901.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #print("STDOUT:", result.stdout.decode('utf-8'))
        #print("STDERR:", result.stderr.decode('utf-8'))
        self.assertEqual(result.returncode, 66)
        self.assertEqual(result.stderr.decode('utf-8'), 'ERROR -- Invalid file name. Please re-check the file name and try again.\r\n')

    def test100_emptyMap(self):
        result = subprocess.run(['python', 'Project1A\Parser\\nosjParser.py', 'Project1A\inputs\\nosjParserTest100.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(result.stdout.decode('utf-8'), ' -- -- \r\n')

    def test101_basicNumObject(self):
        #exceptedResult = sys.stdout.write("key-name -- type -- 0.0\n")
        #actualResult = njp.readFile('<<abc:f0.0f>>')
        result = subprocess.run(['python', 'Project1A\Parser\\nosjParser.py', 'Project1A\inputs\\nosjParserTest101.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(result.stdout.decode('utf-8'), 'abc -- type -- f0.0f\r\n')
        #self.assertEqual(actualResult, exceptedResult)
    
    def test102_validKey(self):
        actualResult = njp.validateKey('abc')
        self.assertEqual(actualResult, True)

    def test102_0_invalidKey(self):
        actualResult = njp.validateKey('ABC')
        self.assertEqual(actualResult, False)
    
    def test000_randomTest(self):
        actualResult = njp.unpackObject('<<abc:f0.0f>>')
        self.assertEqual(actualResult, ('abc','f0.0f'))

    def test001_randomTest(self):
        actualResult = njp.unpackObject('<<abc:<<a:f0.0f>>>>')
        self.assertEqual(actualResult, ('abc','<<a:f0.0f>>'))


if __name__ == "__main__":
    unittest.main()