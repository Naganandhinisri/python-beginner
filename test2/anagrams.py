word = "astronomer"
sub_word = "moonarter"
new_word = sub_word.replace(' ', '')


for letter in new_word:
    if letter in word:
        new_word = new_word.replace(letter, '')
    else:
        print('FALSE')


if len(new_word) == 0:
    print('TRUE')


