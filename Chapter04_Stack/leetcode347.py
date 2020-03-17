from collections import Counter, defaultdict
import heapq


class Solution:
    # def topKFrequent(self, nums, k):
    #     return [ele[0] for ele in Counter(nums).most_common(k)]

    # 使用堆
    from collections import Counter, defaultdict
    import heapq

    class Solution:
        def topKFrequent(self, nums, k):
            counter = defaultdict(int)
            hep = []
            for ele in nums:
                counter[ele] += 1
            for elem, value in counter.items():
                if len(hep) < k:
                    heapq.heappush(hep, (value, elem))
                else:
                    temp = heapq.heappop(hep)
                    if temp[0] < value:
                        heapq.heappush(hep, (value, elem))
                    else:
                        heapq.heappush(hep, (temp[0], temp[1]))
            res = []
            while hep:
                ele = heapq.heappop(hep)
                res.append(ele[1])
            return reversed(res)


if __name__ == "__main__":
    print(list(Solution().topKFrequent([3, 0, 1, 0], 1)))
