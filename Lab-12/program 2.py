class Matrix:
    def __init__(self, elements):
        self.elements = elements

    def __add__(self, other):
        return Matrix([[self.elements[i][j] + other.elements[i][j] for j in range(3)] for i in range(3)])

    def __mul__(self, other):
        return Matrix([[sum(self.elements[i][k] * other.elements[k][j] for k in range(3)) for j in range(3)] for i in range(3)])

    def transpose(self):
        return Matrix([[self.elements[j][i] for j in range(3)] for i in range(3)])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.elements])


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)
print("Addition of Matrix 1 and Matrix 2:")
print(matrix1 + matrix2)
print("Multiplication of Matrix 1 and Matrix 2:")
print(matrix1 * matrix2)
print("Transpose of Matrix 1:")
print(matrix1.transpose())
print("Transpose of Matrix 2:")
print(matrix2.transpose())
