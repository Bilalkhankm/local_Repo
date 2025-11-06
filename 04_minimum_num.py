# 4. Write an Algorithm and Python. Program to Input three Numbers N1, N2 and N3.
# The Program then Displays the Minimum Number using Nested IF

N1 = int(input("Enter Number 1 ="))
N2 = int(input("Enter Number 2 ="))
N3 = int(input("Enter Number 3 ="))

if(N1 < N2):
    if(N1 < N3):
        print(N1, "is the minimum number")
    else:
        print(N3, "is the minimum number")
else:
    if(N2 < N3):
        print(N2, "is the minimum number")
    else:
        print(N3, "is the minimum number")