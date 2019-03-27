def stringReplace(string):
    replaced_string = string.replace("%20", "===")
    return replaced_string


inputString = "we%20use%20%%20to%20find%20remainder"
print(stringReplace(inputString))
