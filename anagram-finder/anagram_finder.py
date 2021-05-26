with open('anagram_finder/2of4brif.txt') as in_file:
    words = in_file.read().strip().split('\n')
    words = [word.lower() for word in words]

lookup_word = 'charming'

anagrams = [lookup_word]

for word in words:
    if word != lookup_word:
        # to find out if a word is an anagram of another, we can convert them into a list and sort the items in the list
        if sorted(word) == sorted(lookup_word):
            anagrams.append(word)

if len(anagrams) <= 1:
    print(f"'{lookup_word}' has no anagrams")
else:
    print(f"Anagrams: {anagrams}")
