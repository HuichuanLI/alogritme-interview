class Solution:
    def isValid(self, s):
        stack = []
        a = ['(', '[', '{']
        b = [')', ']', '}']
        for ele in s:
            if ele in ['(', '[', '{']:
                stack.append(ele)
            elif ele in [')', ']', '}']:
                if len(stack) > 0:
                    p_ele = stack.pop()
                    for tempa, tempb in zip(a, b):
                        if tempa == ele and p_ele == tempb:
                            continue
                        else:
                            return False

                else:
                    return False
        return True