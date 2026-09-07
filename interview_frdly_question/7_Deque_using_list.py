#pop with O(1)
from collections import deque

queue = deque()

queue.append("Ravi")
queue.append("Priya")
queue.append("You")
queue.append("Karan")

print(queue)
queue.popleft() #O(1)
print(queue)

print(queue[0])
print(len(queue))
print(len(queue) == 0)