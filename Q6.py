# Find the Minimum Element ⭐

nums = [12, 5, 8, 21, 17]

minimum_element = float("+inf")

for num in nums:
    if num < minimum_element:
        minimum_element=num


print(minimum_element)
