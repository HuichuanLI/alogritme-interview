class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def cal(nums, exp, pre, ans):
            n = len(nums)
            if n == 0 and ans == target:
                res.append(exp)
            else:
                for i in range(1, n + 1):
                    if i > 1 and nums[0] == '0':
                        break
                    num = int(nums[:i])
                    if exp == '':
                        cal(nums[i:], nums[:i], num, num)
                    else:
                        cal(nums[i:], exp + '+' + nums[:i], num, ans + num)
                        cal(nums[i:], exp + '-' + nums[:i], -num, ans - num)
                        cal(nums[i:], exp + '*' + nums[:i], pre * num, ans - pre + pre * num)

        res = []
        cal(num, '', 0, 0)
        return res
