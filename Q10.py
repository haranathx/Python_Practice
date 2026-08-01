# Question 1: Move Zeroes

nums = [0, 1, 0, 3, 12]

insert_pos = 0

for i in range(len(nums)):

    if nums[i] != 0:
        # Swap elements at left and right indices
        nums[insert_pos], nums[i] = nums[i], nums[insert_pos]

        # Move pointers toward the middle
        insert_pos += 1

print(nums)


# Alternatives
# ptr=0

# for i, num in enumerate(nums):
#     if nums[i]!=0:
#         nums[i],nums[ptr]=nums[ptr],nums[i]

#         ptr+=1

# print(nums)