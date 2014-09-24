#!/usr/bin/env python

import argparse


class FizzBuzz(object):

    def fizzbuzzify(self, num):
        fizz_buzz = ''
        if num == 0:
            return str(num)
        if num % 3 == 0 or '3' in str(num):
            fizz_buzz += 'Fizz'
        if num % 5 == 0 or '5' in str(num):
            fizz_buzz += 'Buzz'
        return fizz_buzz if len(fizz_buzz) else str(num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='FizzBuzz program.')
    parser.add_argument('--start', type=int, help='start of range', default=1)
    parser.add_argument('--end', type=int, help='end of range', default=101)
    args = parser.parse_args()
    start = args.start
    end = args.end

    for num in xrange(start, end):
        print(FizzBuzz().fizzbuzzify(num))
