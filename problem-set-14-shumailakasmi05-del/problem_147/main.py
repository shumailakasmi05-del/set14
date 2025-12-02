# Read number of food items
n = int(input())

# Read all food items into a list of tuples: (name, days)
foods = []
for _ in range(n):
    line = input().split()
    name = line[0]
    days = int(line[1])
    foods.append((name, days))

# Sort foods by number of days in fridge (ascending)
for i in range(len(foods)):
    for j in range(i + 1, len(foods)):
        if foods[i][1] > foods[j][1]:
            foods[i], foods[j] = foods[j], foods[i]

# Keep at most 5 freshest items
keep = foods[:5]

# Items to throw away
throw_away = foods[5:]

# If nothing to throw away, print "None"
if len(throw_away) == 0:
    print("None")
else:
    # Collect names and sort alphabetically
    names = []
    for item in throw_away:
        names.append(item[0])

    # Simple bubble sort for names
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if names[i] > names[j]:
                names[i], names[j] = names[j], names[i]

    # Print names separated by spac
