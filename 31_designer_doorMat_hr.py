# Enter your code here. Read input from STDIN. Print output to STDOUT

def game():
    a = input("Size: ").split()
    print(a)
    val1 = int(a[0])
    val2 = int(a[2])
    for i in range (val1):
        print(i)
    for j in range(val2):
           print(j, end = "")
            
        
    
    print( val1, val2)
game()