strs = ["eat","tea","tan","ate","nat","bat"]
"""[["bat"],["nat","tan"],["ate","eat","tea"]]"""
#for x in range(len(nums)): //code for checking it
    # for num in range(x+1,len(nums)):

countdic={}


for word in strs:
    print(word)
    for letter in word:
        if letter in countdic[str(word)]:
            countdic[word][letter]+=1
        else:
            countdic[word][letter]=0
        print(countdic)
    print(countdic)
            
            


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
"""    sdict={}
tdict={}
for letter in s:
    if letter in sdict:
        sdict[letter]+=1
    else:
        sdict.update({letter:0})
for letter in t:
    if letter in tdict:
        tdict[letter]+=1
    else:
        tdict.update({letter:0})
print(sdict==tdict)"""