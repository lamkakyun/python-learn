#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 求平方命令
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('square', help="display the square of given number", type=int) # positional args
parser.add_argument('-v', '--verbose', action="store_true", help="verbose")

args = parser.parse_args()
if args.verbose:
    print("the square of {} equals {}".format(args.square, args.square ** 2))
else: print(args.square ** 2)