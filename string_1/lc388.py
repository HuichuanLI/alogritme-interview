import re
from collections import defaultdict


class Solution:
    def lengthLongestPath(self, input):
        # Write your code here
        dict = defaultdict(str)
        lines = input.split("\n")

        n = len(lines)
        result = 0
        for i in range(n):
            count = lines[i].count("\t")
            lines[i] = dict[count - 1] + re.sub("\\t+", "/", lines[i])
            if "." in lines[i]:
                result = max(result, len(lines[i]))
            dict[count] = lines[i]

        return result
