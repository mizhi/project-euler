#!/usr/bin/env python

# Each character on a computer is assigned a unique code and the
# preferred standard is ASCII (American Standard Code for Information
# Interchange). For example, uppercase A = 65, asterisk (*) = 42, and
# lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes
# to ASCII, then XOR each byte with a given value, taken from a secret
# key. The advantage with the XOR function is that using the same
# encryption key on the cipher text, restores the plain text; for
# example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain
# text message, and the key is made up of random bytes. The user would
# keep the encrypted message and the encryption key in different
# locations, and without both "halves", it is impossible to decrypt
# the message.
#
# Unfortunately, this method is impractical for most users, so the
# modified method is to use a password as a key. If the password is
# shorter than the message, which is likely, the key is repeated
# cyclically throughout the message. The balance for this method is
# using a sufficiently long password key for security, but short
# enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of
# three lower case characters. Using cipher1.txt (right click and
# 'Save Link/Target As...'), a file containing the encrypted ASCII
# codes, and the knowledge that the plain text must contain common
# English words, decrypt the message and find the sum of the ASCII
# values in the original text.


import fileinput
import sys


def decrypt(msg, key):
    newm = []

    for ki in xrange(0, len(msg)):
        newm.append(msg[ki] ^ key[ki % len(key)])
        ki += 1

    return newm

# load message
matrix_file = sys.argv[-1]
fi=fileinput.input(matrix_file)
cmessage=[]
for l in fi:
    nums=[int(i) for i in l.split(",")]
    cmessage.extend(nums)
fileinput.close()

# load up filter words
fi=fileinput.input('/usr/share/dict/words')
words=set([w.lower().strip() for w in fi])
fileinput.close()



# generate all possible keys
print "Generating keys..."        
lower_case=[ord(c) for c in 'abcdefghijklmnopqrstuvwxyz']
keys = []
for i in lower_case:
    newkey=[i]
    for j in lower_case:
        newkey.append(j)
        for k in lower_case:
            newkey.append(k)
            keys.append(tuple(newkey))
            newkey.pop()
        newkey.pop()

print "Decrypting...", len(keys)

# brute decrypt
pmessages = {}
for k in keys:
    pmessages[k] = "".join([chr(c) for c in decrypt(cmessage, k)])

    for c in pmessages[k]:
        if not (ord(c) >= ord(' ') and ord(c) <= ord('z')):
            del pmessages[k]
            break

print "Summing... ", len(pmessages.keys())

for k,m in pmessages.items():
    if 'the' in m.lower():
        print m, sum([ord(c) for c in m])

print "Candidates..."

    

