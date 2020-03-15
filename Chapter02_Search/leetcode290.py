class Solution:
    # - 时间复杂度: O(N ^ 2) - 空间复杂度: O(N)

    def wordPattern(self, pattern, str):
        str_array = str.split(" ")
        if len(pattern) != len(str_array):
            return False

        dict1 = {}
        for p_ele, str_ele in zip(pattern, str_array):
            if not dict1.get(p_ele, None):
                if str_ele in dict1.values():
                    return False
                dict1[p_ele] = str_ele
            else:
                if dict1[p_ele] != str_ele:
                    return False
        return True

    # - 时间复杂度: O(N)- 空间复杂度: O(N)
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern = list(pattern)
        strList = str.split(' ')
        if len(pattern) != len(strList):
            return False
        tmp = len(set(zip(pattern, strList)))
        return tmp == len(set(pattern)) and tmp == len(set(strList))


if __name__ == "__main__":
    print(Solution().wordPattern("abba", "dog cat cat fish"))
