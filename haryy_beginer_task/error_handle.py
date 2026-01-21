try:
    a = int(input("num1 : "))
    b = int(input("num2 : "))
    print(a / b)
        
except ZeroDivisionError as e:
    print("infanite.. please change the value of b it's 0. not divide by any number")
