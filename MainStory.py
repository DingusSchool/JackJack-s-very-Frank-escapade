import random
from time import sleep


if True:  # hier worden alle checks ingevoerd, ik doe het in een IF zodat je het kan inklappen
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
    lookCheckLiving = False
    lookCheckSleep = False
    lookCheckPlay = False
    lookCheckStorage = False
    itemVynilGet = False
    itemHouseKey = False
    itemSnicker = False
    itemBadDragon = False
    itemLaserGun = False
    itemCrowbar = False
    itemBattery = False
    itemUFOKey = False
    itemDictionary = False

    monoloogMama = False
    monoloogWoon = False
    monoloogKantoor = False
    monoloog = False
    monoloog = False
    monoloog = False
    monoloog = False
    monoloog = False
    monoloog = False
    monoloog = False
    monoloog = False
    monoloog = False
    monoloog = False
    monoloog = False
    monoloog = False
    monoloog = False

    location = "kamer Jack"
    

def standard_checks(answer, locatie):
    if "back" in answer.lower():  # als speler terug wil, mag dat lekker niet
        print("You look back, only to see your deepest regrets in life.\nGoing back is not an option anymore. Ever.")
        return True

    if answer == "look":
        if locatie == "woonkamer":
            print("")

    elif answer.lower() == "i" or answer.lower() == "inventory":  # print inventory als wordt gevraagd
        print("Your current inventory:")
        print("\n- ".join(inventory))
        return True
    elif "swim" in answer.lower():  # als de speler iets met zwemmen invoert, komen er sarcastische antwoorden terug
        print("It doesn't seem like swimming would be useful on a solid surface.")
        return True
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
        return True
    elif "scream" in answer.lower():  # laat de speler lekker schreeuwen
        print("AAAAAAARRRRRRGGGGGHHHHHHH!!")
        if locatie == "alien huis binnen":
            print("The alien gets jump-scared and starts crying. You monster.")
        return True
    elif "eat" in answer.lower():
        print("I can't seem to recognize that verb.")
        return True
    else:
        return False


def item_pickups(locatie, aliensleutel, plaat, snickerreep, draakspeeltje, lasergeweer, breekijzer, accu, ufosleutel, woordenboek):
    # hier staan alle statements voor de inventory checks, als de speler "Look" heeft gebruikt
    if locatie == "woonkamer" and woonkamerCheck:
        print("You have added the record of 'Roundabout - Yes' to your inventory.")
        inventory.append("Record of 'Roundabout - Yes'")
        plaat = True
    elif locatie == "speeltuin" and speeltuinCheck:
        print("Armed with a crowbar, you continue on your journey.")
        inventory.append("Crowbar")
        breekijzer = True
    elif locatie == "ufo slaapcabine" and ufoSlaapCheck:
        print("This toy feels kinda weird, but you still insert it into your backpack.")
        inventory.append("Bad Dragon toy")
        draakspeeltje = True
    elif locatie == "ufo opslag":  # bij de opslag geven we 2 items, als er "Look" is gebruikt, geven we een 3e
        if ufoOpslagCheck:
            print("You have picked up the dictionary, this might come in handy later.")
            inventory.append("Dictionary")
            woordenboek = True
        print("You pick up the battery,")
        print("you also arm yourself with the laser gun, things might get dangerous...")
        inventory.append("UFO battery")
        inventory.append("Laser gun")
        accu = True
        lasergeweer = True
    elif locatie == "koelkast":
        print("Jack-Jack: 'You are not yourself when you are hungry, but I am not hungry yet!'")
        inventory.append("Snicker bar")
        snickerreep = True
    elif locatie == "ufo cockpit":
        print("The key! You might be able to start the spaceship with this key!")
        inventory.append("UFO key")
        ufosleutel = True
    elif locatie == "alien deurmat":
        print("This key looks identical to your own house key, and it is also under the doormat at the front door...")
        print("Jack-Jack: 'What is going on here?? How did this happen?'")
        inventory.append("Alien house key?")
        aliensleutel = True
    return locatie, aliensleutel, plaat, snickerreep, draakspeeltje, lasergeweer, breekijzer, accu, ufosleutel, woordenboek


