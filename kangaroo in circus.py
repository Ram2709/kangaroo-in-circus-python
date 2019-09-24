# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 19:24:15 2019

@author: Ram
"""

import sys
def kangaroo(x1, v1, x2, v2):
    if v1 > v2:
        if (x2 - x1) % (v2 - v1) == 0:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
    # Complete this function

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

    

    
