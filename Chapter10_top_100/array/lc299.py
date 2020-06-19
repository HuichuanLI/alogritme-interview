from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull_visited = [0 for i in range(10)]
        cows = 0
        cows_visited = [0 for i in range(10)]
        for elema, elemb in zip(secret, guess):
            if elema == elemb:
                bull_visited[int(elema)] += 1
        secret_count = Counter(secret)
        for elem in guess:
            if elem in secret and cows_visited[int(elem)] < secret_count[elem]:
                cows_visited[int(elem)] += 1
        for elma, elmb in zip(bull_visited, cows_visited):
            if elmb - elma > 0:
                cows += elmb - elma
        return str(sum(bull_visited)) + "A" + str(cows) + "B"


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 极简算法
        A = sum(s == g for s, g in zip(secret, guess))
        B = sum((Counter(secret) & Counter(guess)).values()) - A
        return "{A}A{B}B".format(A=A, B=B)
