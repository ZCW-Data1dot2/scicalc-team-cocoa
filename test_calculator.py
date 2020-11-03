import unittest
import unittest.mock as mk
from calculator import Calculator

class TestCalculator(unittest.TestCase):


    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(10,5), 15)

    def test_add2(self):
        calc = Calculator()
        self.assertEqual(calc.add(100.5,5), 105.5)

    def test_sub(self):
        calc = Calculator()
        self.assertEqual(calc.sub(10,5), 5)

    def test_sub2(self):
        calc = Calculator()
        self.assertEqual(calc.sub(100.5,5), 95.5)

    def test_mul(self):
        calc = Calculator()
        self.assertEqual(calc.mul(5,5), 25)

    def test_mul2(self):
        calc = Calculator()
        self.assertEqual(calc.mul(2.5, 2.5), 6.25)

    def test_div(self):
        calc = Calculator()
        self.assertEqual(calc.div(6,3), 2)

    def test_div2(self):
        calc = Calculator()
        self.assertEqual(calc.div(11,2),5.5)

    def test_squ(self):
        calc = Calculator()
        self.assertEqual(calc.squ(10), 10000000000)

    def test_squ2(self):
        calc = Calculator()
        self.assertEqual(calc.squ(5.5), 11803.064820864423)

    def test_roo(self):
        calc = Calculator()
        self.assertEqual(calc.roo(26), 5.0990195135927845 )

    def test_roo2(self):
        calc = Calculator()
        self.assertEqual(calc.roo(9),3)

    def test_exp(self):
        calc = Calculator()
        self.assertEqual(calc.exp(10,3), 1000)

    def test_exp2(self):
        calc = Calculator()
        self.assertEqual(calc.exp(6,5.5),19047.232239881992 )

if __name__ == '__main__':
    unittest.main()

