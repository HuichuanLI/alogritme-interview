import re
class Solution:
    # - 时间复杂度: O(N)- 空间复杂度: O(N)
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiou'
        lst = list(s)
        l, r = 0, len(s) - 1
        while l <= r:
            if lst[l].lower() not in vowels:
                l += 1
            elif lst[r].lower() not in vowels:
                r -= 1
            else:
                lst[l], lst[r] = lst[r], lst[l]
                l += 1
                r -= 1
        return ''.join(lst)

    def reverseVowels2(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = re.findall(r'[aeiouAEIOU]', s)
        print(vowels)
        return re.sub('[aeiouAEIOU]', lambda m: vowels.pop(), s)


if __name__ == "__main__":
    print(Solution().reverseVowels2('abcde'))
