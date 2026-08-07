# Product of Array Except Self
nums = [1, 2, 3, 4]

result = [1] * len(nums)
print(result)
# Prefix products
prefix = 1

for i in range(len(nums)):
    result[i] = prefix
    prefix *= nums[i]

# Suffix products
suffix = 1

for i in range(len(nums) - 1, -1, -1):
    result[i] *= suffix
    suffix *= nums[i]

print(result)















# for num in nums:
#     if num==nums[0]:
#         print(nums[0], nums[1]*nums[2]*nums[3])
#     elif num==nums[1]:
#         print(nums[1], nums[0]*nums[2]*nums[3])
#     elif num==nums[2]:
#         print(nums[2], nums[1]*nums[0]*nums[3])
#     elif num==nums[3]:
#         print(nums[3], nums[1]*nums[2]*nums[0])