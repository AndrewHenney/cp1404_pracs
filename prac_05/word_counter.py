
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

for word in key_list:
    print('{} : {}'.format(word, word_count[word]))
