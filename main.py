# Globālā mainīgā spēlētāja dzīvībām
dzivibas = 3

def start():
    global dzivibas
    dzivibas = 3  # Atjauno dzīvības spēles sākumā
    print("**********************************************")
    print("Laipni lūdzam spēlē 'Mājas apzagšana'!")
    print("Tu spēlēsi kā mājas zaglis, kura mērķis ir apzagt dažādas mājas, izvēloties no dažādiem īpašniekiem.")
    print("Katram īpašniekam ir savi izaicinājumi un riski, kā iekļūt mājā.")
    print("Tavs uzdevums ir pieņemt pareizās izvēles, lai apzagt māju, izvairoties no aizdomīgiem cilvēkiem un trauksmes sistēmām.")
    print("Tomēr esi uzmanīgs, katrai izvēlei ir sekas, un ne visas izvēles beidzas veiksmīgi!\n")
    
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
        restart = input("Vai vēlies atsākt spēli? (Jā/Nē): ")
        if restart.lower() == "jā":
            start()
        else:
            print("Uz redzēšanos!")
            exit()

# Spēles noteikumu paskaidrojums
def noteikumi():
    print("------------------------------------------")
    print("Spēles noteikumi:")
    print("1. Tu izvēlies, kuru māju vēlies apzagt. Katram īpašniekam ir savi izaicinājumi un ceļi, kā iekļūt mājā.")
    print("2. Katru reizi, kad tu veic izvēli, tev būs jāizdara secīga izvēle, lai pārvarētu šķēršļus un iegūtu vērtīgas mantas.")
    print("3. Esi uzmanīgs, jo dažas izvēles var novest pie aizturēšanas vai slēptiem zaudējumiem.")
    print("4. Dažas izvēles var beigt spēli ar aizturēšanu, bet citas ļaus tev veiksmīgi aizbēgt ar mantām.")
    print("5. Katrs īpašnieks ir atšķirīgs, tāpēc izvēles būs dažādas katram scenārijam.\n")
    print("Galvenais ir pieņemt pareizās izvēles, lai iegūtu dārgumus un izvairītos no aizturēšanas!\n")
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
    print("\nTu piesit pie durvīm un saki, ka esi radinieks, kas atnesis palīdzību. Viņa tev uzticas un ielaiž iekšā.")
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
    print("Spēles beigas! Tevi aiztur policija.\n")

def nopecot_naudu():
    print("\nVecmāmiņa labprāt tev dod naudu, jo viņa nezin, ka tu esi zaglis. Tu aizbēdz ar naudu. Veiksmīgi!")
    print("Spēles beigas: Tu aizbēdz ar naudu.\n")

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
    print("Tu mēģini kāpt pa ārdurvīm, bet neturi līdzsvaru un nokrīti uz zemes! Spēle beigusies.")
    print("Spēles beigas: Tu nokriti un ievainojies.\n")

def caur_logu_bankieris():
    print("\nTu mēģini iekļūt mājā pa logu, bet baņķiera mājā ir sarežģītas drošības sistēmas. Tu izsit logu, bet tas aktivizē trauksmi!")
    print("Spēles beigas: Tu esi noķerts!\n")

def durvju_viltus_stasts():
    print("\nTu nolem izdomāt viltus stāstu, ka esi izsists un meklē palīdzību. Vecmāmiņa uzticas tev, bet viņa ir pārāk laipna.")
    print("Viņa iepazīstina tevi ar visiem saviem dārgumiem, bet tev nākas pazust no viņas mājas, jo viņa sauc policiju!")
    print("Spēles beigas! Tevi noķer!\n")

def durvju_stasts_bankierim():
    print("\nTu pie durvīm izdomā stāstu, ka esi piegādātājs. Baņķieris piekrīt tevi ielaist, bet viņš ir ļoti aizdomīgs.")
    print("Tevi noķer, kad tu mēģini apzagt viņu!")
    print("Spēles beigas! Tu esi noķerts!\n")

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
    print("\nTu skrien prom un izbēg no mājas, bet policija tevi izseko un noķer. Spēle beigusies!")
    
def samierinaties_ar_bankieri():
    print("\nBaņķieris piekrīt tev palīdzēt, bet viņa noslēptais aģents tevi noķer, un tu esi aizturēts. Spēle beigusies!\n")

# Kima Kardašiana
def kim_kardashian():
    print("\nTu izvēlējies apzagt Kimu Kardašianu. Viņas māja ir ļoti dārga un pilna ar luksusa priekšmetiem.")
    print("Bet viņai ir ļoti laba drošība un daudz kameras. Esi uzmanīgs!\n")
    
    print("Izvēles:\n")
    print("1. Mēģini iekļūt pa pagrabu.")
    print("2. Iekļūt pa galvenajām durvīm, izmantojot viltus stāstu.")
    print("3. Mēģini zvanīt pie durvīm un teikt, ka tev ir piegāde.\n")
    
    izvele = input("Izvēlies (1/2/3): ")
    
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
    print("\nTu mēģini ielauzties pa pagrabu, bet tur ir modernās drošības sistēmas. Tev izdodas iekļūt, bet trauksme tiek aktivizēta!")
    print("Spēles beigas: Tu esi noķerts apsargiem!\n")

def durvju_viltus_stasts_kim():
    print("\nTu mēģini iekļūt pa durvīm ar viltus stāstu, bet Kimas drošības personāls ir pārāk profesionāls un tevi noķer!")
    print("Spēles beigas: Tu esi noķerts!\n")

def zvans_durvīs():
    print("\nTu zvani pie durvīm un saki, ka tev ir piegāde, bet apsargi ir aizdomīgi un tu esi noķerts!")
    print("Spēles beigas: Tu esi noķerts!\n")
