class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        for i in range(n):
            if knows(celebrity, i):
                celebrity = i

        for i in range(celebrity):
            if knows(celebrity, i):
                return -1
        for i in range(n):
            if i != celebrity and not knows(i, celebrity):
                return -1
        return celebrity
