import random

inventory = []
options = []
woonkamerCheck = False
speeltuinCheck = False
ufoSlaapCheck = False
ufoOpslagCheck = False
bathroomCheck = False
planetBussCheck = False
alienKeyCheck = False
doorOpenCheck = False
location = "kamer Jack"
antwoord = ""


def standard_checks(answer, locatie):
    if "back" in answer.lower():  # als speler terug wil, mag dat lekker niet
        print("You look back, only to see your deepest regrets in life. Going back is not an option anymore. Ever.")
    elif answer.lower() == "i" or answer.lower() == "inventory":  # print inventory als wordt gevraagd
        print("Your current inventory:")
        print("\n- ".join(inventory))
    elif "swim" in answer.lower():  # als de speler iets met zwemmen invoert, komen er sarcastische antwoorden terug
        print("It doesn't seem like swimming would be useful on a solid surface.")
    elif "jump" in answer.lower():  # als de speler iets met springen invoert, komen er sarcastische antwoorden terug
        if locatie == "speeltuin":
            print("You jump off of the slide, your ankle hurts a bit.")
        else:
            random_getal = random.randrange(1, 4)
            if random_getal == 1:
                print("Wow, your feet are off the ground! :D")
            elif random_getal == 2:
                print("You jump about 20cm high.")
            elif random_getal == 3:
                print("You feel like you are flying! WEEEE")
    elif "scream" in answer.lower():  # laat de speler lekker schreeuwen
        print("AAAAAAARRRRRRGGGGGHHHHHHH!!")
        if locatie == "alien huis binnen":
            print("The alien gets jump-scared and starts crying. You monster.")
    elif "eat" in answer.lower():
        print("I can't seem to recognize that verb.")
    return answer


def item_pickups(locatie, sleutel):
    # hier staan alle statements voor de inventory checks, als de speler "Look" heeft gebruikt
    if locatie == "woonkamer" and woonkamerCheck:
        print("You have added the record of 'Roundabout - Yes' to your inventory.")
        inventory.append("Record of 'Roundabout - Yes'")
    elif locatie == "speeltuin" and speeltuinCheck:
        print("Armed with a crowbar, you continue on your journey.")
        inventory.append("Crowbar")
    elif locatie == "ufo slaapcabine" and ufoSlaapCheck:
        print("This toy feels kinda weird, but you still insert it into your backpack.")
        inventory.append("Bad Dragon toy")
    elif locatie == "ufo opslag":  # bij de opslag geven we 2 items, als er "Look" is gebruikt, geven we een 3e
        if ufoOpslagCheck:
            print("You have picked up the dictionary, this might come in handy later.")
            inventory.append("Dictionary")
        print("You pick up the battery,")
        print("you also arm yourself with the laser gun, things might get dangerous...")
        inventory.append("UFO battery")
        inventory.append("Laser gun")
    elif locatie == "kantoor la 2":  # vanaf hier geven we de items gewoon gratis als ze in een plek zijn
        print("You put the key in your pocket.")
        print("Jack-Jack: 'But why was it not under the doormat?'")
        inventory.append("House key")
    elif locatie == "koelkast":
        print("Jack-Jack: 'Scrumdiddlyumptious.'")
        inventory.append("Granola bar")
    elif locatie == "ufo cockpit":
        print("The key! You might be able to start the spaceship with this key!")
        inventory.append("UFO key")
    elif locatie == "alien deurmat":
        print("This key looks identical to your own house key, and it is also under the doormat at the front door...")
        print("Jack-Jack: 'What is going on here?? How did this happen?'")
        inventory.append("Alien house key?")
        sleutel = True
    return locatie, sleutel


