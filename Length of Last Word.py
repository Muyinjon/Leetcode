s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
"""
Better method was this one
s=s.strip() --> removes all leading and trailing spaces
s=s.split() --> splits the string into list of words
print(len(s[-1]))--> gives the length of last word

"""

s = s[::-1] #reversing the string
count = 0 #initializing count to 0

for letter in s: 
    if letter.isalpha(): #checking if the letter is a letter
        count+=1 #incrementing count


    else: #if the letter is not a letter
        if count==0: 
            pass
        else:
            break
        

print(count)