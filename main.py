def start():
    print("Tu esi sagatavojies apzagt māju. Tu esi saņēmis informāciju par mājas īpašniekiem un to vērtīgo mantu atrašanās vietām.")
    print("Tagad tev jāizlemj, kā iekļūt mājā.")
    
    choice = input("1. Izmanto durvis un mēģini iekļūt caur ieejas durvīm.\n2. Izmanto logu, lai iekļūtu mājā.\n3. Meklē pagrabu.\nIzvēlies (1/2/3): ")

    if choice == "1":
        through_door()
    elif choice == "2":
        through_window()
    elif choice == "3":
        through_basement()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        start()

def through_door():
    print("\nTu mēģini atvērt durvis, bet tās ir aizslēgtas. Tomēr redzi, ka durvju blakus ir logi, kas varētu būt vaļā.")
    choice = input("1. Pārbaudi, vai logi ir atvērti.\n2. Mēģini izsist durvis.\nIzvēlies (1/2): ")

    if choice == "1":
        through_window()
    elif choice == "2":
        break_door()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        through_door()

def break_door():
    print("\nTu izsist durvis, bet trokšņojot pievērš uzmanību kaimiņiem. Policija ierodas, un tu esi aizturēts. Beigas!")
    
def through_window():
    print("\nTu izdari veiklu pāreju caur logu un ieej mājā. Tagad esi iekšā.")
    print("Iekšā ir tumsā, un tu dzirdi soļus, kas nāk no augšas. Kas jādara?")
    choice = input("1. Steidzīgi ej uz augšu, lai atrastu dārgumus.\n2. Paliec klusumā un izgaist, ja kāds atnāks.\nIzvēlies (1/2): ")

    if choice == "1":
        upstairs_find_treasure()
    elif choice == "2":
        hide()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        through_window()

def upstairs_find_treasure():
    print("\nTu nokļūsti augšā, kur atradīsi vērtīgu dārgumu kasti. Taču pie viena dārguma skapja pēkšņi ieslēdzas trauksmes signāls!")
    choice = input("1. Ņem dārgumus un steidzīgi bēdz!\n2. Pārtrauc, saproti, ka risks nav vērts, un meklē citu vietu.\nIzvēlies (1/2): ")

    if choice == "1":
        get_arrested()
    elif choice == "2":
        return_to_basement()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        upstairs_find_treasure()

def get_arrested():
    print("\nTu paķeri dārgumus, bet trauksmes signāls piesaista policiju. Tevi aiztur un nogādā cietumā. Beigas!")
    
def return_to_basement():
    print("\nTu pārtrauc un atgriezies pagrabiņā, bet, kad kāp laukā no pagraba, tu dzirdi soļus. Policija ierodas. Beigas!")

def hide():
    print("\nTu paliec klusumā, bet, izdzirdot soļus, tu nolemj bēgt. Diemžēl pie durvīm tu sastopi mājas īpašnieku.")
    choice = input("1. Izsist mājas īpašniekam no rokām ieroci un bēdz!\n2. Pārsteidz mājas īpašnieku ar mieru un cenšoties bēgt.\nIzvēlies (1/2): ")

    if choice == "1":
        get_arrested()
    elif choice == "2":
        escape()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        hide()

def escape():
    print("\nTu veiksmīgi iznāc no mājas, bet policija tev sāk sekot. Tava bēgšana beidzas ar aizturēšanu. Beigas!")

def through_basement():
    print("\nTu pieej pagraba logiem un nolemj ieiet pa pagrabu. Tu dzirdi suņa riešanu, taču tu esi uzmanīgs.")
    choice = input("1. Klusām ieej un tuvojies slēptajam dārgumam.\n2. Ej ārā no pagraba, jo tu esi dzirdējis kādu skrienam.\nIzvēlies (1/2): ")

    if choice == "1":
        find_basement_treasure()
    elif choice == "2":
        get_caught_by_dog()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        through_basement()

def find_basement_treasure():
    print("\nTu atrod dārgumus un apmierināts ar panākumiem pamet māju. Taču, kad tu domā par aizbēgšanu, tevi ielenc policija.")
    print("Beigas!")

def get_caught_by_dog():
    print("\nPagrabā ir suns, kas uzbrūk tev, kad tu mēģini iziet. Tevi noķer un aiztur. Beigas!")

# Spēles sākums
start()
