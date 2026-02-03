class Difference:
    def __init__(self, a):
        self.__elements = a
        self.elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        min_val = min(self.elements)
        max_val = max(self.elements)
        self.maximumDifference = max_val - min_val

	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)