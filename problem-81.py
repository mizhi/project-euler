#!/usr/bin/env python

#
# Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.
#
# How many routes are there through a 20x20 grid?
#
# (In thie problem, the robot goes on the grid.  In the google treasure hunt problem the robot was on the squares themselves.
# The solution is to increase by 1
#

import fileinput
import sys

matrix_file = sys.argv[-1]
fi=fileinput.input(matrix_file)
weights=[]
for l in fi:
    nums=[int(i) for i in l.split(",")]
    weights.append(nums)
fileinput.close()

def min_path_dyn(ws):
    m=[[ws[0][0]]]
    for w in ws[0][1:]:
        m[0].append(w + m[0][-1])

    for w in ws[1:]:
        newm=[w[0] + m[-1][0]] + (len(ws[0]) - 1) * [0]
        m.append(newm)

    for j in xrange(1,len(ws)):
        for i in xrange(1,len(ws[j])):
            m[j][i] = min(m[j-1][i],m[j][i-1]) + ws[j][i]

    return m[-1][-1]

def min_path_mem(h, w, ws, mdict={}):
    if not (h,w) in mdict:
        if h == 1 and w == 1:
            mdict[(h,w)] = ws[h-1][w-1]
        elif h == 1:
            mdict[(1,w)] = ws[0][w-1] + min_path_mem(1, w - 1, ws)
        elif w == 1: 
            mdict[(h,1)] = ws[h-1][0] + min_path_mem(h - 1, 1, ws)
        else: 
            mdict[(h,w)] = ws[h-1][w-1] + min(min_path_mem(h, w-1, ws), min_path_mem(h-1, w, ws))
    return mdict[(h,w)]

print min_path_dyn(weights)
print min_path_mem(len(weights), len(weights[0]), weights)
