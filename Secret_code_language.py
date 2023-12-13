# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end 
# else:
#     simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now remove the last letter

#  In following program I have applied a little different approach from the question given, to encode or decode the message 

import random
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '1', '2', '3', '4', '5', '6','7','8','9','0']

def rand():
    return int(random.random() *100 % len(characters))

st = input("Enter your message : ")
words = st.split(" ")
coding = input("1 for coding or 0 for decoding : ")
coding = True if(coding == '1') else False

if(coding):
    nwords = []
    for word in words:
        if(len(word) >= 3):

            r1 = characters[rand()] + characters[rand()] + characters[rand()]
            r2 = characters[rand()] + characters[rand()] + characters[rand()]
            stnew = r1 + word[1:] + word[0] + r2 
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if(len(word) >= 3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))