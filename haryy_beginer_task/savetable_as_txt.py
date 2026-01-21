n = int(input("enter number :"))

data = [i*n for i in range(1,11)]

with open("C:/Users/SHIFA SAIYED/OneDrive/Documents/Python _Journey/30-Days-Of-Python-Challenge17_01_2026/haryy_beginer_task/tables.txt", "a") as f:
    f.write(f"the table of {n} is {str(data)}\n")
print(data)

