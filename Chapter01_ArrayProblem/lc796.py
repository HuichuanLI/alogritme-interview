class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return True
        for index, a in enumerate(A):
            if a != B[0]:
                continue
            else:
                if A[index:] + A[:index] == B:
                    return True
        return False
