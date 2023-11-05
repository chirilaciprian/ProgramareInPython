# Write a Python class that simulates a Stack. The class should implement methods like push, pop, peek 
# (the last two methods should return None if no element is present in the stack).
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()
    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

s = Stack()
s.push(10)
s.push(20)
s.push(3)
print("Stack:")
print(s.pop())
print(s.peek())
 
# Write a Python class that simulates a Queue. The class should implement methods like push, pop, peek 
# (the last two methods should return None if no element is present in the queue).

class Queue:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)
    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[0]
    
q = Queue()
q.push(10)
q.push(20)
q.push(13)
print("Queue:")
print(q.pop())
print(q.peek())

# Write a Python class that simulates a matrix of size NxM, with N and M provided at initialization. 
# The class should provide methods to access elements (get and set methods) and some methematical functions
# such as transpose, matrix multiplication and a method that allows iterating through all elements form a matrix
# an apply a transformation over them (via a lambda function).

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0 for i in range(m)] for j in range(n)]
    def get(self, i, j):
        return self.matrix[i][j]
    def set(self, i, j, value):
        self.matrix[i][j] = value
    def transpose(self):
        transposed = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def multiply(self, other):
        if self.m != other.n:
            raise ValueError("Matrix dimensions are incompatible for multiplication")
        
        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                dot_product = sum(self.get(i, k) * other.get(k, j) for k in range(self.m))
                result.set(i, j, dot_product)
        return result

    def apply_transform(self, transform_function):
        for i in range(self.n):
            for j in range(self.m):
                self.set(i, j, transform_function(self.get(i, j)))

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])
    
matrix1 = Matrix(3, 3)
matrix1.set(0, 0, 1)
matrix1.set(0, 1, 2)
matrix1.set(0, 2, 3)
matrix1.set(1, 0, 4)
matrix1.set(1, 1, 5)
matrix1.set(1, 2, 6)
matrix1.set(2, 0, 7)
matrix1.set(2, 1, 8)
matrix1.set(2, 2, 9)

matrix2 = Matrix(3, 3)
matrix2.set(0, 0, 9)
matrix2.set(0, 1, 8)
matrix2.set(0, 2, 7)
matrix2.set(1, 0, 6)
matrix2.set(1, 1, 5)
matrix2.set(1, 2, 4)
matrix2.set(2, 0, 3)
matrix2.set(2, 1, 2)
matrix2.set(2, 2, 1)

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

transposed_matrix1 = matrix1.transpose()
print("Transposed Matrix 1:")
print(transposed_matrix1)

product_matrix = matrix1.multiply(matrix2)
print("Matrix 1 * Matrix 2:")
print(product_matrix)

matrix2.apply_transform(lambda x: x * 2)
print("Transformed Matrix 2:")
print(matrix2)
