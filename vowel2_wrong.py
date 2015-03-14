def anti_vowel(text):
    word = list(text)
    for letter in word:
        print letter
        if letter in "aeiouAEIOU":
                word.remove(letter)
    rem = ''.join(word)
    print rem

anti_vowel('Hey look Words!')