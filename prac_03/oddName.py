name = input("What is your name: ")
length = len(name)
while length<1:
    print('that is not a valid name')
    name = input("What is your name: ")
    length=len(name)
counter = 1

for char in name :
    if counter % 2:
        print(char)

    counter += 1