class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        record = set()
        for i in range(nums):
            for ele in range(nums[i] - t, nums[i] + t + 1):
                if ele in record:
                    return True
            record.add(nums[i])
            if len(record) == k + 1:
                record.remove(nums[i - k])
        return False
