"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = Celsius_to_Fahrenheit(float(input("Celsius: ")))
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            celsius = Fahrenheit_to_Celsius(float(input("Fahrenheit: ")))
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def Fahrenheit_to_Celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def Celsius_to_Fahrenheit(celsius):

    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()