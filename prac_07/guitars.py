from prac_07.guitar import Guitar

guitars=[]
print("My guitars!")
name = 'a'
guitars.append(Guitar(input('Name: '), input('Year: '), input('Cost: ')))
name = guitars.name
while name != '':
    # year = input('Year: ')
    # cost = input('Cost: ')
    guitars.append(Guitar(input('Name: '), input('Year: '), input('Cost: ')))
    # print("{} ({}) : ${:,.2f} added.".format(name, year, int(cost)))
    name = guitars.name
    # name = input('Name: ')

# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
print(guitars)
i=0
for i, guitar in enumerate(guitars):
    if guitar.is_vintage() :
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1,
    guitar.name, guitar.year, guitar.cost, vintage_string))