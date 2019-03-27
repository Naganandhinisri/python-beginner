open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

def synthesis(word):
    stack = []
    for element in word:
        if element in open_list:
            stack.append(element)
        elif element in close_list:
            index_value = close_list.index(element)
            if ((len(stack)> 0) and (open_list[index_value] == stack[len(stack)-1])):
                stack.pop()
            else:
                return  'unbalanced'

    if len(stack)== 0:
        return  'balanced'
string = "[{}{})(]"
print(string,synthesis(string))