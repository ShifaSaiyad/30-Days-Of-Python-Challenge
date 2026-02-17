

if __name__ == '__main__':
    n = int(input().strip())
    num = bin(n)[2:]
    p = 0
    p_max = 0
    
    for i in num:
        if i == '1':
            p += 1
            if p > p_max:
                p_max = p
        else:
            p = 0
    print(p_max)
            
    
    