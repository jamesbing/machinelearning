#!/usr/bin/env python
# coding=utf-8

import random
cups = [0,0,0,0,0]

count = 0

while (cups[0] == cups[1] == cups[2] == cups[3] == cups[4] == 1) is not True:
        id = random.randint(0,4)
        print id
