'''
Created on August 20, 2023

@author: Arpan Srivastava
'''

import unittest
import subprocess
#import nosjParser as njp

#   Analysis: Project1A.nosjParser
#        inputs:
#            file: a nosj formatted input file (passed as the first command line argument)
#        output: 
#            side-effects:
#
#            nominal: 
#                     deserealize the input file and print the description to standard output (stdout). 
#                     The description should be formatted as follows: "key—name -- type -- value" 
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
#                
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


if __name__ == "__main__":
    unittest.main()