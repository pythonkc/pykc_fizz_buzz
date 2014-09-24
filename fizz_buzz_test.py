#!/usr/bin/env python

import unittest
from fizz_buzz import FizzBuzz


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.fizz_buzz = FizzBuzz()

    def test_fizzbuzzify_handles_zero(self):
        self.assertEqual('0', self.fizz_buzz.fizzbuzzify(0))

    def test_fizzbuzzify_handles_multiples_of_three(self):
        self.assertEqual('Fizz', self.fizz_buzz.fizzbuzzify(3))

    def test_fizzbuzzify_handles_multiples_of_five(self):
        self.assertEqual('Buzz', self.fizz_buzz.fizzbuzzify(5))

    def test_fizzbuzzify_handles_multiples_of_three_and_five(self):
        self.assertEqual('FizzBuzz', self.fizz_buzz.fizzbuzzify(15))

    def test_fizzbuzz_handles_three_in_num(self):
        self.assertEqual('Fizz', self.fizz_buzz.fizzbuzzify(13))

    def test_fizzbuzzify_handles_five_in_num(self):
        self.assertEqual('Buzz', self.fizz_buzz.fizzbuzzify(52))

    def test_fizzbuzzify_handles_three_and_five_in_num(self):
        self.assertEqual('FizzBuzz', self.fizz_buzz.fizzbuzzify(53))

if __name__ == '__main__':
    unittest.main()
