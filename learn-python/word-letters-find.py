word1 = ' hai there and somebody Hari do the talking'
word2 = 'is with or Krishna and of'

firstNameStart = word1.find('H')
firstNameEnd = word1.find('i', firstNameStart)


secondNameStart = word2.find('K')
secondNameEnd = word2.find('a', secondNameStart)


name = word1[firstNameStart:firstNameEnd+1] + " " + word2[secondNameStart:secondNameEnd+1]

print (name)