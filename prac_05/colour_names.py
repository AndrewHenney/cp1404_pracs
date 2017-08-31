COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4"}

colour = input("Enter colour name: ")
while colour != "":
    if colour in COLOUR_CODES:
        print("The hexadecimal code for", colour, "is", COLOUR_CODES[colour])
    else:
        print("Colour not in colour directory")
    colour = input("Enter colour name: ")

