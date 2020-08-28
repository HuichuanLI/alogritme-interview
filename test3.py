import sys


def lengthOfLongestSubstring(s: str):
    if len(s) == 0:
        return 0
    ans = 0
    j = 0
    for i in range(len(s)):
        while j < len(s) and len(set(s[i:j + 1])) == j - i + 1:
            ans = max(ans, j - i + 1)
            j += 1

    return ans


res = []
while 1:
    line1 = sys.stdin.readline().strip()
    if line1:
        res.append(lengthOfLongestSubstring(line1))
    else:
        break
for elem in res:
    print(elem)
