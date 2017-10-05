from prac_08.silver_service_taxi import SilverServiceTaxi

Hummer=SilverServiceTaxi('Hummer', 18, 2)
Hummer.drive(40)
print(Hummer)
print('${:.2f}'.format(Hummer.get_fare()))
