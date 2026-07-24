# Two Sum
nums = [2, 7, 11, 15]
target = 18

seen={}

for i in range(len(nums)):
    num=nums[i]
    diff=target-num


    if diff in seen:
        print([seen[diff], i])
        break

    seen[num]=i










# num1 = nums[0]
# num2 =target - nums[0]
# two_sum = [num1, num2]
# print(two_sum)