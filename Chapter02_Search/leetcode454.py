from collections import defaultdict,Counter


class Solution:
    # 空间O(n^2) 时间O(N^2)
    def fourSumCount(self, A, B, C, D):
        record = defaultdict(int)
        for i in range(len(C)):
            for j in range(len(D)):
                record[C[i] + D[j]] += 1

        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if -A[i] - B[i] in record.keys():
                    res += record[-A[i] - B[i]]

        return res

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        lookup = Counter(a + b for a in A for b in B)
        return sum(lookup[-c - d] for c in C for d in D)
