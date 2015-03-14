alf = 'aeiouAEIOU'
text = 'Hey look Words!'
def anti_vowel(text):
    new = ''
    for c in range(len(text)):
        print text[c]
        if text[c] not in alf:
            new = new + text[c]
    return new
print anti_vowel(text)