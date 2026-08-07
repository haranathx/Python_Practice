# Maximum Sum Subarray of Size K

# Find the maximum sum of any 3 consecutive elements.


nums = [2, 1, 5]
k = 5


def max_sub_array_of_size_k(k, nums):

    if k <= 0 or k > len(nums):
        return 0

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


print(max_sub_array_of_size_k(k, nums))


# nums = [2, 1, 5, 1, 3, 2]
# k = 5

# # def max_sub_array_of_size_k(k: int, nums: list[int]) -> int:
# def max_sub_array_of_size_k(k, nums):

#     if k <= 0 or k > len(nums):
#         return 0


#     window_sum = sum(nums[:k])
#     max_sum=window_sum


#     ## Slide the window across the array
#     # for i in range(len(nums) - k):
#     #     # Subtract element leaving the window, add element entering it
#     #     window_sum = window_sum - nums[i] + nums[i + k]
#     #     max_sum = max(max_sum, window_sum)

#     for i in range(k, len(nums)):
#         window_sum = window_sum - nums[i - k] + nums[i]
#         max_sum = max(max_sum, window_sum)

#     return max_sum


# print(max_sub_array_of_size_k(k, nums))
