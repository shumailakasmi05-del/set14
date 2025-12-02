## Problem: Task Priority Manager

### Description
Write a program that reads a series of task management commands and processes them. The program maintains a list of tasks, each with a name and priority value. When displaying tasks, they should be sorted by priority in descending order (highest priority first), and tasks with the same priority should be sorted alphabetically by name in ascending order.

### Input Format
First line: integer n (number of commands)
Next n lines: one command per line, in one of these formats:
- "ADD <task_name> <priority>" - adds a task with the given name and priority (integer)
- "REMOVE <task_name>" - removes the task with the given name
- "LIST" - outputs all current tasks in sorted order

### Output Format
For each LIST command, print all current tasks one per line in the format "<task_name> <priority>". Tasks should be sorted by priority in descending order, then alphabetically in ascending order for tasks with the same priority. If no tasks exist when LIST is called, print "EMPTY".

### Examples

---
Input:
```
5
ADD review_code 3
ADD write_tests 5
ADD fix_bug 5
ADD documentation 1
LIST
```
Output:
```
fix_bug 5
write_tests 5
review_code 3
documentation 1
```

---
Input:
```
7
ADD task_a 2
ADD task_b 3
ADD task_c 2
LIST
REMOVE task_b
ADD task_d 4
LIST
```
Output:
```
task_b 3
task_a 2
task_c 2
task_d 4
task_a 2
task_c 2
```

---
Input:
```
1
LIST
```
Output:
```
EMPTY
```

---
Input:
```
6
ADD alpha 10
ADD beta 10
ADD gamma 10
ADD delta 5
REMOVE beta
LIST
```
Output:
```
alpha 10
gamma 10
delta 5
```

---
Input:
```
8
ADD meeting 7
ADD email 3
LIST
REMOVE meeting
REMOVE email
LIST
ADD review 2
LIST
```
Output:
```
meeting 7
email 3
EMPTY
review 2
```
