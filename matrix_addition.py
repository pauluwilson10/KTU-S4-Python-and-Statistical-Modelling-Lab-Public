
def input_matrix(rows,columns,matrix):

    print("Enter the element in matrix:")
    for i in range(rows):
        row = []
        for j in range(columns):
            element=int(input(f"Enter the element in position ({i},{j}): "))
            row.append(element)
        matrix.append(row)
    return matrix


def p_matrix(matrix):
    for row in matrix:
        print(row)


def matrix_add(matrix1,matrix2,result):
    if(len(matrix1)!=len(matrix2) or len(matrix1[0])!=len(matrix2[0])):
        print("Matrix addition NOT possible... ")
    else:
        for i in range(len(matrix1)):
            row = []
            for j in range((len(matrix1[0]))):
                row.append(matrix1[i][j]+matrix2[i][j])
            result.append(row)
    return result
print("Details of matrix-1")
rows1=int(input("Enter the rows in matrix 1: "))
columns1=int(input("Enter the columns in matrix 1: "))
matrix1=[]
matrix1=input_matrix(rows1,columns1,matrix1)
print("Elements in matrix  1 are:")
p_matrix(matrix1)

print("Details of matrix-2")
rows2=int(input("Enter the rows in matrix 2: "))
columns2=int(input("Enter the columns in matrix 2: "))
matrix2=[]
matrix2=input_matrix(rows2,columns2,matrix2)
print("Elements in matrix  2 are:")
p_matrix(matrix2)

print("Details of addition matrix :")
result=[]
result=matrix_add(matrix1,matrix2,result)
print("elements in resultant matrix")
p_matrix(result)




