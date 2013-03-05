#!/usr/bin/env python

# If the numbers 1 to 5 are written out in words: one, two, three,
# four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in
# total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were
# written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three
# hundred and forty-two) contains 23 letters and 115 (one hundred and
# fifteen) contains 20 letters. The use of "and" when writing out
# numbers is in compliance with British usage.

digits={
0: "zero",
1: "one",
2: "two",
3: "three",
4: "four",
5: "five",
6: "six",
7: "seven",
8: "eight",
9: "nine"
}

teens={
10: "ten",
11: "eleven",
12: "twelve",
13: "thirteen",
14: "fourteen",
15: "fifteen",
16: "sixteen",
17: "seventeen",
18: "eighteen",
19: "nineteen"
}

afterteens={
20: "twenty",
30: "thirty",
40: "forty",
50: "fifty",
60: "sixty",
70: "seventy",
80: "eighty",
90: "ninety"
}

def num_to_english(n):
    rwords = []
    if n >= 0 and n <= 9:
        rwords.append(digits[n])
    elif n >= 10 and n < 20:
        rwords.append(teens[n])
    elif n >= 20 and n < 100:
        tens = (n / 10) * 10
        rem = n % 10
        rwords.append(afterteens[tens])
        if rem != 0:
            rwords.extend(num_to_english(rem))
    elif n >= 100 and n < 1000:
        hundreds = (n / 100)
        rem = n % 100
        rwords.extend([digits[hundreds], "hundred"])
        if rem != 0:
            rwords.append("and")
            rwords.extend(num_to_english(rem))
    elif n >= 1000 and n < 1000000:
        thousands = (n / 1000)
        rem = n % 1000
        rwords.extend(num_to_english(thousands))        
        rwords.append("thousand")
        if rem != 0:
            rwords.extend(num_to_english(rem))

    return rwords

def list_string_len(a,b):
    _a = a
    _b = b
    if type(a) is str:
        _a = len(a)
    if type(b) is str:
        _b = len(b)

    return _a + _b
    

sums=[]
for i in xrange(1, 1001):
    english = num_to_english(i)
    if len(english) > 1:        
        sums.append(reduce(list_string_len, english))
    else:
        sums.append(len(english[0]))
    print i, " ".join(english)

print sums
print sum(sums)
