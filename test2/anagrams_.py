def anagram():
    word = "programmer"
    new_word = "pronrammer"
    sorted_word = sorted(word)
    print(sorted_word)
    sorted_new_word = sorted(new_word)
    print(sorted_new_word)
    if sorted_new_word == sorted_word:
        return ('TRUE')
    else:
        return ('FALSE')


print(anagram())
