class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """

        res = []
        id1, id2 = 0, 0
        while id1 < m or id2 < n:
            if id1 >= m:
                res.append(B[id2])
                id2 += 1
            elif id2 >= n:
                res.append(A[id1])
                id1 += 1
            elif A[id1] < B[id2]:
                res.append(A[id1])
                id1 += 1
            else:
                res.append(B[id2])
                id2 += 1
        A[:] = res
