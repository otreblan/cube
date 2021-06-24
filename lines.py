#!/usr/bin/env python3

from time import sleep

n = 60

i = 0

while True:
    print('0,0,{}'.format(i), flush=True)
    i = (i+0.1)%360
    sleep(1/n)
