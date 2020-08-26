def parathese(string):
    if len(string) == 0:
        return dict()
    res = dict()
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(i)
        elif stack[i] == ')':
            cur_index = stack.pop()
            res[cur_index] = i

    return res
