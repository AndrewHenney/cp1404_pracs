out_file = open('name.txt', 'w')
name = input("what is your name: ")
print(name, file=out_file)
out_file.close()

in_file = open('name.txt', 'r')
name = in_file.read().strip()
print("Your name is:", name)



in_file = open('numbers.txt', 'r')
total_sum = 0
for line in in_file:
    number = int(line)
    total_sum += number

print(total_sum)
in_file.close()
