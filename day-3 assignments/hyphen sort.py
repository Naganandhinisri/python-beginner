items = input("Input hypen separated sequence of words")
words = [word for word in items.split("-")]
print("-".join(sorted(list(set(words)))))