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