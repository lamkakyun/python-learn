#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# optparse 是不建议使用的，使用argparse，这是它基本的用法
import argparse

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('echo', help="echo the string you use here") # positional args, 必须指定值
parser.add_argument('square', type=int, help="display a square of given number=") # 必须指定值
parser.add_argument('--verbosity', help="increase output verbosity") # optional args, 必须指定值
parser.add_argument('--verbose', help="increase output verbosity2", action="store_true") # 必须不指定值
parser.add_argument('-v2', '--verbose2', help="increase output verbosity3", action="store_true") # short args, 必须不指定值
parser.add_argument('-v3', '--verbose3', help="increase output verbosity4") # short args, 必须指定值
args = parser.parse_args()

print(args)
print(args.echo)
print(args.square**2)
print(args.verbosity)
print(args.verbose)
print(args.verbose2)
print(args.verbose3)
