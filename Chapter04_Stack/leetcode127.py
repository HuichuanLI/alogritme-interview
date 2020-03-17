class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        visited = set()
        cur = set()
        cur.add(beginWord)
        # 单词长度
        word_n = len(beginWord)
        res = 1
        # BFS
        while cur:
            next_time = set()
            if endWord in cur:
                return res
            for tmp in cur:
                if tmp in wordList:
                    wordList.remove(tmp)
                for i in range(word_n):
                    for a in range(97, 123):
                        w = tmp[:i] + chr(a) + tmp[i+1:]
                        if w in wordList:
                            next_time.add(w)
            res += 1
            cur = next_time
        return 0