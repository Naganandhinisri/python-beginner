def check_for_order(word):
    sorted_letters = sorted(word)
    alphabetized_word = ''.join(sorted_letters)
    if alphabetized_word == word:
        print(True)
    else:
        print(False)


check_for_order("ACER")
check_for_order("ADCB")
check_for_order("")
