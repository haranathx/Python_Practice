# Find the Second Largest Element
# nums = [45, 18, 90, 67, 12]

nums = [45, 18, 90, 67, 12]

largest = float("-inf")
second_largest = float("-inf")

for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(largest)
print(second_largest)