def locatie_checks(opties, plaats, pispotcheck, deurcheck):  # check welke locaties mogelijk en verbonden zijn aan andere locaties
    if plaats == "kamer Jack":
        opties = ["overloop"]
        if "hallway" in antwoord:
            plaats = "overloop"

    elif plaats == "overloop":
        opties = ["kamer Jack", "WC", "woonkamer", "kamer mama"]
        if "Jack" in antwoord:
            plaats = "kamer Jack"
        if "toilet" in antwoord:
            if not pispotcheck:
                print("That was a big relief, now to continue on your way to find your mommy.")
                pispotcheck = True
            elif pispotcheck:
                print("You are REALLY nervous, aren't you? Either way, your bladder is empty.")
        elif "living" in antwoord or "up" in antwoord:
            plaats = "woonkamer"
        elif "mom" in antwoord:
            plaats = "kamer mama"

    elif plaats == "kamer mama":
        opties = ["overloop"]
        if "hallway" in antwoord:
            plaats = "overloop"

    elif plaats == "woonkamer":
        opties = ["kantoor", "WC", "keuken", "overloop"]
        if "office" in antwoord or "study" in antwoord:
            plaats = "kantoor"
        elif "toilet" in antwoord:
            if not pispotcheck:
                print("That was a big relief, now to continue on your way to find your mommy.")
                pispotcheck = True
            elif pispotcheck:
                print("You are REALLY nervous, aren't you? Either way, your bladder is empty.")
        elif "kitchen" in antwoord:
            plaats = "keuken"
        elif "hallway" in antwoord or "up" in antwoord:
            plaats = "overloop"

    elif plaats == "kantoor":
        opties = ["kantoor la 1", "kantoor la 2", "woonkamer"]
        if "1" in antwoord:
            print("You see something that you really don't like and instantly close the drawer back up.")
        elif "2" in antwoord:
            plaats = "kantoor la 2"
        elif "living" in antwoord:
            plaats = "woonkamer"

    elif plaats == "keuken":
        opties = ["woonkamer", "koelkast", "achtertuin"]
        if "living" in antwoord:
            plaats = "woonkamer"
        elif "fridge" in antwoord:
            plaats = "koelkast"
        elif "ard" in antwoord:  # yARD en gARDen zijn beide goede manieren om naar de achtertuin te komen
            if "House key" in inventory:  # als we HouseKey hebben, mag je naar buiten
                inventory.remove("House key")
                deurcheck = True
            elif "House key" not in inventory:  # als we HouseKey niet hebben, mag je niet naar buiten
                if deurcheck:  # tenzij je de HouseKey al hebt gebruikt
                    plaats = "achtertuin"

    elif plaats == "achtertuin":
        opties = ["speeltuin", "ufo buiten", "keuken"]
        if "play" in antwoord:
            plaats = "speeltuin"
        elif "ufo" in antwoord:
            plaats = "ufo buiten"
        elif "kitchen" in antwoord:
            plaats = "keuken"

    elif plaats == "speeltuin":
        opties = ["achtertuin"]
        if "ard" in antwoord:
            plaats = "achtertuin"

    elif plaats == "ufo buiten":
        opties = ["ufo cockpit", "achtertuin"]
        if "inside" in antwoord or "ufo" in antwoord:
            plaats = "ufo cockpit"
        elif "ard" in antwoord:
            plaats = "achtertuin"

    elif plaats == "ufo cockpit":
        if not planetBussCheck:  # als we op de planeet zijn, kan je niet meer naar de achtertuin, nu wel naar de krater
            opties = ["ufo opslag", "ufo slaapcabine", "achtertuin"]
            if "storage" in antwoord:
                plaats = "ufo opslag"
            elif "cabin" in antwoord:
                plaats = "ufo slaapcabine"
            elif "out" in antwoord or "ard" in antwoord:
                plaats = "achtertuin"
        elif planetBussCheck:
            opties = ["ufo opslag", "ufo slaapcabine", "krater"]
            if "storage" in antwoord:
                plaats = "ufo opslag"
            elif "cabin" in antwoord:
                plaats = "ufo slaapcabine"
            elif "out" in antwoord:
                plaats = "krater"

    elif plaats == "ufo opslag":
        opties = ["ufo cockpit"]
        if "cock" in antwoord:
            plaats = "ufo cockpit"

    elif plaats == "ufo slaapcabine":
        opties = ["ufo cockpit"]
        if "cock" in antwoord:
            plaats = "ufo cockpit"

    elif plaats == "krater":
        opties = ["alien huis buiten", "ufo cockpit"]
        if "house" in antwoord:
            plaats = "alien huis buiten"
        elif "ufo" in antwoord or "cock" in antwoord:
            plaats = "ufo cockpit"

    elif plaats == "alien huis buiten":
        if not alienKeyCheck:  # als de alien-sleutel nog niet gepakt is, is de deurmat nog een optie
            opties = ["alien deurmat", "alien huis binnen"]
            if "mat" in antwoord:
                plaats = "alien deurmat"
            elif "door" in antwoord or "in" in antwoord:
                plaats = "alien huis binnen"
        elif alienKeyCheck:
            opties = ["alien huis binnen"]
            if "door" in antwoord or "in" in antwoord:
                plaats = "alien huis binnen"

    elif plaats == "alien huis binnen":
        opties = ["alien huis buiten"]
        if "out" in antwoord:
            plaats = "alien huis buiten"

    return opties, plaats, pispotcheck, deurcheck


while True:
    # location = input("locatie: ")
    antwoord = standard_checks(input("\n  >>> "), location).lower()
    if "pick" in antwoord:
        location, alienKeyCheck = item_pickups(location, alienKeyCheck)

    if "go" in antwoord:
        options, location, bathroomCheck, doorOpenCheck = locatie_checks(options, location, bathroomCheck, doorOpenCheck)
    print(location)
