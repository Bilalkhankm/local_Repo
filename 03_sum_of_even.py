# 3. Write an Algorithm and Pyhton 
# Program to Input a Number N and Print Sum of Even Numbers up to that Number

N = int(input("Enter Number ="))

sum = 0

for i in range(1, N + 1):
   
    if(i % 2 == 0):
        sum = sum + i
        print(i)
print("Sum of even numbers up to", N, "=", sum)
       