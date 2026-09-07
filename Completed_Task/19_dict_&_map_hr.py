# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phonebook = {}



for _ in range(n):
    #a = input().split()
    name, mnum = input().split()
    phonebook[name] = mnum
    
while True:
    try:
        query = input()
        if query in phonebook:
            print(f"{query}={phonebook[query]}")
        else:
            print("Not found")
    except Exception :
        #print()
        break