import sys
def line_count(string):
    lines = string.split("\n")
    return len(lines)

def word_count(string):
    replaced_string = string.replace("\n", " ")
    words = replaced_string.split(" ")
    filtered_words = filter(None, words)
    number_of_words = len(list(filtered_words))
    return number_of_words


def byte_count(string):
    number_of_bytes = len(string)
    return number_of_bytes


if __name__ == "__main__":
    options = []
    files = []
    for ele in sys.argv[1:]:
        if ele.startswith('-'):
            options.append(ele)
        else:
            files.append(ele)


    for file_name in files:
        with open(file_name, "r") as f:
            s = f.read()

            if '-l' in options:
                print(str(line_count(s)) + " -l  " + file_name)
            if '-w' in options:
                print(str(word_count(s))+" -w  " + file_name)
            if '-c' in options:
                print(str(byte_count(s))+" -c  " + file_name)

            if len(options) == 0 :
                print(str(line_count(s)) + " " + str(word_count(s)) + " " + str(byte_count(s)) + " " + file_name)
                # total = [x+y+z for x, y, z  in zip(line_count(s), word_count(s), byte_count(s))]
                # print(total)


