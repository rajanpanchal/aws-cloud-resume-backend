import unittest
from getCounter import *


class TestDynamoDB(unittest.TestCase):
       
    def test_getCounter(self):
        value1 = getCounter();
        #print(value1)
        self.assertTrue(value1 > 0);   

if __name__ == '__main__':
    
    unittest.main()

