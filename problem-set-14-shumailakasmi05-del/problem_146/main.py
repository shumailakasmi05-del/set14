# Read number of commands
n = int(input())

# List to store tasks as [task_name, priority]
tasks = []

for _ in range(n):
    command = input().split()
    cmd_type = command[0]

    if cmd_type == "ADD":
        name = command[1]
        priority = int(command[2])
        tasks.append([name, priority])

    elif cmd_type == "REMOVE":
        name = command[1]
        # Remove task with this name
        idx = -1
        for i in range(len(tasks)):
            if tasks[i][0] == name:
                idx = i
                break
        if idx != -1:
            tasks.pop(idx)

    elif cmd_type == "LIST":
        if len(tasks) == 0:
            print("EMPTY")
        else:
            # Sort by priority descending, then name ascending
            for i in range(len(tasks)):
                for j in range(i + 1, len(tasks)):
                    if tasks[i][1] < tasks[j][1]:
                        tasks[i], tasks[j] = tasks[j], tasks[i]
                    elif tasks[i][1] == tasks[j][1]:
                        if tasks[i][0] > tasks[j][0]:
                            tasks[i], tasks[j] = tasks[j], tasks[i]
            # Print tasks
            for t in tasks:
                print(t[0], t[1])
