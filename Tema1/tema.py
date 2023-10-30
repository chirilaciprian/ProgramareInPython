# ex 0
def suma_n_nr(n):
    nr=list(range(1,n+1))
    return sum(nr)
print("\n\n Exercitiul 0")
print(suma_n_nr(4))

# ex 1
def generate_ascii(start,nr):
    s = ' '.join([hex(ord(start) + i)[2:] for i in range(nr)])
    return s

print("\n\n Exercitiul 1")
print(generate_ascii('0',32))

# ex 2
def secventa_8biti(l):
    secventa=list()
    nr_0 = 0
    nr_1 = 0
    for nr in l:
        binary = format(nr,'08b')
        secventa.append(binary)
        nr_0+=str(binary).count('0')
        nr_1+=str(binary).count('1')
    return secventa,nr_0,nr_1
print("\n\n Exercitiul 2")
print(secventa_8biti([0,1,2,3,4]))

# ex 3
from decimal import Decimal,getcontext
def impartire_cu_virgula(n1,n2):
    getcontext().prec = 100
    res = Decimal(n1)/Decimal(n2)
    return res
print("\n\n Exercitiul 3")
print(impartire_cu_virgula(10,3))

# ex 4
def equation(coefficients, constants):
    n = len(constants)
    augmented_matrix = [coeff + [constants[i]] for i, coeff in enumerate(coefficients)]
    for col in range(n):
        max_row = max(range(col, n), key=lambda i: abs(augmented_matrix[i][col]))
        augmented_matrix[col], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[col]
        pivot = augmented_matrix[col][col]
        for j in range(col, n + 1):
            augmented_matrix[col][j] /= pivot
        for i in range(n):
            if i != col:
                factor = augmented_matrix[i][col]
                for j in range(col, n + 1):
                    augmented_matrix[i][j] -= factor * augmented_matrix[col][j]
    solutions = [augmented_matrix[i][-1] for i in range(n)]
    return solutions
print("\n\n Exercitiul 4")
print(equation([[2,1],[1,1]],[5,3]))

# ex 5
def nth_root(n, x):
    if x == 0:
        return 0.0 
    guess = 1.0 
    for _ in range(50):
        previous_guess = guess
        guess = ((n - 1) * previous_guess + x / previous_guess ** (n - 1)) / n
        if abs(guess - previous_guess) < 1e-50:
            break
    return float(guess)
print("\n\n Exercitiul 5")
print(nth_root(3,27))

# ex 6
def generate_permutations(n,p,a):
    if n>= pow(len(a),p):
        return "N este mai mare decat nr de permutari posibile"
    permutations = list()
    for i in range(n,n+p):
        current_i = i
        current_permutation = list()
        for j in range(p):
            current_i,remainder = divmod(current_i,len(a))
            current_permutation.append(a[remainder])
        permutations.append(''.join(reversed(current_permutation)))
    return permutations
print("\n\n Exercitiul 6")
print(generate_permutations(1,3,"abc"))

# ex 7
def hex_to_binary(hex_str):
    return str(format(int(hex_str),'08b'))
hex_representation = [
    [0x00, 0x00, 0xFC, 0x66, 0x66, 0x66, 0x7C, 0x60, 0x60, 0x60, 0x60, 0xF0, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7E, 0x06, 0x0C, 0xF8, 0x00],
    [0x00, 0x00, 0x10, 0x30, 0x30, 0xFC, 0x30, 0x30, 0x30, 0x30, 0x36, 0x1C, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0xE0, 0x60, 0x60, 0x6C, 0x76, 0x66, 0x66, 0x66, 0x66, 0xE6, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x7C, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7C, 0x00, 0x00, 0x00, 0x00],
    [ 0x00, 0x00, 0x00, 0x00, 0x00, 0xDC, 0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0x00, 0x00, 0x00, 0x00]
]
def generate_matrix(hex_str):
    binary_matrix = []
    for row in hex_str:
        bin_matrix_tmp = list()
        for el in row:
            binary_number = hex_to_binary(el)
            row = ''.join(binary_number.split())
            bin_matrix_tmp.append(row)
        binary_matrix.append(bin_matrix_tmp)
    return binary_matrix
print("\n\n Exercitiul 7")
matrix = generate_matrix(hex_representation)
for row in matrix:
    for el in row:
        print(el)
    print("\n")



# ex 8
def calculate_area(y_values):
    n = len(y_values)
    width = 1.0
    total_area = 0.0
    for i in range(n - 1):
        height = y_values[i] - y_values[i + 1]
        trapezoid_area = (y_values[i] + y_values[i + 1]) * width / 2
        total_area += trapezoid_area
    return total_area
print("\n\n Exercitiul 8")
print(calculate_area([6,6,6,6,7,8,9,9,9,8,12,14,13,9,8,8,8,4,3,3,3]))