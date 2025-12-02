## Problem: Fridge Cleanup

### Description
Write a program that reads a list of food items with the number of days each has been in the fridge and determines which items need to be thrown away. The fridge can hold at most 5 items, so only the 5 freshest items (those with the fewest days in the fridge) should be kept. All other items must be thrown away. Print the names of items to throw away in alphabetical order, or "None" if nothing needs to be thrown away.

### Input Format
First line: an integer n (number of food items)
Next n lines: each contains a food item name (string) and days in fridge (integer), separated by a space

### Output Format
Print the names of items to throw away in alphabetical order, separated by spaces, or "None" if no items need to be thrown away

### Examples

---
Input:
```
8
milk 3
bread 7
eggs 2
cheese 10
yogurt 1
butter 5
lettuce 8
tomato 4
```
Output:
```
bread cheese lettuce
```

---
Input:
```
5
apple 2
banana 5
orange 1
grape 3
pear 4
```
Output:
```
None
```

---
Input:
```
3
carrot 6
potato 2
onion 4
```
Output:
```
None
```

---
Input:
```
10
apple 1
banana 3
cherry 2
date 5
fig 4
grape 8
kiwi 6
lemon 9
mango 7
orange 10
```
Output:
```
grape kiwi lemon mango orange
```

---
Input:
```
7
salad 5
soup 3
pasta 5
rice 2
beans 3
corn 7
peas 5
```
Output:
```
corn salad
```
