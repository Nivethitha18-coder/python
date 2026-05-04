r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

# Check multiplication condition
if c1 != r2:
    print("Matrix multiplication not possible")
else:
    # Input first matrix
    print("Enter elements of first matrix:")
    A = []
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input()))
        A.append(row)

    # Input second matrix
    print("Enter elements of second matrix:")
    B = []
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input()))
        B.append(row)

    # Result matrix
    result = [[0 for j in range(c2)] for i in range(r1)]

    # Matrix multiplication
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    # Display result
    print("Resultant Matrix:")
    for row in result:
        print(row)
