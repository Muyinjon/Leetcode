s ="aaa"
t ="aa"
sdict={}
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
print(sdict==tdict)