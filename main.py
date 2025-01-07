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
        atkārtot_spelet()
    else:
        print("Tev beigušās visas dzīvības! Tagad tu nonāc tiesā.\n")
        tiesa()

def tiesa():
    print("\nTu esi nonācis tiesā. Tagad tev ir iespēja sevi aizstāvēt!")
    print("Izvēles:\n")
    print("1. Melot un teikt, ka esi nevainīgs.")
    print("2. Aizbildināties ar sliktiem apstākļiem (piemēram, ka tev bija jārūpējas par ģimeni).")
    print("3. Atzīt savu vainu un lūgt žēlastību.\n")

    izvele = input("Izvēlies (1/2/3): ")

    if izvele == "1":
        melot_tiesa()
    elif izvele == "2":
        aizbildinaties_tiesa()
    elif izvele == "3":
        atzit_vainu_tiesa()
    else:
        print("Tu neko nesaki, un tiesnesis piespriež tev bargu sodu!")
        print("Spēles beigas: Tu esi notiesāts un aizsūtīts uz cietumu uz 10 gadiem.\n")
        exit()

def melot_tiesa():
    print("\nTu mēģini melot, bet pierādījumi ir pārāk spēcīgi pret tevi.")
    print("Tiesnesis tevi atzīst par vainīgu un piespriež bargu sodu!")
    print("Spēles beigas: Tu esi notiesāts un aizsūtīts uz cietumu.\n")
    exit()

def aizbildinaties_tiesa():
    print("\nTu stāsti tiesnesim par saviem smagajiem apstākļiem. Viņš izrāda sapratni un piespriež maigāku sodu.")
    print("Tu saņem nosacītu sodu un esi brīvībā, bet tev ir jābūt piesardzīgam nākotnē.")
    print("Spēles beigas: Tu izvairies no cietuma, bet sabiedrība tevi uzrauga.\n")
    exit()

def atzit_vainu_tiesa():
    print("\nTu godīgi atzīsti savu vainu un izrādi nožēlu. Tiesnesis tevi žēlo un piespriež tikai sabiedriskos darbus.")
    print("Spēles beigas: Tu izvairies no cietuma un gūsti iespēju laboties!\n")
    exit()

def atkārtot_spelet():
    izvele = input("Vai vēlies mēģināt vēlreiz? (Jā/Nē): ")
    if izvele.lower() == "jā":
        global dzivibas
        dzivibas = 3  # Atjauno dzīvības
        pasakot_vairs_uzsakt()
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
    print("3. Mēģini apzagt viņa automašīnu.\n")
    
    izvele = input("Izvēlies (1/2/3): ")
    
    if izvele == "1":
        bankieris_durvis()
    elif izvele == "2":
        bankieris_logu()
    elif izvele == "3":
        bankieris_automasina()
    else:
        zaude_dzivibu()
        bankieris()

def bankieris_durvis():
    print("\nTu izvēlies pieiet pie durvīm un ieiet iekšā, izmantojot izdomātu stāstu. Baņķieris tev uzticas un ļauj ienākt.")
    print("Iekļūsti mājā un paņem dārgumus.\n")
    print("Veiksmīgi apzagts!\n")
    spēlēt_vēlreiz()

def bankieris_logu():
    print("\nTu mēģini iekļūt pa logu, bet tas ir pārāk sarežģīti. Baņķieris tevi noķer!")
    zaude_dzivibu()

def bankieris_automasina():
    print("\nTu izvēlies apzagt viņa automašīnu. Diemžēl, tas ir pārāk riskanti, un tevi noķer.")
    zaude_dzivibu()

# Kima Kardašiana
def kim_kardashian():
    print("\nTu izvēlējies apzagt Kimu Kardašianu. Viņai ir pilns mansions ar daudzām dārgām mantām.")
    print("\nIzvēles:\n")
    print("1. Iekļūt mājā, izmantojot kādu no viņas pakalpotājiem.")
    print("2. Iekļūt mājā, izmantojot viltus stāstu.\n")

    izvele = input("Izvēlies (1/2): ")

    if izvele == "1":
        kim_pakalpotajs()
    elif izvele == "2":
        kim_viltus_stasts()
    else:
        zaude_dzivibu()
        kim_kardashian()

def kim_pakalpotajs():
    print("\nTu izmanto pakalpotāju un izkļūsti ar vērtīgām mantām. Veiksmīgi!\n")
    spēlēt_vēlreiz()

def kim_viltus_stasts():
    print("\nTu piezvani pie durvīm un izdomā stāstu, bet Kim neuzticas un zvana drošības dienestam. Tu tiek aizturēts!\n")
    zaude_dzivibu()

# **Trūkstošās funkcijas, kas tika norādītas**:

def caur_logu():
    print("\nTu mēģini iekļūt mājā pa logu, bet durvis ir pārāk aizsargātas. Tu izsist logu un ieej iekšā.")
    print("Tev izdodas iegūt dārgumus un aizbēgt bez aizķeršanās.\n")
    spēlēt_vēlreiz()

def durvju_viltus_stasts():
    print("\nTu pieklauvēji pie durvīm un saki, ka esi radinieks, kas atnesis vecmāmiņai zāles. Viņa tev uzticas un ielaiž iekšā.")
    print("Tev izdodas apzagt viņu, un tu bēdz projām.\n")
    spēlēt_vēlreiz()

def spēlēt_vēlreiz():
    izvele = input("Vai vēlies spēlēt vēlreiz? (Jā/Nē): ")
    if izvele.lower() == "jā":
        start()
    else:
        print("Paldies, ka spēlēji! Spēle beigusies.\n")
        exit()

# Spēles sākums
start()
