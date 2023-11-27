def two_positive(a, b, c):
    count_positive = 0
    # Count the number of positive numbers
    if a > 0:
        count_positive += 1
    if b > 0:
        count_positive += 1
    if c > 0:
        count_positive += 1
    
    # Return True if exactly two numbers are positive, False otherwise
    return count_positive == 2

a = 2
b = 4
c = -3

# Check if exactly two of three integers are positive
result = two_positive(a, b, c)
print(f"{result}")