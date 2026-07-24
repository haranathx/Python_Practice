# Count Even Numbers
# nums = [1, 2, 4, 7, 9, 10, 14]
nums = [1, 2, 4, 7, 9, 10, 14]

even_nums=0

for num in nums:
    if (num%2 == 0):
        # even_nums=even_nums+1
        even_nums+=1

print(even_nums)