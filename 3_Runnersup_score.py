if __name__ == '__main__':
    n = 0
    n = int(input("enter the total n  : "))
    arr = map(int, input(f"enter the  value :").split())
    
    a = list(arr)
    maximum = max(a)
    #print(a)
    a.remove(maximum)
    while (maximum in a):
        a.remove(maximum)
    new1_max = max(a)
    print(a) 
    print(new1_max)
    #print("second maximum number is ", b)