nums = [1,1,1,2,2,3]
k = 2

nums = sorted(nums)
ranking = {}
for i in range(len(nums)):
    if nums[i] in ranking:
        ranking[nums[i]]+=1
    else:
        ranking[nums[i]]=1

ranking