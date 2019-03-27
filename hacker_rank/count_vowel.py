import re
vowels = "aeiou"
vowel_list = list(vowels)
word = "ninanjohne"
word_list = list(word)
count = 0
for element in range(0, len(vowels)):
    for elements in range(0, len(word)):
        if vowels[element] == word[elements]:
            count = count + 1
print(vowels)
print(count)
print(len(word)- count)
slicing = word[:: -1]
print(slicing)
filtered_string = re.sub('a|o|i|e|u','',word)
print(filtered_string)