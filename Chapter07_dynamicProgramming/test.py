#
#
# @param N int整型
# @param trust int整型二维数组
# @return int整型
#
class Solution:
    def Find_Police(self, N, trust):
        # write code here
        if N == 0:
            return -1
        if len(trust) == 0:
            return -1
        police = 1
        for i in range(1, N + 1):
            if [police, i] in trust:
                police = i

        for i in range(1, N + 1):
            if i != police and [police, i]  in trust:
                return -1
        for i in range(1, N + 1):
            if i != police and [i, police] not in trust:
                return -1
        return police


if __name__ == "__main__":
    print(Solution().Find_Police(2, [[1, 2]]))
