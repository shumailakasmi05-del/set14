# Read input
n = int(input())

# Initialize counter
count = 0

# Loop until n becomes 0
while n > 0:
    # If the least significant bit is 1, increment count
    if n % 2 == 1:
        count += 1
    # Shift right by 1 (integer division by 2)
    n = n // 2

# Print the result
print(count)
