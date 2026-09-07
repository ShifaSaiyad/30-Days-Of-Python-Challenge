class stack:

    def __init__(self):
        self.items = [] #initial list

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def dispaly(self):
        print("stack top > Bottom : ", self.items[::-1])
s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print("our stack is : ")
s.dispaly()

#pop
s.pop()
print("after Pop : ")
s.dispaly()

size = s.size()
print("Size of stack : ",size)

#top item of the stack
peek = s.peek()
print("top item of the stack : ",peek)





