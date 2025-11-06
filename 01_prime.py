# 1. Write an Algorithm and Python Program to Input a Number N.
# The Program then Displays whether the Number is Prime or Not Prime

N = int(input("Enter Number = "))

if N <= 1:
    print(N, "is not Prime")
else:
    for i in range(2, N):
        if N % i == 0:
            print(N, "is not Prime")
            break
    else:
        print(N, "is Prime")

