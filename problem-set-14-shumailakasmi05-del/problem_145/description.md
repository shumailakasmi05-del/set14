## Problem: User Activity Difference

### Description
Write a program that reads user activity logs and calculates the difference between each user's last and first activity values. Each activity log entry contains a username and an integer value. For each user, compute the difference (last value - first value) and print the results in the order users first appeared.

### Input Format
First line: an integer n (number of activity log entries)
Next n lines: each contains a username (string) and an integer value, separated by a space

### Output Format
Print each username followed by the difference (last value - first value), one per line, in the order users first appeared

### Examples

---
Input:
```
9
alice 10
bob 5
charlie 15
alice 25
bob 20
charlie 35
alice 40
bob 25
charlie 45
```
Output:
```
alice 30
bob 20
charlie 30
```

---
Input:
```
6
david 100
eve 50
frank 200
david 120
eve 80
frank 180
```
Output:
```
david 20
eve 30
frank -20
```

---
Input:
```
8
grace 90
henry 40
ida 60
jack 100
grace 70
henry 50
ida 40
jack 80
```
Output:
```
grace -20
henry 10
ida -20
jack -20
```

---
Input:
```
9
joe 5
mary 2
harold 10
joe 9
joe 3
mary 12
mary 23
joe 99
harold 6
```
Output:
```
joe 94
mary 21
harold -4
```

---
Input:
```
10
kelly 20
leo 15
mike 30
kelly 25
leo 10
mike 35
kelly 30
leo 5
mike 50
leo 20
```
Output:
```
kelly 10
leo 5
mike 20
```
