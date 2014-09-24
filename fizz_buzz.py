#!/usr/bin/env python

import argparse


class FizzBuzz(object):

    def fizzbuzzify(self, num):
        # Put your code here.
        pass  # Be sure to change this to a return statement of some sort.


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='FizzBuzz program.')
    parser.add_argument('--start', type=int, help='start of range', default=1)
    parser.add_argument('--end', type=int, help='end of range', default=101)
    args = parser.parse_args()
    start = args.start
    end = args.end

    for num in xrange(start, end):
        print(FizzBuzz().fizzbuzzify(num))
