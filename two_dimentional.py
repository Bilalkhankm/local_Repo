
rows = int(input("Enter number of rows (M): "))
cols = int(input("Enter number of columns (N): "))


matrix = []
print("\nEnter elements row by row:")
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Enter element ({i},{j}): "))
        row.append(val)
    matrix.append(row)


print("\nMatrix:")
for r in matrix:
    print(r)


print("\nSum of each row:")
for i in range(rows):
    row_sum = sum(matrix[i])
    print(f"Row {i+1} sum = {row_sum}")


print("\nSum of each column:")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Column {j+1} sum = {col_sum}")


first_row_product = 1
last_row_product = 1
for val in matrix[0]:
    first_row_product *= val
for val in matrix[-1]:
    last_row_product *= val

print("\nProduct of 1st row =", first_row_product)
print("Product of last row =", last_row_product)


first_col_product = 1
last_col_product = 1
for i in range(rows):
    first_col_product *= matrix[i][0]
    last_col_product *= matrix[i][-1]

print("Product of 1st column =", first_col_product)
print("Product of last column =", last_col_product)