# Reverse list using 2 pointer

nums = [10, 20, 30, 40]

left = 0
right = len(nums) - 1

left=0
right=len(nums)-1

for num in nums:
    if left<right:
        nums[left],nums[right]=nums[right],nums[left]

        left+=1
        right-=1

print(nums)
#######################################################

while left < right:
    # Swap elements at left and right indices
    nums[left], nums[right] = nums[right], nums[left]
    
    # Move pointers toward the middle
    left += 1
    right -= 1

print(nums)  # Output: [40, 30, 20, 10]