class Solution:
    def sumSubarrayMins(self, A) -> int:
        sum_value = []
        self.dfs(A, 0, [], sum_value)
        return sum(sum_value)

    def dfs(self, A, index, path, sum_value):
        if index >=len(A):
            return
        if len(path) > 0:
            sum_value.append(min(path))
            print(sum_value)
        for i in range(index+1, len(A)):
            self.dfs(A, i, path + [A[i]], sum_value)
        return


if __name__ == "__main__":
    print(Solution().sumSubarrayMins([3, 1, 2, 4]))
