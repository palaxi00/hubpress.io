from sympy.combinatorics.graycode import gray_to_bin
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        stringe = test.strip()
        liststringe = stringe.split(" | ")
        print (" | ".join([str(int(gray_to_bin(i),2)) for i in liststringe]))