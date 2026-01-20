if __name__ == '__main__':
    main = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        main.append([name, score])
        
    lowest_first = min(s[1] for s in main)
    
    for s in main:
        if s[1] == lowest_first:
            main.remove(s)
    #print(main)
    
    l =[]
    second_lowest = min(s[1] for s in main)
    for s in main:
        if s[1] == second_lowest:
            l.append(s[0])
    l.sort()
    for a in l:
        print(a)