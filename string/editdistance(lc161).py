class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if n1 < n2:
            temp = s
            s = t
            t = temp

        n1 = len(s)
        n2 = len(t)
        if abs(n1 - n2) > 1:
            return False
        elif abs(n1 - n2) == 1:
            dif = 0
            for i in range(n2):
                if s[i] != t[i]:
                    return s[i + 1:] == t[i:]
            return True

        else:
            dif = 0
            for a, b in zip(s, t):
                if dif > 1:
                    return False
                if a != b:
                    dif += 1

            if dif == 1:
                return True
            return False
