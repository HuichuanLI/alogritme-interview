import sys
from collections import Counter

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

if Counter(a) == Counter(b):
    print(1)
else:
    print(0)



