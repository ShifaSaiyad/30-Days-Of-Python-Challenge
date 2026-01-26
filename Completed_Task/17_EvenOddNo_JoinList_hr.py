# Enter your code here. Read input from STDIN. Print output to STDOUT

n  = int(input())
for i in range(0,n):
    string = input()
    a = list(string)
    l =[]
    l2 =[]
    for i in range(len(a)):
        if i%2 == 0:
            l.append(a[i])
        else:
            l2.append(a[i])
        
    a1 = "".join(l)
    b = "".join(l2)
    print(a1,b)