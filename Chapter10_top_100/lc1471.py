class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr_sorted = sorted(arr)
        if len(arr_sorted) % 2 == 1:
            mid = arr_sorted[len(arr) // 2]
        else:
            mid = (arr_sorted[len(arr) // 2] + arr_sorted[len(arr) // 2 - 1]) / 2

        res = []
        k_value = []
        for elem in arr_sorted:
            if len(res) < k:
                res.append(elem)
                k_value.append(abs(elem-mid))
            else:
                if abs(elem-mid) >= min(k_value):
                    res.pop(k_value.index(min(k_value)))
                    k_value.pop(k_value.index(min(k_value)))

        return res