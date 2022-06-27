sentence = "My name is Hari Krishna. I am a Software biiiigwoooord Engineer with PHP as main skill but learning python"

wordsarray = sentence.split(' ')

length = 0

for word in wordsarray:
    if len(word) > length:
        length = len(word)
        longword = word

print(longword)