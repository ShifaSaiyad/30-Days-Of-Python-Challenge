#2]
'''name = input("enter the name : ")
marks = float(input("Enter your Score : "))
mob_no = int(input("mobile number"))
a = "a name of the student is {}. marks of a student is {} and the mobile number is {}".format(name, marks,mob_no)
print(a)'''



#3]
l = [7*i for i in range(1,11)]

a1 = "\n".join(map(str,l))
print(a1)

#4]
l = [1,45,12,65,7,50,59,85,56,52,12,65,10,19,54,89]
def table(n):
    if n%5 == 0 :
        return True
    return False
final = filter(table,l)
print(list(final))

from functools import reduce
#5]
def greter(a,b):
    if a < b:
        return b
    return a

max1 = reduce(greter,l) 
print(max1)  

