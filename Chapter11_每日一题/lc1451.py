from collections import defaultdict


class Solution:
    def arrangeWords(self, text: str) -> str:
        count = defaultdict(list)
        for elem in text.split():
            count[len(elem)].append(elem)
        res = []
        for elem in sorted(count.keys(), reverse=False):
            for items in count[elem]:
                res.append(items.lower())
        return " ".join(res).capitalize()
