from random import shuffle


def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)


words = ['hello', 'carrots', 'habbit']
anagram = []

# normal
for word in words:
    anagram.append(jumble(word))
print (anagram)

# map
print (list(map(jumble, words)))

# comprehension method
print ([jumble(word) for word in words])
