class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        res = []
        self._permute(nums, [], res)
        return res

    def _permute(self, nums, path, res):
        if len(nums) == 1:
            res.append(path + [nums[0]])
            return

        for elem in nums:
            temps = nums.copy()
            temps.remove(elem)
            self._permute(temps, path + [elem], res)
        return


class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        res = []
        self._permute(nums, [], [False for _ in range(len(nums))], res)
        return res

    def _permute(self, nums, path, visited, res):
        if sum(nums) == len(nums):
            res.append(path)
            return

        for index, elem in enumerate(nums):
            if not visited[index]:
                visited[index] = True
                self._permute(nums, path + [elem],visited ,res)
                visited[index] = False

        return
