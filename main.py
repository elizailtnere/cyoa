# Global variable for player lives
dzivibas = 3

def start():
    global dzivibas
    dzivibas = 3  # Reset lives at the start of the game
    print("**********************************************")
    print("Welcome to the game 'House Robbery'!")
    print("You play as a burglar whose goal is to rob different houses by choosing from different owners.")
    print("Each owner has their own challenges and risks to enter the house.")
    print("Your task is to make the right choices to rob the house while avoiding suspicious people and alarm systems.")
    print("But be careful, every choice has consequences, and not all choices lead to success!\n")
    
    izvele = input("Do you want to know the rules and instructions? (Yes/No)\n\nChoose (Yes/No): ")

    if izvele.lower() == "yes":
        noteikumi()
    elif izvele.lower() == "no":
        pasakot_vairs_uzsakt()
    else:
        zaude_dzivibu()
        start()

def zaude_dzivibu():
    global dzivibas
    dzivibas -= 1
    if dzivibas > 0:
        print(f"Invalid choice. You have {dzivibas} lives left. Try again.\n")
    else:
        print("You have run out of lives. The game is over!\n")
        restart = input("Would you like to restart the game? (Yes/No): ")
        if restart.lower() == "yes":
            start()
        else:
            print("Goodbye!")
            exit()

# Game rules explanation
def noteikumi():
    print("------------------------------------------")
    print("Game Rules:")
    print("1. You choose which house you want to rob. Each owner has their own challenges and ways to enter the house.")
    print("2. Every time you make a choice, you will need to make a sequence of decisions to overcome obstacles and get valuable items.")
    print("3. Be careful, as some choices can lead to capture or hidden losses.")
    print("4. Some choices can end the game with capture, while others will let you escape with the loot.")
    print("5. Every owner is different, so the choices vary for each scenario.\n")
    print("The key is to make the right decisions to get the treasures and avoid getting caught!\n")
    print("------------------------------------------")

    izvele = input("When you're ready, press any key to start the game...\n")
    pasakot_vairs_uzsakt()

def pasakot_vairs_uzsakt():
    print("\nGreat! Start the game by choosing which house you want to rob.")
    print("Choose one of the house owners:\n")
    print("1. Poor Grandmother")
    print("2. Banker")
    print("3. Celebrity - Kim Kardashian\n")
    
    izvele = input("Choose (1/2/3): ")

    if izvele == "1":
        vecmamina()
    elif izvele == "2":
        bankieris()
    elif izvele == "3":
        kim_kardashian()
    else:
        zaude_dzivibu()
        pasakot_vairs_uzsakt()

# Poor Grandmother
def vecmamina():
    print("\nYou chose to rob a poor grandmother. The house is small and old, but the grandmother is very kind and cautious.")
    print("\nChoices:\n")
    print("1. Enter the house through the window.")
    print("2. Enter through the door using a fake story.")
    print("3. Knock on the door as a visitor.\n")
    
    izvele = input("Choose (1/2/3): ")
    
    if izvele == "1":
        caur_logu()
    elif izvele == "2":
        durvju_viltus_stasts()
    elif izvele == "3":
        viesis_stasts()
    else:
        zaude_dzivibu()
        vecmamina()

def viesis_stasts():
    print("\nYou knock on the door and claim to be a relative bringing help. She trusts you and lets you in.")
    print("\nChoices:\n")
    print("1. Try to rob her while she's away.")
    print("2. Ask if she can give you some money.\n")
    
    izvele = input("Choose (1/2): ")

    if izvele == "1":
        apzagt_vecmaminu()
    elif izvele == "2":
        nopecot_naudu()
    else:
        zaude_dzivibu()
        viesis_stasts()

def apzagt_vecmaminu():
    print("\nYou robbed the grandmother, but she starts screaming and calls the police. You get caught!")
    print("Game Over! You were arrested by the police.\n")

def nopecot_naudu():
    print("\nThe grandmother kindly gives you money because she doesn't know you're a burglar. You escape with the money. Success!")
    print("Game Over: You escaped with the money.\n")

# Banker
def bankieris():
    print("\nYou chose to rob a banker. He lives in an expensive villa, and his house is full of valuable items.")
    print("\nChoices:\n")
    print("1. Enter through the door with a made-up story.")
    print("2. Enter through the window.")
    print("3. Try to rob him while he's away.\n")
    
    izvele = input("Choose (1/2/3): ")
    
    if izvele == "1":
        durvju_stasts_bankierim()
    elif izvele == "2":
        caur_logu_bankieris()
    elif izvele == "3":
        apzagt_bankieri()
    else:
        zaude_dzivibu()
        bankieris()

def caur_logu():
    print("\nYou decided to enter through the window. It is a tricky choice because the window is high and you could easily fall.")
    print("You try to climb the outer wall, but you lose your balance and fall to the ground! Game over.")
    print("Game Over: You fell and got injured.\n")

def caur_logu_bankieris():
    print("\nYou try to enter the house through the window, but the banker's house has advanced security systems. You break the window, but it activates an alarm!")
    print("Game Over: You got caught!\n")

def durvju_viltus_stasts():
    print("\nYou decide to come up with a fake story that you were robbed and are looking for help. The grandmother trusts you, but she's too kind.")
    print("She introduces you to all her valuables, but you have to leave quickly because she calls the police!")
    print("Game Over: You got caught!\n")

def durvju_stasts_bankierim():
    print("\nAt the door, you make up a story that you're a delivery person. The banker agrees to let you in, but he's very suspicious.")
    print("You get caught when you try to rob him!")
    print("Game Over: You got caught!\n")

def apzagt_bankieri():
    print("\nThe banker is very suspicious and when you try to rob him, he presses the alarm button!")
    print("\nChoices:\n")
    print("1. Try to escape quickly.")
    print("2. Try to calm the banker down by saying you need money.\n")
    
    izvele = input("Choose (1/2): ")

    if izvele == "1":
        aizbēgt_no_bankiera()
    elif izvele == "2":
        samierinaties_ar_bankieri()
    else:
        zaude_dzivibu()
        apzagt_bankieri()

def aizbēgt_no_bankiera():
    print("\nYou run and escape from the house, but the police track you down and catch you. Game over!")
    
def samierinaties_ar_bankieri():
    print("\nThe banker agrees to help you, but his mysterious agent friend catches you, and you get caught. Game over!\n")

# Kim Kardashian
def kim_kardashian():
    print("\nYou chose to rob Kim Kardashian. Her house is very expensive and full of luxury items.")
    print("But she has very good security and many cameras. Be careful!\n")
    
    print("Choices:\n")
    print("1. Try to break in through the basement.")
    print("2. Enter through the front door with a fake story.")
    print("3. Try to ring the doorbell and say you have a delivery.\n")
    
    izvele = input("Choose (1/2/3): ")
    
    if izvele == "1":
        pagraba_ielauzums()
    elif izvele == "2":
        durvju_viltus_stasts_kim()
    elif izvele == "3":
        zvans_durvīs()
    else:
        zaude_dzivibu()
        kim_kardashian()

def pagraba_ielauzums():
    print("\nYou try to break in through the basement, but there are modern security systems. You manage to get in, but the alarm goes off!")
    print("Game Over: You got caught by the guards!\n")

def durvju_viltus_stasts_kim():
    print("\nYou try to enter through the front door with a fake story, but Kim's security staff is too professional and catches you!")
    print("Game Over: You got caught!\n")

def zvans_durvīs():
    print("\nYou ring the doorbell and tell them you have a delivery, but the guards are suspicious and you get caught!")
    print("Game Over: You got caught!\n")
