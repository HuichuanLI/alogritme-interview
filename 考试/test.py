import heapq

a = [2, 4, 1, 3, 6]
res = [-1]
heap = [a[0]]
# for i in range(1, len(a)):
#     if a[i] >= heapq.nlargest(1, heap)[0]:
#         res.append(a[i-1])
#     else:
#         temp = heapq.nlargest(i, heap)
#         for elem in temp:
#             if a[i] > elem:
#                 res.append(elem)
#                 break
#     heapq.heappush(heap, a[i])

# print(res)

stack = [a[0]]
for i in range(1, len(a)):
    if a[i] >= stack[-1]:
        res.append(stack[-1])
        stack.append(a[i])
    else:
        while stack and stack[-1] > a[i]:
            stack.pop()
        if not stack:
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(a[i])

print(res)
