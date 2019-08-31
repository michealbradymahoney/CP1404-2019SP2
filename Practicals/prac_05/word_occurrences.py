words_dict = {}
user_input = input("Text: ")
words = user_input.split()
for string in words:
    occurrences = words_dict.get(string, 0)
    words_dict[string] = occurrences + 1

words = list(words_dict.keys())
words.sort()

max_length = max((len(string) for string in words))
for string in words:
    print("{:{}} : {}".format(string, max_length, words_dict[string]))
