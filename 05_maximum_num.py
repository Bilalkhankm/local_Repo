# 5. Write an Algorithm and Python. Program to Input four Numbers N1, N2, N3 and N4. 
# The Program then Displays the Maximum Number using Nested IF

N1 = int(input("Enter Number 1 ="))
N2 = int(input("Enter Number 2 ="))
N3 = int(input("Enter Number 3 ="))
N4 = int(input("Enter Number 4 ="))

if(N1 > N2):
    if(N1 > N3):
        if(N1 > N4):
            print(N1, "is the Maximum Number")
    else:
        if(N2 > N3):
            if(N2 > N4):
                print(N2, "is the Maximum Number")
        else:
            if(N3 > N4):
                print(N3, "is the Maximum number")
            else:
                print(N4, "is the Maximum Number")
