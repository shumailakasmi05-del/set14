# Read input strings
parts = input().split()

# Perform stable sort based on reversed strings using bubble sort
for i in range(len(parts)):
    for j in range(i + 1, len(parts)):
        # Compare reversed strings
        a = ""
        b = ""
        # Reverse parts[i]
        for k in range(len(parts[i]) - 1, -1, -1):
            a += parts[i][k]
        # Reverse parts[j]
        for k in range(len(parts[j]) - 1, -1, -1):
            b += parts[j][k]
        if a > b:
            parts[i], parts[j] = parts[j], parts[i]

# Print the sorted strings
output = ""
