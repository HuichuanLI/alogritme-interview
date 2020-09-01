import sys


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        max_array = [0] * n
        min_array = [0] * n
        max_array[0] = A[0]
        min_array[0] = A[0]

        for i in range(1, n):
            max_array[i] = max(A[i], max_array[i - 1] + A[i])
            min_array[i] = min(A[i], min_array[i - 1] + A[i])

        if sum(A) == min(min_array):

            return max(max_array)
        else:
            return max(max(max_array), sum(A) - min(min_array))


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        result = -sys.maxsize
        A = A + A

        for i in range(2 * n):
            res = [0]
            res[0] = A[i]
            for j in range(i + 1, min(i + n + 1, n)):
                res.append(max(res[j - i - 1] + A[j], A[j]))
            if max(res) > result:
                result = max(res)

        return result
