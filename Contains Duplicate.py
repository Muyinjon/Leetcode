nums = [1,1,1,3,3,4,3,2,4,2]
rtype = False
numbercounter={}

for x in nums:
    if x in numbercounter:
        numbercounter[x]=+1
        rtype = True
    else:
        numbercounter[x]=1
print(rtype)

