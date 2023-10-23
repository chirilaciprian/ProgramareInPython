#   1. Write a function to return a list of the first n numbers in the Fibonacci string.
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

print("\nEx 1")
print(fibonacci_sequence(20))


#  2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.\
from math import sqrt
def is_prime(n):
    if n > 1:
        for i in range(2, int(sqrt(n))+1):     
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False
def prime_numbers(l):
    l2 = []
    for n in l:
        if is_prime(n):
            l2.append(n)
    return l2
print("\nEx 2")
print(prime_numbers(list(range(1,50))))

# 3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)
def list_operations(a,b):
    intersection = list(set(a)&set(b))
    union = list(set(a) | set(b))
    difference_a = list(set(a) - set(b))
    difference_b = list(set(b) - set(a))
    return [intersection,union,difference_a,difference_b]
print("\nEx 3")
print(list_operations([1,2,3,4,5,6,7],[4,5,6,7,8,9,10]))

# 4. Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers)
# and a start position (integer). The function will return the song composed by going though the musical notes beginning
# with the start position and following the moves given as parameter.
def compose_song(notes, moves, start_position):
    song = []
    current_position = start_position
    song.append(notes[start_position])
    for move in moves:
        current_position = (current_position + move) % len(notes)
        song.append(notes[current_position])
    return song

print("\nEx 4")
print(compose_song(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

#   5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements
# under the main diagonal with 0 (zero).
def matrix_replace(m):
    row = len(m)
    col = len(m[0])
    for i in range(row):
        for j in range(col):
            if i>j:
                m[i][j]=0
    return m

print("\nEx 5")
matrix = matrix_replace([[1,2,3,4],[1,2,4,5],[3,5,2,6],[1,5,6,3]])
for c in matrix:
    print(c)



# 6. Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list containing the
# items that appear exactly x times in the incoming lists. 
def items_appearing_x_times(x,*lists):
    dictionary = {}
    
    for sublist in lists:
        for item in sublist:
            if item in dictionary:
                dictionary[item] += 1
            else:
                dictionary[item] = 1
    result = []
    for item,count in dictionary.items():
        if count == x:
            result.append(item)

    return result

list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6]
list4 = [4, 1, "test"]
print("\nEx 6")
print(items_appearing_x_times(2,list1, list2, list3, list4))

#  7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest palindrome number.
def is_palindrome(n):
    return str(n)==str(n)[::-1]
def find_palindromes(list):
    palindroms = []
    for item in list:
        if is_palindrome(item):
            palindroms.append(item)
    return (len(palindroms),max(palindroms))

print("\nEx 7")
print(find_palindromes([121, 1331, 456, 12321, 777, 88888, 12345]))

# 8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True.
# For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True,
# otherwise it should contain characters that have the ASCII code not divisible by x.
def generate_list_ascii(x=1,l=[],flag=True):
    result=[]
    for string in l:
        char_list=[]
        for ch in string:
            ascii_code = ord(ch)
            if (flag and ascii_code % x == 0) or (not flag and ascii_code % x != 0):
                char_list.append(ch)
        result.append(char_list)
    return result

print("\nEx 8")
print(generate_list_ascii(2, ["test", "hello", "lab002"], False))

#   9. Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium
#   and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game.
#   A spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are occupied.
#   All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest row from the field.

def spectators_cant_see(matrix):
    bad_seats=[]
    rows = len(matrix)
    columns = []
    for col in range(len(matrix[0])):
        column_elements = []
        for row in range(rows): 
            column_elements.append(matrix[row][col])
        columns.append(column_elements)
    for c in range(len(columns)):
        for r in range(1,len(columns[c])):
            max_val=max(columns[c][:r])
            if columns[c][r]<=max_val:
                bad_seats.append((r,c))
    return bad_seats
            
stadium = [[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 7, 2],
[5, 5, 2, 5, 6, 4],
[6, 6, 7, 6, 7, 5]] 
print("\nEx 9")
print(spectators_cant_see(stadium))

# 10. Write a function that receives a variable number of lists and returns a list of tuples as follows: 
#     the first tuple contains the first items in the lists, the second element contains the items on the 
#     position 2 in the lists, etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. 

def combine_lists(*lists):
    max_length = max(len(lst) for lst in lists)
    combined_tuples = [
        tuple(lst[i] if i < len(lst) else None for lst in lists)
        for i in range(max_length)
    ]
    return combined_tuples
    
print("\nEx 10")
print(combine_lists([1,2,3],[4,5,6],['a','b','c'],['f','f','f']))


# 11.Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.

def order_tuples_by_third_character(tuples):
    sorted_tuples = sorted(tuples, key=lambda item: item[1][2] if len(item[1]) >= 3 else '')
    return sorted_tuples

print("\nEx 11")
print(order_tuples_by_third_character([('abc', 'bcd'), ('abc', 'zza')]))


#  12. Write a function that will receive a list of words  as parameter and will return a list of lists of words, grouped by rhyme. 
#  Two words rhyme if both of them end with the same 2 letters.

def group_by_rhyme(words):
    rhymes = {}
    for word in words:
        rhyme = word[-2:]
        if rhyme not in rhymes:
            rhymes[rhyme] = []
        rhymes[rhyme].append(word)
    return list(rhymes.values())

print("\nEx 12")
print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))