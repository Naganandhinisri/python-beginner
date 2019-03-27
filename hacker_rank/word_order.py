user_word = input("enter the words")
words = user_word.split(" ")
list_words = list(words)
print(list_words)
unique_words = []
for i in range(0, len(list_words)):
    if list_words[i] in unique_words:
        continue
    else:
        unique_words.append(list_words[i])

print(len(unique_words))
for ele in range(0, len(unique_words)):
    count = 0
    for element in range(0,len(list_words)):
        if unique_words[ele] == list_words[element]:
            count = count + 1

    print(count)


