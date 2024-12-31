def start():
    print("Tu esi sagatavojies apzagt māju. Tu esi saņēmis informāciju par mājas īpašniekiem un to vērtīgo mantu atrašanās vietām.")
    print("Tagad tev jāizlemj, kā iekļūt mājā.")
    
    izvele = input("1. Izmanto durvis un mēģini iekļūt caur ieejas durvīm.\n2. Izmanto logu, lai iekļūtu mājā.\n3. Meklē pagrabu.\nIzvēlies (1/2/3): ")

    if izvele == "1":
        caur_durvim()
    elif izvele == "2":
        caur_logu()
    elif izvele == "3":
        caur_pagrabu()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        start()

def caur_durvim():
    print("\nTu mēģini atvērt durvis, bet tās ir aizslēgtas. Tomēr redzi, ka durvju blakus ir logi, kas varētu būt vaļā.")
    izvele = input("1. Pārbaudi, vai logi ir atvērti.\n2. Mēģini izsist durvis.\nIzvēlies (1/2): ")

    if izvele == "1":
        caur_logu()
    elif izvele == "2":
        lauzt_durvis()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        caur_durvim()

def lauzt_durvis():
    print("\nTu izsist durvis, bet trokšņojot pievērš uzmanību kaimiņiem. Policija ierodas, un tu esi aizturēts. Beigas!")
    
def caur_logu():
    print("\nTu izdari veiklu pāreju caur logu un ieej mājā. Tagad esi iekšā.")
    print("Iekšā ir tumsā, un tu dzirdi soļus, kas nāk no augšas. Kas jādara?")
    izvele = input("1. Steidzīgi ej uz augšu, lai atrastu dārgumus.\n2. Paliec klusumā un izgaist, ja kāds atnāks.\nIzvēlies (1/2): ")

    if izvele == "1":
        augsa_dargumi()
    elif izvele == "2":
        slepties()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        caur_logu()

def augsa_dargumi():
    print("\nTu nokļūsti augšā, kur atradīsi vērtīgu dārgumu kasti. Taču pie viena dārguma skapja pēkšņi ieslēdzas trauksmes signāls!")
    izvele = input("1. Ņem dārgumus un steidzīgi bēdz!\n2. Pārtrauc, saproti, ka risks nav vērts, un meklē citu vietu.\nIzvēlies (1/2): ")

    if izvele == "1":
        tiec_arestets()
    elif izvele == "2":
        atgreizies_pagraba()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        augsa_dargumi()

def tiec_arestets():
    print("\nTu paķeri dārgumus, bet trauksmes signāls piesaista policiju. Tevi aiztur un nogādā cietumā. Beigas!")
    
def atgreizies_pagraba():
    print("\nTu pārtrauc un atgriezies pagrabiņā, bet, kad kāp laukā no pagraba, tu dzirdi soļus. Policija ierodas. Beigas!")

def slepties():
    print("\nTu paliec klusumā, bet, izdzirdot soļus, tu nolemj bēgt. Diemžēl pie durvīm tu sastopi mājas īpašnieku.")
    izvele = input("1. Izsist mājas īpašniekam no rokām ieroci un bēdz!\n2. Pārsteidz mājas īpašnieku ar mieru un cenšoties bēgt.\nIzvēlies (1/2): ")

    if izvele == "1":
        tiec_arestets()
    elif izvele == "2":
        izklut()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        slepties()

def izklut():
    print("\nTu veiksmīgi iznāc no mājas, bet policija tev sāk sekot. Tava bēgšana beidzas ar aizturēšanu. Beigas!")

def caur_pagrabu():
    print("\nTu pieej pagraba logiem un nolemj ieiet pa pagrabu. Tu dzirdi suņa riešanu, taču tu esi uzmanīgs.")
    izvele = input("1. Klusām ieej un tuvojies slēptajam dārgumam.\n2. Ej ārā no pagraba, jo tu esi dzirdējis kādu skrienam.\nIzvēlies (1/2): ")

    if izvele == "1":
        atrast_dargumi_pagraba()
    elif izvele == "2":
        sunis_noker()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        caur_pagrabu()

def atrast_dargumi_pagraba():
    print("\nTu atrod dārgumus un apmierināts ar panākumiem pamet māju. Taču, kad tu domā par aizbēgšanu, tevi ielenc policija.")
    print("Beigas!")

def sunis_noker():
    print("\nPagrabā ir suns, kas uzbrūk tev, kad tu mēģini iziet. Tevi noķer un aiztur. Beigas!")

# Spēles sākums
start()
