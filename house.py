name =input("what's your name? ")

match name:
    case "Harry" | "Herimion" | "Draco":
        print("Gryffindor")
    case _:
        print("who?")