def locatie_checks(opties, plaats, pispotcheck, deurcheck):  # check welke locaties mogelijk en verbonden zijn aan andere locaties
    if plaats == "kamer Jack":
        opties = ["overloop"]
        if "hall" in antwoord:
            plaats = "overloop"

    elif plaats == "overloop":
        opties = ["kamer Jack", "WC", "woonkamer", "kamer mama"]
        if "jack" in antwoord:
            plaats = "kamer Jack"
        if "toilet" in antwoord or "piss" in antwoord or "pee" in antwoord:
            if not pispotcheck:
                print("That was a big relief, now to continue on your way to find your mommy.")
                pispotcheck = True
            elif pispotcheck:
                print("You are REALLY nervous, aren't you? Either way, your bladder is empty.")
        elif "living" in antwoord or "down" in antwoord:
            plaats = "woonkamer"
        elif "mom" in antwoord:
            plaats = "kamer mama"

    elif plaats == "kamer mama":
        opties = ["overloop"]
        if "hall" in antwoord:
            plaats = "overloop"

    elif plaats == "woonkamer":
        opties = ["kantoor", "WC", "keuken", "overloop"]
        if "office" in antwoord or "study" in antwoord:
            plaats = "kantoor"
        elif "toilet" in antwoord or "piss" in antwoord or "pee" in antwoord:
            if not pispotcheck:
                print("That was a big relief, now to continue on your way to find your mommy.")
                pispotcheck = True
            elif pispotcheck:
                print("You are REALLY nervous, aren't you? Either way, your bladder is empty.")
        elif "kitchen" in antwoord:
            plaats = "keuken"
        elif "hall" in antwoord or "up" in antwoord:
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

    elif plaats == "koelkast":
        opties = ["keuken"]
        if "kitchen" in antwoord:
            plaats = "keuken"

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


def locatie_printen(answer, locatie, kijkwoonkamer, kijkslaapcabine, kijkspeeltuin, kijkopslag, aliensleutel, plaat, huissleutel, snickerreep, draakspeeltje, lasergeweer, breekijzer, accu, ufosleutel, woordenboek):
    if locatie == "kamer Jack":
        print("This is your own room, nothing much can be done here anymore.")

    elif locatie == "overloop":
        print("You are now in the hallway.\n"
              "One end has the toilet.\n"
              "On the other end, there is your mom's room at your right.\n"
              "If you want to go downstairs to the living room, go down.\n")

    elif locatie == "kamer mama":
        print("This is your mom's room.\n")

    elif locatie == "woonkamer":
        print("You entered the living room")
        print("On your right is the kitchen, on your left you can find your dad's office.")
        print("Jack-Jack: ’We need to find a way to get outside’")
        print("Jack-Jack: ’I remember that dad keeps the key under the doormat by the kitchen’")
        if "look" in answer:
            kijkwoonkamer = True
        if kijkwoonkamer:  # als woonkamer gekeken is, print dat er een plaat ligt
            print("")
            if not plaat:  # tenzij de plaat opgepakt is
                print("")
    elif locatie == "kantoor":
        print("")
        if not huissleutel:
            print("")
    elif locatie == "keuken":
        print("")
    elif locatie == "achtertuin":
        print("")
    elif locatie == "speeltuin":
        print("")
        if not breekijzer:
            print("")
    elif locatie == "ufo buiten":
        print("")
    elif locatie == "ufo cockpit":
        print("")
        if not ufosleutel:
            print("")
        if not accu:
            print("")
    elif locatie == "ufo opslag":
        print("")
        if "look" in answer:
            kijkopslag = True
            if kijkopslag:
                print("")
        if not accu:
            print("")
        if not woordenboek:
            print("")
    elif locatie == "ufo slaapcabine":
        print("")
        if "look" in answer:
            kijkslaapcabine = True
        if kijkslaapcabine:
            print("")
        if not draakspeeltje:
            print("")
    elif locatie == "krater":
        print("")
    elif locatie == "alien huis buiten":
        print("")
        if not aliensleutel:
            print("")
    elif locatie == "alien huis binnen":
        print("")

    return answer, locatie, kijkwoonkamer, kijkslaapcabine, kijkspeeltuin, kijkopslag, aliensleutel, plaat, huissleutel, snickerreep, draakspeeltje, lasergeweer, breekijzer, accu, ufosleutel, woordenboek


