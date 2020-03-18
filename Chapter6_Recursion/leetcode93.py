class Solution:
    def restoreIpAddresses(self, s):
        res = []
        if len(s)< 4 or len(s) > 12:
            return []
        for i in range(1, len(s) - 2):
            for j in range(i+1, len(s) - 1):
                for k in range(j+1, len(s)):
                    temp = s[0:i] + "." + s[i:j] + "." + s[j:k] + "." + s[k:]
                    if self.checkIp(temp):
                        res.append(temp)
        return res

    def checkIp(self, string):
        arr = string.split(".")
        for ele in arr:
            if ele.startswith("0") and (int(ele) != 0  or len(ele) !=1) :
                return False
            if int(ele) > 255:
                return False
        return True