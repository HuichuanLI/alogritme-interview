class Node:
    def __init__(self):
        # is_word表示这个结点是否为一个单词的结尾
        # next[]表示这个结点的下一个26个字母结点
        self.is_word = False
        self.next = [None] * 26


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        now = self.root
        length = len(word)
        for i in range(length):
            pos = ord(word[i]) - ord('a')
            if now.next[pos] is None:
                now.next[pos] = Node()
            now = now.next[pos]
        now.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        now = self.root
        length = len(word)
        for i in range(length):
            pos = ord(word[i]) - ord('a')
            if now.next[pos] is None:
                return False
            now = now.next[pos]
        return now.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        now = self.root
        length = len(prefix)
        for i in range(length):
            pos = ord(prefix[i]) - ord('a')
            if now.next[pos] is None:
                return False
            now = now.next[pos]
        return True


Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False


class WordFilter:
    def __init__(self, words):
        self.trie = Trie()

        for weight, word in enumerate(words):
            cur = self.trie
            cur[WEIGHT] = weight
            for i, x in enumerate(word):
                # Put all prefixes and suffixes
                tmp = cur
                for letter in word[i:]:
                    tmp = tmp[letter, None]
                    tmp[WEIGHT] = weight

                tmp = cur
                for letter in word[:-i or None][::-1]:
                    tmp = tmp[None, letter]
                    tmp[WEIGHT] = weight

                # Advance letters
                cur = cur[x, word[~i]]
                cur[WEIGHT] = weight

    def search(self, prefix, suffix):
        cur = self.trie
        for a, b in map(None, prefix, suffix[::-1]):
            if (a, b) not in cur: return -1
            cur = cur[a, b]
        return cur[WEIGHT]
