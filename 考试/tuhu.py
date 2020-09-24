class Solution:
    def search_max_continue_sub(self, input_list):
        # write code here
        if not input_list:
            return 0
        input_list.sort()
        result = dp = 0
        pre = input_list[0] - 1
        for i in range(0, len(input_list)):
            if input_list[i] - pre == 1:
                dp += 1
            elif input_list[i] - pre > 1:
                dp = 1
            result = max(result, dp)
            pre = input_list[i]
        return max(result, dp)
