#!/usr/bin/env python

##Comparing two numbers written in index form like 211 and 37 is not
##difficult, as any calculator would confirm that 211 = 2048  37 = 2187.
##
##However, confirming that 632382^518061  519432^525806 would be much more
##difficult, as both numbers contain over three million digits.
##
##Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K
##text file containing one thousand lines with a base/exponent pair on
##each line, determine which line number has the greatest numerical
##value.
##
##NOTE: The first two lines in the file represent the numbers in the
##example given above.

import fileinput
import sys
import math

matrix_file = sys.argv[-1]
fi=fileinput.input(matrix_file)

max_line = 0
max_num = 0
line_no = 0
for l in fi:
    line_no += 1
    base_exp=[int(i) for i in l.split(",")]
    exp = base_exp[1];
    base = base_exp[0];
    cnum = exp * math.log(base)
    if cnum > max_num:
        max_num = cnum
        max_line = line_no
    
fileinput.close()

print max_line
