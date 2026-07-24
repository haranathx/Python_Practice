# Find the Largest Element
# nums = [12, 5, 8, 21, 17]

nums = [45, 18, 90, 67, 12]

largest = nums[0]

for num in nums:
    if num>largest:
        largest=num

print(largest)