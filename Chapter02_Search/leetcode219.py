class Solution:
    # 划动窗口
    def containsNearbyDuplicate(self, nums, k):
        record = set()
        for i in range(len(nums)):
            if nums[i] in record:
                return True
            record.add(nums[i])
            if len(record) == k + 1:
                record.remove(record[i - k])

        return False


