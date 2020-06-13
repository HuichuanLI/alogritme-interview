class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        s = 0
        l =  0
        # print([arr[i] + arr[i + 1] for i in range(len(arr)) if not i & 1])
        ans = []
        for r in range(len(arr)):
            s += arr[r]
            while s > target:
                s -= arr[l]
                l += 1
            if s == target:
                ans.append((l,r,r-l+1))
                # if l<=r:
                # else:
                # l = r = r+1
        # print(ans)
        ans.sort(key=lambda o:o[2])
        if len(ans) < 2:
            return -1
        else:
            t = ans[0]
            for i in range(1,len(ans)):
                if ans[i][0]>t[1] or ans[i][1]<t[0]:
                    return ans[i][2]+t[2]
            return -1