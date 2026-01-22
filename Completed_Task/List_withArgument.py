if __name__ == '__main__':
    N = int(input())
    
    l = []
    a = 1
    b=1
   
        
    for i in range(N):
        a = input("")
        parts = a.split()

        if parts[0] == "insert":
            index = int(parts[1])
            value = int(parts[2])
            l.insert(index,value)

        if parts[0] == "remove":
            value = int(parts[1])
            if value in l:
                l.remove(value)

        if parts[0] == "append":
            value = int(parts[1])
            l.append(value)

        if parts[0] == "print":
            print(l) 

        if parts[0] == "sort":
            l.sort()

        if parts[0] == "pop":
            l.pop()

        if parts[0] == "reverse":
            l.reverse()
        

    
        


        
