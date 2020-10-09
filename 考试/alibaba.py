import sys


class Solution:
    def restoreIpAddresses(self, s: str):
        size = len(s)
        cnt = s.count('0')
        path = []
        res = []
        self.__dfs(s, size, 0, 0, path, res, cnt)
        return res

    def __dfs(self, s, size, split_times, begin, path, res, cnt):
        if begin == size:
            if split_times == cnt:
                res.append('.'.join(path))
            return

        if size - begin < (cnt - split_times):
            return

        for i in range(size - begin + 1):
            if begin + i >= size:
                break
            if s[begin:begin + i].count('0') > 1:
                break

            ip_segment = self.__judge_if_ip_segment(s, begin, begin + i)

            if ip_segment != -1:
                path.append(str(ip_segment))
                self.__dfs(s, size, split_times + 1, begin + i + 1, path, res, cnt)
                path.pop()

    def __judge_if_ip_segment(self, s, left, right):

        res = s[left:right + 1]

        if res.count('0') > 1 or res.count('0') == 0:
            return - 1
        return res


n = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

print(len(Solution().restoreIpAddresses(s)))
