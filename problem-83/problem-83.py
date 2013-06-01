#!/usr/bin/env python


# The minimal path sum in the 5 by 5 matrix below, by starting in any
# cell in the left column and finishing in any cell in the right
# column, and only moving up, down, and right, is indicated in red;
# the sum is equal to 994.
#
# Find the minimal path sum, in matrix.txt (right click and 'Save
# Link/Target As...'), a 31K text file containing a 80 by 80 matrix,
# from the left column to the right column.

import fileinput
import sys

matrix_file = sys.argv[-1]
fi=fileinput.input(matrix_file)
weights=[]
for l in fi:
    nums=[int(i) for i in l.split(",")]
    weights.append(nums)
fileinput.close()

def neighbors(m, u):
    r = set()
    max_r = len(m) - 1
    max_c = len(m[0]) - 1

    # if not all the way to the left,
    # add left neighbor
    if u[1] > 0:
        r.add((u[0], u[1] - 1))

    # if not all the way to the right
    # add right neighbor
    if u[1] < max_c:
        r.add((u[0], u[1] + 1))
    
    # if not at top, add upper neighbor
    if u[0] > 0:
        r.add((u[0] - 1, u[1]))

    # if no at bottom, add lower neighbor
    if u[0] < max_r:
        r.add((u[0] + 1, u[1]))

    return r

def dijkstra(m, source):
    """Takes cost matrix m and source and computes
    shortest path to all other "nodes.
    """
    dist={None: sys.maxint}
    previous={}
    unvisited=set()
    for r in xrange(len(m)):
        for c in xrange(len(m[r])):
            dist[(r,c)] = sys.maxint
            previous[(r,c)] = None            
            unvisited.add((r,c))
    dist[source] = m[source[0]][source[1]]
    
    while unvisited:        
        # find node with smalled dist
        u = None
        for n in unvisited:
            if dist[n] < dist[u]:
                u = n
        unvisited.discard(u)

        nv = unvisited & neighbors(m, u)
        for v in nv:
            alt = dist[u] + m[v[0]][v[1]]
            if alt < dist[v]:
                dist[v] = alt
                previous[v] = u

    return previous

def sum_dijkstra_path(m, prevlist, target):
    t = target
    csum = 0

    if t not in prevlist:
        return sys.maxint

    while t:
        print t
        csum += m[t[0]][t[1]]
        t = prevlist[t]

    return csum
        

print "%dx%d matrix" % (len(weights), len(weights[0]))

# iterate through all starting row,cols
path = dijkstra(weights, (0,0))
min_sum = sum_dijkstra_path(weights, path, (len(weights) - 1, len(weights[0]) - 1))

print min_sum
