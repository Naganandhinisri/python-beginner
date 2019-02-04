character = input("enter your character")
value = character.replace(" ", "")
for i in value:
  print(chr(ord(i) + 3))
