import sys

line = sys.stdin.readline().strip()

result = []
res = ""
index = 1


def check_number(res):
    if len(res) < 6:
        res = "0" * (6 - len(res)) + res
    return res


for elem in line:
    if index % 5 == 1:
        res += " "
    if ord(elem) >= ord('A') and ord(elem) <= ord('Z'):
        res += check_number(bin(ord(elem) - ord("A") + 27)[2:])

    elif ord(elem) >= ord('a') and ord(elem) <= ord('z'):
        res += check_number(bin(ord(elem) - ord("a") + 1)[2:])

    elif ord(elem) >= ord('0') and ord(elem) <= ord('9'):
        res += check_number(bin(ord(elem) - ord("0") + 27 + 26)[2:])
    else:
        res += "0" * 6
    index += 1
if index > 5:
    print(" ".join([str(int(elem, 2)) for elem in res.split()]))
else:
    print(int(res, 2))
