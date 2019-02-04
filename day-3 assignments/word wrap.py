def wrap_word(word):
    for i in range(0, len(word)):
        word = word[1:] + word[0]
        print(word)



wrap_word("hello")
wrap_word("")
wrap_word(" ")
