class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dict = {}
        dict['0'] = '0'
        dict['8'] = '8'
        dict['6'] = '9'

        dict['9'] = '6'
        dict['1'] = '1'
        for j in range(len(num)):
            i = len(num) - j - 1
            if num[j] not in dict or dict[num[j]] != num[i]:
                return False

        return True
