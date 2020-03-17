# coding:gbk
import heapq

tasks = []
heapq.heappush(tasks, (10, 'aaa'))
heapq.heappush(tasks, (40, 'bbb'))
heapq.heappush(tasks, (30, 'ccc'))
heapq.heappush(tasks, (20, 'ddd'))

while tasks:
    task = heapq.heappop(tasks)
    print(task)



from queue import Queue, PriorityQueue


# 定义一个可比较对象
class CompareAble:
    def __init__(self, priority, jobname):
        self.priority = priority
        self.jobname = jobname

    def __lt__(self, other):
        if self.priority < other.priority:
            return 1
        else:
            return 0

# 最小堆
pq = PriorityQueue()
pq.put(CompareAble(80, 'eat'))
pq.put(CompareAble(70, 'a write plan2'))
pq.put(CompareAble(70, 'write plan'))
pq.put(CompareAble(90, 'sleep'))
pq.put(CompareAble(100, 'write code'))
while pq.qsize() != 0:
    task = pq.get_nowait()
    print(task.jobname, task.priority)
