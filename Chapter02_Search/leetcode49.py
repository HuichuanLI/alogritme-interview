from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)
        for elem in strs:
            result[tuple(sorted(elem))].append(elem)
        return list(result.values())

        # noinspection PyUnreachableCode
        def groupAnagrams1(self, strs):
            mapx = {}
            for i in strs:
                tmp = ''.join(sorted(list(i)))
                if tmp in mapx:
                    mapx[tmp].append(i)
                else:
                    mapx[tmp] = [i]
            return list(mapx.values())


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
