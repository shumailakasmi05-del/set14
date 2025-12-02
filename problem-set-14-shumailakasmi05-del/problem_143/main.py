# Read input
parts = input().split()

# Convert to integers
numbers = []
for p in parts:
    numbers.append(int(p))

# Separate evens and odds
evens = []
odds = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

# Sort evens (ascending) using bubble sort
for i in range(len(evens)):
    for j in range(i + 1, len(evens)):
        if evens[i] > evens[j]:
            evens[i], evens[j] = evens[j], evens[i]

# Sort odds (ascending) using bubble sort
for i in range(len(odds)):
    for j in range(i + 1, len(odds)):
        if odds[i] > odds[j]:
            odds[i], odds[j] = odds[j], odds[i]

# Combine results
result = []
for num in evens:
    result.append(num)
for num in odds:
    result.append(num)

# Print output
output = ""
for num in result:
    output += str(num) + " "
print(output.strip())
