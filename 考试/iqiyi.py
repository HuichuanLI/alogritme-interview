import sys
import re
from collections import defaultdict

line = sys.stdin.readline().strip()

dict = sys.stdin.readline().strip()

array = dict.split()

hash_dict = defaultdict(str)
for elem in array:
    cur_str = ""
    for index in range(len(elem)):
        if index == 0:
            cur_str = elem[index]
        else:
            cur_str += "\s*" + elem[index]
    hash_dict[cur_str] = " " + elem + " "
for key, value in hash_dict.items():
    line = re.sub(key, value, line)

print(" ".join(line.split()))
