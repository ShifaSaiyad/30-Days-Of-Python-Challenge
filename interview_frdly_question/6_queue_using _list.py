#pop with O(n)
queue = []

queue.append("Ravi")
queue.append("Priya")
queue.append("You")
queue.append("Karan")

print(queue)
queue.pop(0)   #O(n)
print(queue)

print(queue[0])
print(len(queue))
print(len(queue) == 0)

"""
for interview:- 
-dequeue front/back - both

- collections.deque -  import for queue and use this

-list.pop(0) bcs this follow - O(n) (dont use this)

-for priority queue import heap and use it 
"""
