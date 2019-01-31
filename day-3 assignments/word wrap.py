import textwrap

value = "ABCD."


wrapper = textwrap.TextWrapper(width=50)

string = wrapper.fill(text=value)

print(string)