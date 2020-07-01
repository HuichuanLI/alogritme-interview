class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        res_A = [0] * (len(A) + 1)
        reversed_B = list(reversed(B))
        res_A[0] = 0
        res_max = 0
        for elem in range(len(A)):
            if A[elem] in B:
                temp = elem
                index_B = len(B) - reversed_B.index(A[elem]) - 1

                while index_B >= 0 and temp >= 0 and B[index_B] == A[temp]:
                    index_B -= 1
                    temp -= 1
                res_A[elem] = elem - temp

            res_max = max(res_max, res_A[elem])

        return res_max
