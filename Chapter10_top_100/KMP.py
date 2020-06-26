class Kmp:
    def __init__(self, string, pattern):
        self.next = [0] * len(pattern)
        self.next[0] = -1
        j = 1
        k = 0
        while j < len(pattern):
            if k == 0 or string[j] == string[k]:
                j += 1
                k += 1
                self.next[j] = k
            else:
                k = self.next[k]
        print(self.kmp(string, pattern))

    def kmp(self, string, pattern):
        i = 0
        j = 0
        while i < len(string) and j < len(pattern):
            if j == -1:
                i += 1
                j = 0
            elif string[i] == pattern[j]:
                i += 1
                j += 1
            else:
                j = self.next[j]

        if j < len(pattern):
            return -1
        else:
            return i - j


if __name__ == "__main__":
    a = "abdc"
    b = "c"
    Kmp(a, b)
