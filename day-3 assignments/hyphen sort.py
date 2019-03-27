items = input("Input hypen separated sequence of words")
words = [word for word in items.split("-")]
print(words)
print("-".join(sorted(list(set(words)))))