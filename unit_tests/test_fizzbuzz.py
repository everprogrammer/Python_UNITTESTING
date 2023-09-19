import unittest
import TDD_FizzBuzz.fizzbuzz as fb

# 3 Steps involved in TDD:
## 1. write a failing test
## 2. make the test pass
## 3. refactor

class TestFizzBuzz(unittest.TestCase):

    # You can also comment out the test below as refactoring, but I keep it
    def test_canCallFizzBuzz(self):
        fb.fizzbuzz(1)

    def checkValWithExpected(self, val, expected):
        ret = fb.fizzbuzz(val)
        self.assertEqual(ret, expected)

    def test_callFizzBuzzReturn1WhenPassed1(self):
        # self.assertEqual(fb.fizzbuzz(1), '1')

        # Refactoring
        self.checkValWithExpected(1, '1')

    def test_callFizzBuzzReturn2WhenPassed2(self):
        # self.assertEqual(fb.fizzbuzz(2), '2')

        # Refactoring
        self.checkValWithExpected(2, '2')

    def test_callFizzBuzzReturnFizzWhenPassed3(self):
        self.checkValWithExpected(3, 'Fizz')

    def test_callFizzBuzzReturnBuzzWhenPassed5(self):
        self.checkValWithExpected(5, 'Buzz')

    def test_callFizzBuzzReturnFizzWhenPassedMultiple3(self):
        self.checkValWithExpected(6, 'Fizz')
        self.checkValWithExpected(9, 'Fizz')
        self.checkValWithExpected(12, 'Fizz')

    def test_callFizzBuzzReturnBuzzWhenPassedMultiple5(self):
        self.checkValWithExpected(10, 'Buzz')
        self.checkValWithExpected(20, 'Buzz')
        self.checkValWithExpected(40, 'Buzz')
        self.checkValWithExpected(50, 'Buzz')


    def test_callFizzBuzzReturnFizzBuzzWhenPassed15(self):
        self.checkValWithExpected(15, 'FizzBuzz')
        self.checkValWithExpected(30, 'FizzBuzz')
        self.checkValWithExpected(45, 'FizzBuzz')
        self.checkValWithExpected(60, 'FizzBuzz')
