#!/bin/python3

import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    a = meal_cost*(tip_percent/100)
    b = meal_cost*(tax_percent/100)
    #print(a,b)
    f = meal_cost+a+b
    print(round(f))
    
if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
