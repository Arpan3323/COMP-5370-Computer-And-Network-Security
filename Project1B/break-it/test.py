import unittest
import subprocess
import nosjParser as njp



class Test(unittest.TestCase):

    def test(self):
        result = subprocess.run(['python3', 'nosjParser.py', 'tc-1.input'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(result.returncode, 66)
        self.assertEqual(result.stdout.decode('utf-8'), 'ERROR -- Invalid value found: \n')
    def test001_randomTest(self):
        #actualResult = njp.unpackObject('<<abc:<<a:f0.0f>>>>')
        #self.assertEqual(actualResult, ('abc','<<a:f0.0f>>'))
        actualResult = njp.readFile('<<a:s>>')

if __name__ == '__main__':
    unittest.main()