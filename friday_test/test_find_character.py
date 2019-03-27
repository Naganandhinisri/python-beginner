import collections
def strings():
    input_string = 'A,b,c,a,b,b,d,c'
    formatted_string = input_string.casefold()
    corrected_string = formatted_string.split(',')
    count = collections.defaultdict(int)
    for letter in corrected_string:
        count[letter] += 1

    for letter in sorted(count):
        if count[letter] == 2:
            print('%s %d' % (letter, count[letter]))

strings()

#
# charss = 'a,b,c,a,b,b,d,c'
#
# for char in charss:
#   count = charss.count(char)
#   if count == 2:
#     print (char, count)

# from collections import Counter
# input_string = 'A,b,c,a,b,b,d,c'
# n = 2
# formatted_string = input_string.casefold()
# corrected_string = formatted_string.split(',')
# counted_string = Counter(corrected_string)
# # print(counted_string.values())
# if (counted_string.values()) == 2:
#     print(counted_string.keys())










