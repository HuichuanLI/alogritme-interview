class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrty = -1
        for i in range(n):
            flag = True
            for j in range(n):
                if i == j:
                    continue
                if not knows(j, i) or knows(i, j):
                    flag = False
                    break
            if flag:
                return i
        return celebrty


class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        for i in range(1, n):  # 他不认识后面的人
            if knows(celebrity, i):
                celebrity = i  # 可能的名人

        for i in range(celebrity):  # 他不认识前面的人
            if knows(celebrity, i):
                return -1

        for i in range(n):  # 检查是否 都认识他
            if not knows(i, celebrity):
                return -1

        return celebrity
