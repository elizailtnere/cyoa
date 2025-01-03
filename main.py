# Spēlētāja dzīvības
dzivibas = 3

def start():
    global dzivibas
    dzivibas = 3  # Atjauno dzīvības spēles sākumā
    print("**********************************************")
    print("Laipni lūdzam spēlē 'Blēdīgais Jānis'!")
    print("Tu domā, ka esi Mārvs no Viens pats mājās (tu neesi pat tik meistarīgs kā viņš, bet par to mēs aizmirstam), tādēļ vēlies apzagt dažādas mājas un tev ir vairākas iespējas ko apzagt.")
    print("Katrs īpašnieks ir citādāks, un katrai mājai ir savi knifiņi un riski.")
    print("Tavs uzdevums ir pieņemt pareizās izvēles un apzagt māju, izvairoties no aizdomīgiem cilvēkiem un drošības sistēmām.")
    print("Tomēr esi uzmanīgs, jo katra tavu izvēļu sekas var būt atšķirīgas, un ne visas izvēles beidzas veiksmīgi. Neesi idiots!\n")
    
    izvele = input("Vai vēlies zināt spēles noteikumus un instrukcijas? (Jā/Nē)\n\nIzvēlies (Jā/Nē): ")

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
        print(f"Nepareiza izvēle. Tev ir palikušas {dzivibas} dzīvības. Mēģini vēlreiz.\n")
        atkārtot_spelet()  # Piedāvāt spēlētājam vēlreiz spēlēt
    else:
        print("Tevi pieķēra. Spēle beigusies :(((((((!\n")
        exit()

def atkārtot_spelet():
    izvele = input("Vai vēlies mēģināt vēlreiz? (Jā/Nē): ")
    if izvele.lower() == "jā":
        dzivibas = 3  # Atjauno dzīvības
        pasakot_vairs_uzsakt()  # Turpina spēli no vietas, kur apstājās
    else:
        print("Paldies, ka spēlēji! Spēle beigusies.\n")
        exit()

# Spēles noteikumu paskaidrojums
def noteikumi():
    print("------------------------------------------")
    print("Spēles noteikumi:")
    print("1. Tu izvēlies, kuru māju tu vēlies apzagt. Katram īpašniekam ir savi izaicinājumi un ceļi, kā iekļūt mājā.")
    print("2. Katru reizi, kad tu veic izvēli, tev būs jāizdara secīga izvēle, lai pārvarētu šķēršļus un nozagtu vērtīgos priekšmetus.")
    print("3. Tev ir jābūt uzmanīgam, jo dažas izvēles var novest pie aizturēšanas.")
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
    print("2. Iekļūt caur durvīm, izmantojot viltus stāstu jeb melojot viņai.")
    print("3. Mēģini pieklauvēt pie durvīm kā viesis.\n")
    
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
    print("\nTu pieklauvēji pie durvīm un saki, ka esi radinieks, kas atnesis vecmāmiņai zāles. Viņa tev uzticas un ielaiž iekšā.")
    print("\nIzvēles:\n")
    print("1. Mēģini apzagt viņu, kamēr viņa ir prom.")
    print("2. Pajautā, vai viņa var tev iedot naudu.\n")
    
    izvele = input("Izvēlies (1/2): ")

    if izvele == "1":
        apzagt_vecmaminu()
    elif izvele == "2":
        dabut_naudu()
    else:
        zaude_dzivibu()
        viesis_stasts()

def apzagt_vecmaminu():
    print("\nTu apzagi vecmāmiņu, bet viņa sāk kliegt un piezvana policijai. Tevi noķer!")
    print("Beigas! Tevi aiztur policija.\n")
    zaude_dzivibu()

def dabut_naudu():
    print("\nVecmāmiņa labprāt tev iedod naudu, jo viņa nezin, ka tu esi zaglis. Tu aizbrauc ar naudu un veic bēgšanu. Veiksmīgi!")
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
    print("\nTu izlēmi iekļūt mājā pa logu Tā ir sarežģīta izvēle, jo logs ir augstu, un tu vari viegli nokrist.")
    print("Tu mēģini kāpt, bet neturi līdzsvaru, un nokrīti uz zemes! Spēle beigusies.")
    print("Beigas! Tu nokriti un esi nāvīgi ievainots.\n")
    zaude_dzivibu()

def caur_logu_bankieris():
    print("\nTu mēģini iekļūt mājā pa logu, bet baņķiera mājā ir sarežģītas drošības sistēmas. Tu izsit logu, bet tas aktivizē trauksmi!")
    print("Beigas! Tu esi noķerts!\n")
    zaude_dzivibu()

def durvju_viltus_stasts():
    print("\nTu nolem izdomāt viltus stāstu, ka esi ievainots un meklē palīdzību. Vecmāmiņa uzticas tev, viņa ir pārāk laipna.")
    print("Viņa iepazīstina tevi ar visiem saviem dārgumiem, bet tev nākas pazust no viņas mājas, jo viņa izsauc policiju!")
    print("Beigas! Tevi noķer!\n")
    zaude_dzivibu()

def durvju_stasts_bankierim():
    print("\nTu pie durvīm izdomā stāstu, ka esi piegādātājs. Baņķieris piekrīt tevi ielaist, bet viņš ir ļoti aizdomīgs.")
    print("Tevi noķer, kad tu mēģini apzagt viņu!")
    print("Beigas! Tu esi noķerts!\n")
    zaude_dzivibu()

def apzagt_bankieri():
    print("\nBaņķieris ir ļoti aizdomīgs un, kad tu mēģini apzagt viņu, viņš piespiež trauksmes pogu!")
    print("\nIzvēles:\n")
    print("1. Mēģini aizbēgt ātri.")
    print("2. Mēģini aprunāties ar baņķieri, apgalvojot, ka tev ļoti ļoti vajag naudu, lai izārstētu savam kaķim vēzi.\n")
    
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
    zaude_dzivibu()

def samierinaties_ar_bankieri():
    print("\nBaņķieris piekrīt tev palīdzēt, bet viņam ir noslēpumaina aģenta palīdzība, un tu esi noķerts. Beigas!\n")
    zaude_dzivibu()

def kim_kardashian():
    print("\nTu izvēlējies apzagt Kimu Kardašianu. Viņas māja ir ļoti dārga un pilna ar luksusa mantām u citiem nevajadzīgiem sūdiem.")
    print("Bet viņai ir ļoti laba drošība un daudz kameras. Esi uzmanīgs!\n")
    
    print("Izvēles:\n")
    print("1. Mēģini iekļūt pa pagrabu.")
    print("2. Iekļūt pa galvenajām durvīm, izmantojot viltus stāstu.")
    print("3. Mēģini zvanīt pie durvīm un teikt, ka tu esi Bolt kurjers.\n")
    
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
    print("Spēles beigas: Tevi noķēra apsargi!\n")
    zaude_dzivibu()

def durvju_viltus_stasts_kim():
    print("\nTu mēģini iekļūt pa durvīm ar viltus stāstu, bet Kimas drošības personāls ir pārāk profesionāls un tevi noķer!")
    print("Spēles beigas: Tu esi noķerts!\n")
    zaude_dzivibu()

def zvans_durvīs():
    print("\nTu zvani pie durvīm un saki, ka tev ir piegāde, bet apsargi ir aizdomīgi un tu esi noķerts!")
    print("Spēles beigas: Tu esi noķerts!\n")
    zaude_dzivibu()

# Spēles sākums
start()

