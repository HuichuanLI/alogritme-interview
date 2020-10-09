class Solution:

    def strStr(self, source, target):
        Hash_Base, Hash_Size = 31, 2 ** 20

        if source is None or target is None: return -1
        m, n = len(source), len(target)
        if n == 0: return 0
        if m < n: return -1
        target_hash = 0
        running_hash = 0
        top_power = 1
        for _ in range(len(target) - 1):
            top_power = (top_power * Hash_Base) % Hash_Size

        for index in range(len(target)):
            target_hash = (target_hash * Hash_Base + ord(target[index])) % Hash_Size
            running_hash = (running_hash * Hash_Base + ord(source[index])) % Hash_Size
        if running_hash == target_hash:
            if source[:n] == target:
                return 0
        for end in range(n, m):
            i = end - n
            running_hash = (running_hash - top_power * ord(source[i])) % Hash_Size
            running_hash = (running_hash * Hash_Base + ord(source[end])) % Hash_Size
            if running_hash == target_hash and target == source[i + 1:end + 1]:
                return i + 1
        return -1
