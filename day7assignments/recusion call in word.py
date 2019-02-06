def explode(word):
    if len(word) <= 1:
        return word
    else :
        return( word[0]) + ' ' + explode(word[2:])

# word = 'hello'
print(explode('hello'))