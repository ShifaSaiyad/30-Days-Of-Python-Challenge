if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    #print(student_marks)

    query_name = input("")

    i = 0
    total = 0
    for keys in student_marks:
        if query_name == keys:
            l = student_marks[query_name]
            for s in l:
                total += s
                a = total/(len(l))
                
            print(f"{a:.2f}")
            #print("{:.2f}".format(a))

            
