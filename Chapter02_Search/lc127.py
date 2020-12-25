from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(wordList) == 0:
            return 0
        if beginWord == endWord:
            return 0
        if endWord not in wordList:
            return 0
        queue = deque([beginWord])
        visited = defaultdict(bool)
        visited[beginWord] = True
        res = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                cur_string = queue.popleft()
                for elem in wordList:
                    if not visited[elem] and self.difference(cur_string, elem):
                        if elem == endWord:
                            return res + 1
                        queue.append(elem)
                        visited[elem] = True
            res += 1
        return 0

    def difference(self, a, b):
        if abs(len(a) - len(b)) >= 2:
            return False
        res = 0
        for elem_a, elm_b in zip(a, b):
            if elem_a != elm_b:
                res += 1
            if res > 1:
                return False
        return res == 1
