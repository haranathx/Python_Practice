# Check if an Element Exists

nums = [12, 5, 8, 21, 17]
target = 21

for i in nums:
    if i==target:
        print("Found")
        break

else:
    print("Not Found")

################################################
for num in nums:
    if target==num:
        print(True)
        break

else:
    print(False)

