# Read input
numbers = input().split()
numbers = [int(x) for x in numbers]

# Make a copy to find smallest and largest values
nums_copy = numbers[:]

# Find the 3 smallest values
smallest = []
for _ in range(3):
    min_val = nums_copy[0]
    for num in nums_copy:
        if num < min_val:
            min_val = num
    smallest.append(min_val)
    nums_copy.remove(min_val)

# Reset copy to find largest values
nums_copy = numbers[:]

# Find the 3 largest values
largest = []
for _ in range(3):
    max_val = nums_copy[0]
    for num in nums_copy:
        if num > max_val:
            max_val = num
    largest.append(max_val)
    nums_copy.remove(max_val)

# Now print numbers that are not in smallest or largest lists
# We need to remove each value only once for duplicates
remaining = numbers[:]
for val in smallest:
    remaining.remove(val)
for val in largest:
    remaining.remove(val)

# Print remaining numbers in original order
print(" ".join([str(x) for x in remaining]))
