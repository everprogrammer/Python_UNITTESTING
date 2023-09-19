import unittest
import Calculator.calculator as calculator

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        # Happy Path Testing, (LHS) == (RHS)
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(10, -5), 5)
        self.assertEqual(calculator.add(-10, -5), -15)

    def test_sub(self):
        self.assertEqual(calculator.sub(10, 5), 5)
        self.assertEqual(calculator.sub(10, -5), 15)
        self.assertEqual(calculator.sub(-10, -5), -5)

    def test_mul(self):
        self.assertEqual(calculator.mul(10, 5), 50)
        self.assertEqual(calculator.mul(10, -5), -50)
        self.assertEqual(calculator.mul(-10, -5), 50)
        self.assertEqual(calculator.mul(-10, 0), 0)
        self.assertEqual(calculator.mul(10, 0), 0)
    
    def test_div(self):
        self.assertEqual(calculator.div(10, 5), 2)
        self.assertEqual(calculator.div(10, -5), -2)
        self.assertEqual(calculator.div(-10, -5), 2)
        # Sad Path testing, I know that an error will raise
        with self.assertRaises(ZeroDivisionError):
            calculator.div(10, 0)


