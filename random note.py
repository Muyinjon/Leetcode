
ransomNote = "fihjjjjei"
magazine = "hjibagacbhadfaefdjaeaebgi"
rtype = False
notecount={}
for letter in magazine:
    if letter in notecount:
        notecount[letter]+=1
    else:
        notecount.update({str(letter):1})
for letter in ransomNote:
    if letter not in notecount or notecount[letter] <= 0:
        rtype=False
        break
    elif letter in notecount:
        notecount[letter]-=1
        rtype=True

    else:
        rtype=False
