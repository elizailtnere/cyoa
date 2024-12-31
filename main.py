# Spēlētāja dzīvības
dzivibas = 3

def start():
    global dzivibas
    dzivibas = 3  # Reset dzīvības spēles sākumā
    print("**********************************************")
    print("Laipni lūdzam spēlē 'Mājas apzagšana'!")
    print("Tu spēlēsi kā mājas zaglis, kura mērķis ir apzagt dažādas mājas, izvēloties no dažādiem īpašniekiem.")
    print("Katrs īpašnieks ir citādāks, un katrai mājai ir savi izaicinājumi un drošības riski.")
    print("Tavs uzdevums ir pieņemt pareizās izvēles un apzagt māju, izvairoties no aizdomīgiem cilvēkiem un trauksmes sistēmām.")
    print("Tomēr esi uzmanīgs, jo katra tavu izvēļu sekas var būt atšķirīgas, un ne visas izvēles beidzas veiksmīgi!\n")
    
    izvele = input("Vai vēlies uzzināt spēles noteikumus un instrukcijas? (Jā/Nē)\n\nIzvēlies (Jā/Nē): ")

    if izvele.lower() == "jā":
        noteikumi()
    elif izvele.lower() == "nē":
        pasakot_vairs_uzsakt()
    else:
        zaude_dzivibu()
        start()

def zaude_dzivibu():
    global dzivibas
    dzivibas -= 1
    if dzivibas > 0:
        print(f"Nederīga izvēle. Tev ir palikušas {dzivibas} dzīvības. Mēģini vēlreiz.\n")
    else:
        print("Tev beidzās dzīvības. Spēle beigusies!\n")
        exit()

# Spēles noteikumu paskaidrojums
def noteikumi():
    print("------------------------------------------")
    print("Spēles noteikumi:")
    print("1. Tu izvēlies, kuru māju tu vēlies apzagt. Katram īpašniekam ir savi izaicinājumi un ceļi, kā iekļūt mājā.")
    print("2. Katru reizi, kad tu veic izvēli, tev būs jāizdara secīga izvēle, lai pārvarētu šķēršļus un sagūstītu vērtīgos priekšmetus.")
    print("3. Tev ir jābūt uzmanīgam, jo dažas izvēles var novest pie aizturēšanas vai pat slēptiem zaudējumiem.")
    print("4. Dažas izvēles var izbeigt spēli ar aizturēšanu, citas ļaus tev veiksmīgi iznāk no mājas ar mantām.")
    print("5. Katrs īpašnieks ir atšķirīgs, tāpēc izvēles būs dažādas katram scenārijam.\n")
    print("Spēlē galvenais ir pieņemt pareizās izvēles, lai iegūtu dārgumus un izvairītos no aizturēšanas!\n")
    print("------------------------------------------")

    izvele = input("Kad esi gatavs, spied jebkuru taustiņu, lai uzsāktu spēli...\n")
    pasakot_vairs_uzsakt()

def pasakot_vairs_uzsakt():
    print("\nLieliski! Sāc spēli, izvēloties, kuru māju vēlies apzagt.")
    print("Izvēlies kādu no mājas īpašniekiem:\n")
    print("1. Nabadzīga vecmāmiņa")
    print("2. Baņķieris")
    print("3. Slavenība - Kima Kardašiana\n")
    
    izvele = input("Izvēlies (1/2/3): ")

    if izvele == "1":
        vecmamina()
    elif izvele == "2":
        bankieris()
    elif izvele == "3":
        kim_kardashian()
    else:
        zaude_dzivibu()
        pasakot_vairs_uzsakt()

