#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__version__  0.1.0
@author: gy18qz (Zhao Qianchen) by Python 3.7
"""

import matplotlib.pyplot

"""
Step 1: Read the file.
"""
print("Step 1: Read the file.")
file = 'snow.slope'
fp = open(file)
snowslope = []
for line in fp.readlines():
    line = line[:-2]
    line = line.split(' ')
    tmp = []
    for l in line:
        tmp.append(int(l))
    snowslope.append(tmp)
fp.close()

"""
Step 2: Plot the heights.
"""
print("Step 2: Plot the heights.")
matplotlib.pyplot.imshow(snowslope)
matplotlib.pyplot.show()

"""
Step 3: Calculate the slopes.
"""
print("Step 3: Calculate the slopes.")
def boundary(x, y, w, h):
    # if (x, y) in (w, h)
    if x >= 0 and y >= 0 and x < w and y < h:
        return True
    return False

w = len(snowslope)
h = len(snowslope)
slopes = []
for i in range(w):
    line = []
    for j in range(h):
        m = 0
        if boundary(i - 1, j, w, h):
            if m < abs((snowslope[i][j] - snowslope[i - 1][j]) / 1):
                m = abs((snowslope[i][j] - snowslope[i - 1][j]) / 1)
                
        if boundary(i + 1, j, w, h):
            if m < abs((snowslope[i][j] - snowslope[i + 1][j]) / 1):
                m = abs((snowslope[i][j] - snowslope[i + 1][j]) / 1)
                
        if boundary(i, j - 1, w, h):
            if m < abs((snowslope[i][j] - snowslope[i][j - 1]) / 1):
                m = abs((snowslope[i][j] - snowslope[i][j - 1]) / 1)
                
        if boundary(i, j + 1, w, h):
            if m < abs((snowslope[i][j] - snowslope[i][j + 1]) / 1):
                m = abs((snowslope[i][j] - snowslope[i][j + 1]) / 1)
                
        if boundary(i - 1, j - 1, w, h):
            if m < abs((snowslope[i][j] - snowslope[i - 1][j - 1]) / 2 ** 0.5):
                m = abs((snowslope[i][j] - snowslope[i - 1][j - 1]) / 2 ** 0.5)

        if boundary(i - 1, j + 1, w, h):
            if m < abs((snowslope[i][j] - snowslope[i - 1][j + 1]) / 2 ** 0.5):
                m = abs((snowslope[i][j] - snowslope[i - 1][j + 1]) / 2 ** 0.5)

        if boundary(i + 1, j - 1, w, h):
            if m < abs((snowslope[i][j] - snowslope[i + 1][j - 1]) / 2 ** 0.5):
                m = abs((snowslope[i][j] - snowslope[i + 1][j - 1]) / 2 ** 0.5)

        if boundary(i + 1, j + 1, w, h):
            if m < abs((snowslope[i][j] - snowslope[i + 1][j + 1]) / 2 ** 0.5):
                m = abs((snowslope[i][j] - snowslope[i + 1][j + 1]) / 2 ** 0.5)
                
        line.append(m)
    slopes.append(line)

"""
Step 4: Plot the slope gradients.
"""
print("Step 4: Plot the slope gradients.")
matplotlib.pyplot.imshow(slopes)
matplotlib.pyplot.show()

"""
Step: 5 Build the dataset.
"""
print("Step 5: Build the dataset.")
fp = open('slope.txt', 'w')
for line in slopes:
    for l in line:
        fp.write(str(l))
        fp.write(' ')
    fp.write('\n')