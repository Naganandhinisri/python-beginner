# print("enter 'x' for exit")
string = input("enter the string")
character = input("enter the letter to be count from above string")
for character in string:
      value = string.count(character)
      print("{}:{}".format(character, value))