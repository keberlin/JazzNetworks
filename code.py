#
#  Straightforward generator to produce Fibonacci numbers using the following rule:
#  f(0) = 1
#  f(1) = 1
#  f(n) = f(n-1) + f(n-2) where n>=2
#
def fibonacci():
    a = 0
    b = 1
    while True:
        yield b
        a, b = (
            b,
            a + b,
        )  # Use Python's clever way of swapping variables without the use of a temporary swap variable


#
# Print out the first 100 Fibonacci even numbers along with their sum
#
numbers = []
for i, v in enumerate(fibonacci()):
    if v % 2 == 0:
        numbers.append(v)
    if len(numbers) == 100:
        break
print("The 1st 100 even Fibonacci numbers:", numbers)
print("Sum of those numbers:", sum(numbers))


#
# Function to return the overlapping set of values from 2 different lists
#
def intersection(list1, list2):
    # Ensure both parameters are lists
    assert isinstance(list1, list) and isinstance(list2, list)
    return sorted(list(set(list1) & set(list2)))  # Python's internal 'set' type performs this logic out of the box


#
# Define 2 different lists of numbers and print out the overlapping (intersection) of these without duplicates
#
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [4, 6, 8, 10, 12, 14, 4, 6, 8, 10, 12, 14]
result = intersection(list1, list2)
print("The list of overlapping numbers are:", result)
print("Testing intersection function..")
assert result == [4, 6, 8, 10]

#
# Function to determine if decimal number has only even digits
#
def number_has_even_digits(n):
    # Ensure n is a positive integer number
    assert n >= 0 and isinstance(n, int)
    s = str(n)
    for c in s:
        if (ord(c) - ord("0")) % 2 == 0:
            continue
        return False
    return True


#
# Test number_has_even_digits function using different test cases
#
print("Testing number_has_even_digits function..")
n = 2468
assert number_has_even_digits(n)  # Test positive case
n = 12345
assert not number_has_even_digits(n)  # Test negative case


#
# Function to compute a number equal to X+XX+XXX+XXXX where X is in the range 0-9
#
def expand_x(x):
    # Ensure X is between 0 and 9
    assert 0 <= x <= 9
    total = 0
    # Setup a range equal to the number of elements in the sequence from 4 descending to 1
    for i in range(4, 0, -1):
        # Calculate the factor of 10 depending on its shift position
        mult = 10 ** (4 - i)
        # And add 'i' multiples of X to the running total
        total += i * x * mult
    return total


#
# Test the expand_x function using a selection of input digits
#
print("Testing expand_x function..")
assert expand_x(0) == 0
assert expand_x(1) == 1234
assert expand_x(2) == 2468
assert expand_x(3) == 3702
assert expand_x(9) == 11106
