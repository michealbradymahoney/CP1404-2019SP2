HEX_COLOURS = {"red": "ff0000", "orange": "ffa500", "yellow": "ffff00", "green": "00ff00", "blue": "0000ff",
               "indigo": "4b0082", "violet": "ee82ee", "black": "000000", "white": "ffffff", "gray": "808080"}

colour = input("Enter a colour: ").lower()
while colour != "":
    if colour in HEX_COLOURS:
        print("{} is {}".format(colour, HEX_COLOURS[colour]))
    else:
        print("Invalid colour")
    colour = input("Enter a colour: ").lower()