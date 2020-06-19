class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        waiting = defaultdict(list)

        for w in words:
            waiting[w[0]].append(iter(w[1:]))  # 存储以w[0]开头的前缀，此时waiting = {'a': [[], ['c', 'd'], ['c', 'e']], 'b': [['b']]}
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)  # 在本题的例子中 it 分别为[]、['c', 'd']、['c', 'e']
        return len(waiting[None])
