class Codec:
    # @param {string[]} strs a list of strings
    # @return {string} encodes a list of strings to a single string
    def encode(self, strs):
        # Write your code here
        return ''.join(['%d$' % len(elem) for elem in strs])

    # @param {string} s a string
    # @return {string[]} decodes a single string to a list of strings
    def decode(self, s):
        # Write your code here
        strs = []
        i, n = 0, len(strs)
        while i < len(s):
            j = s.find('$', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j + 1: i])
        return strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
