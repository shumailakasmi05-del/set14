# Read input and convert to integers
numbers = input().split()
nums = []
for n in numbers:
    nums.append(int(n))

# Sort the list manually using simple bubble sort
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

# Compute median
n = len(nums)
if n % 2 == 1:
    median = nums[n // 2]
else:
    median = (nums[n // 2 - 1] + nums[n // 2]) / 2

# Print median with 2 decimal places
print("{0:.2f}".format(median))
