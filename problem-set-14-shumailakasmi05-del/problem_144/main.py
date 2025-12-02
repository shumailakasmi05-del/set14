# Read input
parts = input().split()

# Convert to integers
numbers = []
for p in parts:
    numbers.append(int(p))

# Bubble sort by squared values, then by original value
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        # Compare squared values
        if numbers[i] ** 2 > numbers[j] ** 2:
            numbers[i], numbers[j] = numbers[j], numbers[i]
        # If squared values are equal, compare original values
        elif numbers[i] ** 2 == numbers[j] ** 2 and numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

# Print result
output = ""
for num in numbers:
    output += str(num) + " "
print(output.strip())
