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