# Nabadzīga vecmāmiņa
def vecmamina():
    print("\nTu izvēlējies apzagt nabadzīgu vecmāmiņu. Māja ir maza un veca, bet vecmāmiņa ir ļoti laipna un aizsargāta.")
    print("\nIzvēles:\n")
    print("1. Iekļūt mājā pa logu.")
    print("2. Iekļūt caur durvīm, izmantojot viltus stāstu.")
    print("3. Mēģini piesist pie durvīm kā viesis.\n")
    
    izvele = input("Izvēlies (1/2/3): ")
    
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
    print("\nTu piesit pie durvīm un saki, ka esi radinieks, kas atnesis vecmāmiņai palīdzību. Viņa tev uzticas un ielaiž iekšā.")
    print("\nIzvēles:\n")
    print("1. Mēģini apzagt viņu, kamēr viņa ir prom.")
    print("2. Pajautā, vai viņa var tev dot naudu.\n")
    
    izvele = input("Izvēlies (1/2): ")

    if izvele == "1":
        apzagt_vecmaminu()
    elif izvele == "2":
        nopecot_naudu()
    else:
        zaude_dzivibu()
        viesis_stasts()

def apzagt_vecmaminu():
    print("\nTu apzagji vecmāmiņu, bet viņa sāk kliegt un piezvana policijai. Tevi noķer!")
    print("Beigas! Tevi aiztur policija.\n")

def nopecot_naudu():
    print("\nVecmāmiņa labprāt tev dod naudu, jo viņa nezin, ka tu esi zaglis. Tu aizbrauc ar naudu un veic bēgšanu. Veiksmīgi!")
    print("Beigas: Tu aizbēdz ar naudu.\n")

# Baņķieris
def bankieris():
    print("\nTu izvēlējies apzagt baņķieri. Viņš dzīvo dārgā villā, un viņa māja ir pilna ar vērtīgiem priekšmetiem.")
    print("\nIzvēles:\n")
    print("1. Iekļūt mājā pa durvīm, izmantojot izdomātu stāstu.")
    print("2. Iekļūt mājā pa logu.")
    print("3. Mēģini apzagt viņu, kamēr viņš ir prom.\n")
    
    izvele = input("Izvēlies (1/2/3): ")
    
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
    print("\nTu izlēmi iekļūt mājā pa logu. Tā ir sarežģīta izvēle, jo logs ir augstu, un tu vari viegli nokrist.")
    print("Tu mēģini kāpt pa ārdurvīm, bet neturi līdzsvaru, un nokrīti uz zemes! Spēle beigusies.")
    print("Beigas! Tu nokriti un ievainojies.\n")

def caur_logu_bankieris():
    print("\nTu mēģini iekļūt mājā pa logu, bet baņķiera mājā ir sarežģītas drošības sistēmas. Tu izsit logu, bet tas aktivizē trauksmi!")
    print("Beigas! Tu esi noķerts!\n")

def durvju_viltus_stasts():
    print("\nTu nolem izdomāt viltus stāstu, ka esi izsists un meklē palīdzību. Vecmāmiņa uzticas tev, bet viņa ir pārāk laipna.")
    print("Viņa iepazīstina tevi ar visiem saviem dārgumiem, bet tev nākas pazust no viņas mājas, jo viņa sauc policiju!")
    print("Beigas! Tevi noķer!\n")

def durvju_stasts_bankierim():
    print("\nTu pie durvīm izdomā stāstu, ka esi piegādātājs. Baņķieris piekrīt tevi ielaist, bet viņš ir ļoti aizdomīgs.")
    print("Tevi noķer, kad tu mēģini apzagt viņu!")
    print("Beigas! Tu esi noķerts!\n")

def apzagt_bankieri():
    print("\nBaņķieris ir ļoti aizdomīgs un, kad tu mēģini apzagt viņu, viņš piespiež nospiest trauksmes pogu!")
    print("\nIzvēles:\n")
    print("1. Mēģini aizbēgt ātri.")
    print("2. Mēģini samierināt baņķieri, apgalvojot, ka tev vajag naudu.\n")
    
    izvele = input("Izvēlies (1/2): ")

    if izvele == "1":
        aizbēgt_no_bankiera()
    elif izvele == "2":
        samierinaties_ar_bankieri()
    else:
        zaude_dzivibu()
        apzagt_bankieri()

def aizbēgt_no_bankiera():
    print("\nTu bēdz un izkļūsti no mājas, bet policija tevi izseko un noķer. Beigas!\n")
    
def samierinaties_ar_bankieri():
    print("\nBaņķieris piekrīt tev palīdzēt, bet viņam ir noslēpumaina aģenta palīdzība, un tu esi noķerts. Beigas!\n")

# Spēles sākums
start()
