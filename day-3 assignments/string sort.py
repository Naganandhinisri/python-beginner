my_str = input("Enter a string: ")
words = my_str
words = my_str.split()

words.sort()

for word in words:
    if my_str != words:
        print("TRUE")
    else:
        print("FALSE")
print(word)