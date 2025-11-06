# 2. Write an Algorithm and Python
# Program to Input a Number N and Print Odd Numbers up to that Number

N = int(input("Enter Number ="))

for i in range(1, N + 1):
   
    if(i % 2 != 0):
        print(i)
        