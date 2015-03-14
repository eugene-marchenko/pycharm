alfab = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz!? []'
text = 'Hey look Words!'
def anti_vowel(text):
    new = ''
    vowel = ''
    for i in text:
        #print i
        for j in alfab:
            #print j
            if i == j:
                #print j
                vowel = vowel + j
                #print vowel
                #return False
    return vowel
    #print vowel

print anti_vowel(text)