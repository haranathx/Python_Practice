# Reverse a List Without Using reverse() or [::-1]

nums = [10, 20, 30, 40]
new_list = []

for num in nums:
    new_list = [num] + new_list

print(new_list)




# new_list + [num]	Appended to the end	Original order
# [num] + new_list	Prepended to the front	Reversed order


# def reverse_iterative(nums):
#     new_num = []
#     for num in nums:
#         new_num.insert(0, num)
#     return new_num

# nums = [10, 20, 30, 40]
# print(reverse_iterative(nums))


# nums = [1, 2, 3, 4, 5, 5, 6, 9, 8, 7, 8, 5, 22, 4]

# # Using list comprehension to reverse the list
# reversed_list = [nums[num] for num in range(len(nums) - 1, -1, -1)]
# print(reversed_list)

