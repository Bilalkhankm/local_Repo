# 7. Write a Procedure Sub-Algorithm to Find and
# Display The Exponential Power of a Number N by the Power P

N = int(input("Enter number ="))
P = int(input("Enter power of number ="))

def power(N, P):

    result = 1
    i = 1
    while i <= P:
        result = result * N
        i = i + 1
    print("Exponential Power =", result)
    
power(N, P) 