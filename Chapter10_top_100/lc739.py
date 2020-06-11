class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        res = [0] * len(T)
        for i, elem in enumerate(T):
            j = 0

            for j, elem_max in enumerate(T[i:]):
                if elem < elem_max:
                    break
            if j + i + 1 == len(T) and elem >= elem_max:
                res[i] = 0
            else:
                res[i] = (j + i) - i

        return res


## 递减栈

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0]*len(T)
        for index, elem in enumerate(T):
            if len(stack) == 0:
                stack.append((index, elem))
            elif stack[-1][1] < elem:
                while len(stack) > 0 and stack[-1][1] < elem:
                    res[stack[-1][0]] = index - stack[-1][0]
                    stack.pop()
                stack.append((index, elem))
            else:
                stack.append((index, elem))

        return res
