print("if  answer like this '<map object at 0x000002251D02C430>' use list function outside it")


print("----Lamda Function-----")

#squre of x
squre = lambda x: x*x
print(squre(4))

#sum of a,b and
sum1 = lambda a,b,c: a+b+c
print(sum1(4,3,2))

print("----Join (is used for convert to string from list)-----")

a = ["shifa", "kazi", "hello"]
final1 = ":".join(a)
final2 = "-".join(a)

print(final1)
print(final2)

print("----format (used for asign value in {})-----")

a = "{} is a good {}".format("shifa", "girl")
a1 = "{1} is a good {0}".format("shifa", "girl")
print(a)
print(a1) 


print("----Map - filter  and Reduse-----")

print("Map")
l = [1,2,3,4,5,6]

squre = lambda X: X*X
print("Map(Function_name, List_name)")
sqrlist = map(squre,l)
print(list(sqrlist))

print("Filter")
def odd(n):
    if(n%2 != 0):
        return True
    return False
new = filter(odd,l)
print(list(new))

from functools import reduce
print("Reduse") 
def sum(a,b):   #sum 
    return a+b
reduce1 = reduce(sum, l)
print(reduce1)

multi = lambda a,b : a*b    #multiplication
mult =reduce(multi,l)
print(mult)