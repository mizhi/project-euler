#!/usr/bin/env python

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 5
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
#
# NOTE: This is a much more difficult version of Problem 18. It is not
# possible to try every route to solve this problem, as there are 299
# altogether! If you could check one trillion (1012) routes every
# second it would take over twenty billion years to check them
# all. There is an efficient algorithm to solve it. ;o)

import fileinput
import sys

matrix_file = sys.argv[-1]
fi=fileinput.input(matrix_file)
weights=[]
for l in fi:
    nums=[int(i) for i in l.split(" ")]
    weights.append(nums)
fileinput.close()

def max_path_dyn(ws):
    m=[[ws[0][0]]]

    # this loop also computes the outer edges of the triangle
    for w in ws[1:]:
        newm=[w[0] + m[-1][0]] + (len(w) - 2) * [0] + [w[-1] + m[-1][-1]]
        m.append(newm)

    for j in xrange(2,len(ws)):
        for i in xrange(1,j):
            m[j][i] = max(m[j-1][i], m[j-1][i-1]) + ws[j][i]

    return max(m[-1])

print max_path_dyn(weights)

