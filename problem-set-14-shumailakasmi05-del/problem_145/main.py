# Read number of entries
n = int(input())

# Initialize lists to store users and their first and last values
users = []        # to keep track of order of first appearance
first_values = [] # first value for each user
last_values = []  # last value for each user

# Process each log entry
for _ in range(n):
    entry = input().split()
    name = entry[0]
    value = int(entry[1])

    if name in users:
        # Update last value
        idx = 0
        # Find index of user
        for i in range(len(users)):
            if users[i] == name:
                idx = i
                break
        last_values[idx] = value
    else:
        # New user
        users.append(name)
        first_values.append(value)
        last_values.append(value)

# Print differences in order of first appearance
for i in range(len(users)):
    diff = last_values[i] - first_values[i]
    print(users[i], diff)
