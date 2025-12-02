## Problem: Sort by Third Column

### Description
Write a program that reads n lines, each containing 4 space-separated integers, and sorts the lines based on the third integer in each line. If two lines have the same third integer, maintain their original order.

### Input Format
First line: an integer n (number of lines)
Following n lines: each containing 4 space-separated integers

### Output Format
Print the n lines sorted by their third integer, maintaining the original format (4 space-separated integers per line)

### Examples

---
Input:
```
3
10 20 30 40
50 60 10 70
80 90 20 100
```
Output:
```
50 60 10 70
80 90 20 100
10 20 30 40
```

---
Input:
```
1
1 2 3 4
```
Output:
```
1 2 3 4
```

---
Input:
```
4
10 20 5 40
50 60 3 70
80 90 8 100
11 22 3 44
```
Output:
```
50 60 3 70
11 22 3 44
10 20 5 40
80 90 8 100
```

---
Input:
```
3
100 200 50 400
10 20 5 40
1 2 500 4
```
Output:
```
10 20 5 40
100 200 50 400
1 2 500 4
```

---
Input:
```
5
5 5 5 5
3 3 3 3
4 4 4 4
2 2 2 2
1 1 1 1
```
Output:
```
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
5 5 5 5
```
