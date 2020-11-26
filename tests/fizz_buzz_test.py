import unittest

from src.fizz_buzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    # if number can be divided by 3 return Fizz
    def test_fizz_buzz__3_returns_fizz(self):
        self.assertEqual('fizz', fizz_buzz(3))

    def test_fizz_buzz__5_returns_buzz(self):
         # if number can be divided by 5 return Buzz
         self.assertEqual('buzz', fizz_buzz(5))

    def test_fizz_buzz__15_returns_fizzbuzz(self):
        self.assertEqual('fizzbuzz', fizz_buzz(15))

    def test_fizz_buzz__4_returns_four(self):
        self.assertEqual('4', fizz_buzz(4))