def printen(tekst):
    for i in tekst:
        sleep(random.randrange(1, 5)/25)
        print(i, end="")
    if "\n\n" in tekst:
        sleep(1)


def helpen():
    print("Instructions to the player:\n")
    print("if you want to go to an available area,\n"
          "just type 'go to [...]' or 'walk to [...]'\n")
    print("if you want to pick up an item that has been shown to you,\n"
          "type 'get [...]' or 'pick up [...]'\n")
    print("if you want to see where you are, or just look around\n"
          "where you are currently, type 'look'\n")
    print("if you want to see this menu again,\n"
          "type 'help' or 'h'\n")


def monoloog_typen(locatie, mama, woon):
    if locatie == "kamer mama":
        print("opens door")
        print("Jack-Jack: ‘mom?’ ")
        printen(".........\n\n")
        print("Jack-Jack: ’Mom, are you there?’")
        printen(".........\n\n")
        print("mom seems to be gone, I’m afraid you are on your own.")
        mama = True
    
    elif locatie == "woonkamer":
        woon = True
    
    return locatie, mama, woon


# hier start het verhaal
helpen()
# printen("\n\n")
# printen("\n\n")
# printen("\n\n")
# printen("You (Jack-Jack) get woken up by a loud noise in the middle of the night\n\n")
# printen("wow, that was super intense! What would that be?\n")
# printen("let’s look for mom.\n")
# printen("*grabs backpack*\n")
# printen("Jack-Jack: ‘Just in case’")
# print("\n if you want to access your backpack during any point of the game,")
# print("enter the command 'i' or 'inventory'")

while True:
    antwoord = input("\n  >>> ")
    antwoord = antwoord.lower()
    if antwoord == "help" or antwoord == "h":
        helpen()
    elif standard_checks(antwoord, location):
        pass
    elif "pick" in antwoord or "get" in antwoord:
        location, alienKeyCheck, itemVynilGet, itemSnicker, itemBadDragon, itemLaserGun, itemCrowbar, itemBattery, itemUFOKey, itemDictionary = item_pickups(location, alienKeyCheck, itemVynilGet, itemSnicker, itemBadDragon, itemLaserGun, itemCrowbar, itemBattery, itemUFOKey, itemDictionary)
    elif "go" in antwoord or "walk" in antwoord:
        options, location, bathroomCheck, doorOpenCheck = locatie_checks(options, location, bathroomCheck, doorOpenCheck)
    elif "open" in antwoord:
        if location == "kantoor":
            if "1" in antwoord:
                print("")
            if "2" in antwoord:
                print("In between the piles of documents you find the back-up key!")
                print("You put the key in your pocket.")
                print("Jack-Jack: 'But why was it not under the doormat?'")
                inventory.append("House key")
                huisslueutel = True

    else:
        print("\033[91m{}\033[00m".format("I can't seem to understand this command"))
    antwoord, location, lookCheckLiving, lookCheckSleep, lookCheckPlay, lookCheckStorage, alienKeyCheck, itemVynilGet, itemHouseKey, itemSnicker, itemBadDragon, itemLaserGun, itemCrowbar, itemBattery, itemUFOKey, itemDictionary = locatie_printen(
        antwoord, location, lookCheckLiving, lookCheckSleep, lookCheckPlay, lookCheckStorage, alienKeyCheck,
        itemVynilGet, itemHouseKey, itemSnicker, itemBadDragon, itemLaserGun, itemCrowbar, itemBattery, itemUFOKey,
        itemDictionary)
    location, monoloogMama, monoloogWoon = monoloog_typen(location, monoloogMama, monoloogWoon)

