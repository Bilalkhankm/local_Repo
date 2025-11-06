# 9. A cash drawer contains 160 bills, all 10s and 50s. 
# If the total value of the 10s and 50s is $1,760. 
# How many of each type of bill are in the drawer?

total_bills = 160

total_value = 1760


ten_bills = (50 * total_bills - total_value) / 40

fifty_bills = total_bills - ten_bills

print("The total 10s bills is =", ten_bills)
print("The total 50s bills is =", fifty_bills)