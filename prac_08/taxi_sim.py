from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
 SilverServiceTaxi("Hummer", 200, 4)]

print("Let's drive")
print('q)uit, c)hoose taxi, d)rive')

taxi_choice = int(0)
bill = 0
menu_input = ''
while menu_input != 'q':
    menu_input = input('>>>')
    if menu_input=='c':
        print('Taxis available: ')
        for i, objects in enumerate(taxis):
            print('{} - {}'.format(i,objects))
        taxi_choice = int(input('Choose taxi:'))
        print('Bill to Date: ${:.2f}'.format(bill))
        print('q)uit, c)hoose taxi, d)rive')


    elif menu_input=='q':
        print('Total trip cost ${:.2f}'.format(bill))
        print('Taxis are now:')
        for i, objects in enumerate(taxis):
            print('{} - {}'.format(i, objects))

    elif menu_input== 'd':
        distance = float(input('Drive how far? '))
        taxis[taxi_choice].start_fare()
        taxis[taxi_choice].drive(distance)
        fare = taxis[taxi_choice].get_fare()
        bill += fare
        print('Your {} trip cost you ${:.2f}'.format(taxis[taxi_choice].name, fare))
        print('Bill to date ${:.2f}'.format(bill))
        print('q)uit, c)hoose taxi, d)rive')

    else:
        print('enter a valid option')
        print('q)uit, c)hoose taxi, d)rive')



