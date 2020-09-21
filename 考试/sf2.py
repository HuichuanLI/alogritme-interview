from collections import Counter


def findNumber(num):
    res = []
    s = bin(num)
    s = list(s[::-1])
    for index, elem in enumerate(s):
        if elem == '1':
            last_1 = index
            break
    for index, elem in enumerate(s):
        if elem == '0':
            last_0 = index
            break
    if last_0 > last_1:
        s[last_0], s[last_1] = s[last_1], s[last_0]

        res.append(int("".join(s), 2))
    else:
        res.append(num * 2)

    s = bin(num)[2:]
    s = list(s)
    for index, elem in enumerate(s):
        if elem == '1':
            first_1 = index
            break
    for index, elem in enumerate(s):
        if elem == '0':
            first_0 = index
            break
    if first_1 < first_0:
        s[first_0], s[first_1] = s[first_1], s[first_0]
        res.append(int("0b" + "".join(s), 2))
    else:
        res.append(-1)

    return res


print(findNumber(3))
