# Two Sum
nums = [2, 7, 11, 15]
target = 13

seen={}

for i, num in enumerate(nums):
    diff = target - num


    if diff in seen:
        print([seen[diff], i])
        break

    seen[num]=i


