strs = ["eat","tea","tan","ate","nat","bat"]
"""[["bat"],["nat","tan"],["ate","eat","tea"]]"""

countdic={}
for word in strs:
    
    sortword = ''.join(sorted(word))
    
    if sortword in countdic:
        countdic[sortword].append(word)
    else:
        countdic[sortword] = [word]
output = list(countdic.values())
