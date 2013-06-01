#!/usr/bin/env python

#
# Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.
#
# How many routes are there through a 20x20 grid?
#
# (In thie problem, the robot goes on the grid.  In the google treasure hunt problem the robot was on the squares themselves.
# The solution is to increase by 1
#

def all_paths_dyn(h,w):
    m=[[1 for i in xrange(w)]]
    for j in xrange(1,h):
        m.append([1] + (w-1) * [0])
        for i in xrange(1,w):
            m[j][i] = m[j-1][i] + m[j][i-1]
    return m[h-1][w-1]

def all_paths_mem(h,w, mdict={}):
    if not (h,w) in mdict:
        if h == 1 or w == 1: return 1
        else: mdict[(h,w)] = mdict[(w,h)] = all_paths_mem(h, w-1) + all_paths_mem(h-1,w)
    return mdict[(h,w)]

print all_paths_dyn(21,21)
