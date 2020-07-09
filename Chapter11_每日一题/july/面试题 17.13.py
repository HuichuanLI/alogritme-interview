class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dictionary = set(dictionary)
        lens = list({len(w) for w in dictionary})
        lens.sort(reverse=True)
        print(lens)
        N, res, i = len(sentence), 0, 0

        @functools.lru_cache(maxsize=1000)
        def sol(i):
            if i >= N: return 0
            tails = []
            tails = [sol(i + l) for l in lens if i + l <= N and sentence[i:i + l] in dictionary]
            tails += [1 + sol(i + 1)]
            return (min(tails) if tails else 0)

        return sol(0)
