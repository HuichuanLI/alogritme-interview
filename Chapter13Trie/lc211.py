class Node:
    def __init__(self):
        # is_word表示这个结点是否为一个单词的结尾
        # next[]表示这个结点的下一个26个字母结点
        self.is_word = False
        self.next = [None] * 26


class WordDictionary:

    def __init__(self):
        self.root = Node()

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """

    def addWord(self, word):
        now = self.root
        length = len(word)
        for i in range(length):
            pos = ord(word[i]) - ord('a')
            # 依次查找每个字符
            # 如果所有下一个结点中没有当前字符，则增加新结点到下一个next[pos]
            if now.next[pos] is None:
                now.next[pos] = Node()
            now = now.next[pos]
        now.is_word = True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """

    def search(self, word):
        n = len(word)
        return self.check(word, n, 0, self.root)

    def check(self, word, n, pos, now):
        if pos == n:
            # 已经判断到末尾都符合要求
            # 如果此时是一个单词，那么就找到了
            # 如果不是一个完整单词，说明不是
            return now.is_word
        if word[pos] == '.':
            # 若为通配符
            # 有任一种符合就返回true
            for i in range(26):
                # 如果有下一位对应字符结点，且找到了完整单词
                if now.next[i] != None and self.check(word, n, pos + 1, now.next[i]):
                    return True
        else:
            ch = ord(word[pos]) - ord('a')
            if now.next[ch] != None:
                # 如果有下一位对应字符结点，那么继续往下查找
                return self.check(word, n, pos + 1, now.next[ch])
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
