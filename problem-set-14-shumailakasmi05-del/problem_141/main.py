# Read number of lines
n = int(input())

# Read all lines as lists of integers
lines = []
for _ in range(n):
    parts = input().split()
    nums = []
    for p in parts:
        nums.append(int(p))
    lines.append(nums)

# Perform a stable sort based on the third integer using bubble sort
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        if lines[i][2] > lines[j][2]:
            lines[i], lines[j] = lines[j], lines[i]

# Print the sorted lines
for line in lines:
    output = ""
    for num in line:
        output += str(num) + " "
    print(output.strip())
