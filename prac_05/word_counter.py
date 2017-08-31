
input_string = input("Text: ")
word_list = input_string.split()
word_count = {}
for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
key_list = list(word_count.keys())
key_list.sort()
max_length = 0
for word in key_list:
    if max_length < len(word):
        max_length = len(word)
for word in key_list:
    print('{:{}} : {}'.format(word, max_length, word_count[word]))
