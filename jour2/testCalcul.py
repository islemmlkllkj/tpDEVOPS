import sys
sys.path.append('../src/') 
from calcul import Calcul
import unittest

class TestCalcul(unittest.TestCase):
    
    def test_add(self):
        c = Calcul()
        self.assertEquals(c.add(10,15),25) 
    def test_sous(self):
        c = Calcul()
        self.assertEquals(c.sous(10,6),4) 
    def test_div(self):
        c = Calcul()
        self.assertEquals(c.div(4,2),2) 
    def test_multi(self):
        c = Calcul()
        self.assertEquals(c.multi(4,2),8)    
    def test_div_ko(self):
        c = Calcul()
        with self.assertRaises(ZeroDivisionError):
           c.div(5,0) 

if __name__ == '__main__':
    unittest.main()