import sys

line_length = int(sys.stdin.readline().strip())
line = ""
nums_words = 0
while 1:
    cur = sys.stdin.readline().strip()
    nums_words = len(cur.split())
    if cur:
        line.append(cur)
    else:
        break
