nums = [10, 20, 30, 40]

left = 0
right = len(nums) - 1

while left < right:
    # Swap elements at left and right indices
    nums[left], nums[right] = nums[right], nums[left]
    
    # Move pointers toward the middle
    left += 1
    right -= 1

print(nums)  # Output: [40, 30, 20, 10]