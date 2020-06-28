class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        x = [0 for _ in range(k)]  # 按余数分类统计个数
        for i in arr:
            x[i % k] += 1
        if x[0] % 2 != 0:  # 两数均能被k整除这种情况容易忽略
            return False
        i = 1
        j = k - 1
        while i <= j:
            if i == j:
                if x[i] % 2 == 0:  # 还有就是如果k为偶数，那么余数为k//2的数组的值一定要是偶数，只能在当前数组里配对
                    return True
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True
