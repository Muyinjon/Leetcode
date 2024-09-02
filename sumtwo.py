nums = [2,7,11,15,35]
target = 26
sumtwo = 0
i=0
pos=[]
for x in range(len(nums)):
    for num in range(x+1,len(nums)):
        if nums[x]+nums[num]==target and num is not x:
            pos=[x,num]
            break
    if pos:
        print(pos)
        