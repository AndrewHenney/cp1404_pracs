
def main():
    name = get_name()
    frequency = 2
    name_print(name,frequency)


def name_print(name,frequency):
    count=1
    for char in name:
        if count % frequency == False :
            print(char)
        count += 1




def get_name():
    name = input("What is your name: ")
    length = len(name)
    while length < 1:
        name = input("What is your name: ")
        length = len(name)
    return name

main()
