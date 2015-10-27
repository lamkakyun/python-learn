#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import itertools

# example 1
# ns = itertools.repeat('A', 10)
# for i in ns:
#     print i

# example 2
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x : x <= 10, natuals)
for i in ns:
    print i

# example 3
for c in itertools.chain('ABC', 'XYZ'):
    print c

# example 4
for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group)

# example 5
for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
    print x