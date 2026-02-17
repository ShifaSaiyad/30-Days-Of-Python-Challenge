
print("-----Walrus Operator-----")
#1] example
'''if (data := input("enter name : "))  != "":
    print(data)
else:
    print("null")
    #2] example
if (lenth1 := len([1,2,3,4,5,6])) >3:
    print("big")
else:
    print("less")
     #3] example
a = 10
if (b := 10) != a:
    print("not")
else:
    print("yess")'''

print("-----Types Definations in python-----")

n : int = 2 #n.
print(n.is_integer) # after write (: int/ str) you can use all of the function in n. or name.
name : str = "shifa"    
print(name.isalnum)

#2]
def sum(a :int, b : int) -> int:
    return a + b
sum(4,5)


print("-----List, Tuple, Dict and Union in python for good data structure-----")
from typing import List, Tuple, Dict, Union

a_list : list[int,str] = [(1,"Shifa"),(2,"b1"),(3,"B3")]
b_tuple : tuple[int, str] = (4,"Shifa")
c_dict : dict[int,str] = {1 :"shifa", 2 : "boy1"} 
d_union : Union[str,int] = 40

print("Lists :\n")
print(a_list)
l = []
for item in a_list:
    l.append(item[0])
    print(l)
print("best way to define the list   :\n")
ints = [item[0] for item in a_list]
print(ints)

print("tuples :\n")
print(b_tuple, "\n")

print("dicts :\n")
print(c_dict)
print(c_dict.keys())    #print only keys like 1,2,3,...
for key in c_dict:
    print(key)
l = list(c_dict.keys()) #convert to list
print(l)

print("Union :\n")
print(d_union)


print("-----MACTH CASE-----")

def http_status(status):
    match status:
        case 200:
            return "Ohk"
        case 404:
            return "Not Found"
        case 500:
            return "internal server error"
        case _:
            return "unknow status"
print(http_status(404))


print("-----Dictionary merge and update operator-----")

'''d1 = {1 :"shifa", 2 : "boy1"}
d2 = {3 :"shifa1", 4 : "boy2"}
marge = d1 |d2
print(marge)

with (
    open("untitled3.txt") as b1,
    open("dunkey.txt") as b2
    ):
    5'''
    #write code for process file
    
print("-----Exception handling-----")

'''try:
    a = int(input("heelo, Enter the number : "))
    print(a)
except Exception as e:  #exception handel
    print(e)
except ValueError as v: #if the error is value error then it run this code
    print(v)
    print("valur Error")
print("Have a good Day")'''

'''print("-----Create Exception -----")
a = int(input("enter 1 number : "))
b = int(input("enter 2 number : "))
if b == 0:
    raise ZeroDivisionError("please enter currect  value 0 is not valid..")
else:
    print(f"the division of a and b is A / B = {a/b}")'''

print("-----Try with else and finally-----")

'''try:
    a = int(input("heelo, Enter the number : "))
    print(a)
except Exception as e:  
    print(e)
else:
    print("Have a good Day, read this line : ")
    print("if try is sucessfully execute then and then the code of else will be executed")

def main():
    try:
        a = int(input("Enter the number : "))
        print(a)
        return
    except Exception as e:  
        print(e)
        return
    
    finally:
        print("finally code is always executed with breack all the rules like : ' if uper function have the return it mean this function code is over , not print bellow lines'")
    print("this line not executed because of this not in finally")
main()'''

print("-----Globel and local veriable-----")

'''a = 5
def fun():
    global a
    a = 2
    print(a)
fun()
print(a)    #if you print a value before run the fun function it same as globel a = 5'''

print("-----Enumerate function in python -----")

l = [12,4,65,89]
l.sort()
index = 0
for item in l:
    print(f"The item number at index {index} is {item}")
    index += 1

print("This can be simplified using enumerate function")


for index, item in enumerate(l):
    print(f"the item number at index {index} is {item}")

print("-----List comprehension-----")

myList = [1, 2, 9, 5, 3, 5]
myList.sort()
# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

squaredList = [i*i for i in myList]

print(squaredList)

