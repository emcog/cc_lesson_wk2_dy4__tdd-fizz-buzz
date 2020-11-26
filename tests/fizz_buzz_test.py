import unittest

from src.fizz_buzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    # if number can be divided by 3 return Fizz
    def test_fizz_buzz__3_returns_fizz(self):
        self.assertEqual('fizz', fizz_buzz(3))