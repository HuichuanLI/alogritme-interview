from collections import OrderedDict


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return
        LOOKUP = OrderedDict()

        LOOKUP[1000] = 'M'
        LOOKUP[900] = 'CM'
        LOOKUP[500] = 'D'
        LOOKUP[400] = 'CD'
        LOOKUP[100] = 'C'
        LOOKUP[90] = 'XC'
        LOOKUP[50] = 'L'
        LOOKUP[40] = 'XL'
        LOOKUP[10] = 'X'
        LOOKUP[9] = 'IX'
        LOOKUP[5] = 'V'
        LOOKUP[4] = 'IV'
        LOOKUP[1] = 'I'

        result = ''

        while num > 0:
            for key, value in LOOKUP.items():
                if num - key >= 0:
                    result += value
                    num -= key
                    break

        return result
