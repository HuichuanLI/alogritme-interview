class Solution:
    def evalRPN(self, tokens):
        Operation = ['/', '+', '*', '-']
        stack = []
        for ele in tokens:
            if ele in Operation and len(stack) >= 2:
                nums1 = stack.pop()
                nums2 = stack.pop()
                res = self.result(nums1, nums2,ele)
                stack.append(res)
            elif isinstance(int(ele), int):
                stack.append(int(ele))
        res = stack.pop()
        return res

    def result(self, num1, num2, operation):
        Operation = ['/', '+', '*', '-']
        if operation == '+':
            return num2 + num1
        elif operation == '-':
            return num2 - num1
        elif operation == '/':
            return int(num2 / num1)
        elif operation == '*':
            return num2 * num1