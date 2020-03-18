class Solution:
    def partition(self, s):
        if not s:
            return []
        res = []
        self._partition(s, [], res)
        return res

    def _partition(self, s, path, res):
        if self.checkParelle(s):
            res.append(path + [s])

        for i in range(1, len(s)):
            if self.checkParelle(s[:i]):
                self._partition(s[i:], path + [s[:i]], res)
            else:
                continue

    def checkParelle(self, s):
        if not s:
            return False
        return list(reversed(s)) == list(s)