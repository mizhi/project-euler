#!/usr/bin/env python

# A common security method used for online banking is to ask the user
# for three random characters from a passcode. For example, if the
# passcode was 531278, they may asked for the 2nd, 3rd, and 5th
# characters; the expected reply would be: 317.
#
# The text file, keylog.txt, contains fifty successful login attempts.
#
# Given that the three characters are always asked for in order,
# analyse the file so as to determine the shortest possible secret
# passcode of unknown length.

import fileinput
import sys

key_file = sys.argv[-1]
fi=fileinput.input(key_file)
keys=set()
for l in fi:
    keys.add(l.strip())
fileinput.close()

def hypfits(h, k):
    if h.index(k[0]) < h.index(k[1]) and h.index(k[1]) < h.index(k[2]):
        return True

    return False


hyp=[]
for k in keys:
    # ensure all digits represented in hyp
    for kd in k:
        if kd not in hyp:
            hyp.append(kd)

    if not hypfits(hyp, k):
        print '---', hyp, k, hypfits(hyp, k)
        # because we know we have all the digits, we know that there are at least 2 digits
        # in hyp that must be swapped to make k fit.
        ik0 = hyp.index(k[0])
        ik1 = hyp.index(k[1])

        # must swap digits for ik0 and ik1
        if ik0 > ik1:
            print '\tMoving %c before %c' % (hyp[ik0], hyp[ik1])
            hyp.insert(ik1, hyp.pop(ik0))

        ik0 = hyp.index(k[0])
        ik2 = hyp.index(k[2])

        # must swap digits for ik0 and ik2
        if ik0 > ik2:
            print '\tMoving %c before %c' % (hyp[ik0], hyp[ik2])
            hyp.insert(ik2, hyp.pop(ik0))

        ik1 = hyp.index(k[1])
        ik2 = hyp.index(k[2])

        if ik1 > ik2:
            print '\tMoving %c before %c' % (hyp[ik1], hyp[ik2])
            hyp.insert(ik2, hyp.pop(ik1))
    else:
        print '+++ ', hyp, k, hypfits(hyp, k)


for k in keys:
    if not hypfits(hyp, k):
        print "*** NOT FIT", hyp, k


print len(keys), len(hyp), hyp
