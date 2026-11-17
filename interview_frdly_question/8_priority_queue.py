import heapq

hopspital = []

#heapq.heappush(queue,item)
heapq.heappush(hopspital,(3,"Brocken Finger"))
heapq.heappush(hopspital,(1,"heart Attack"))
heapq.heappush(hopspital,(2,"HIgh fever"))

print("Before pop : ", hopspital)
#lower number  = Highest priority

print(heapq.heappop(hopspital))
print(heapq.heappop(hopspital))
print(heapq.heappop(hopspital))


"""
for interview:- 
-dequeue front/back - both

- collections.deque -  import for queue and use this

-list.pop(0) bcs this follow - O(n) (dont use this)

-for priority queue import heap and use it 
"""


