# Spēlētāja dzīvības
dzivibas = 3

def start():
    global dzivibas
    dzivibas = 3  # Atjaunot dzīvības spēles sākumā
    print("**********************************************")
    print("Laipni lūdzam spēlē 'Mājas apzagšana'!")
    print("Tu spēlēsi kā mājas zaglis, kura mērķis ir apzagt dažādas mājas, izvēloties no dažādiem īpašniekiem.")
    print("Katrs īpašnieks ir citādāks, un katrai mājai ir savi izaicinājumi un drošības riski.")
    print("Tavs uzdevums ir pieņemt pareizās izvēles un apzagt māju, izvairoties no aizdomīgiem cilvēkiem un trauksmes sistēmām.")
    print("Tomēr esi uzmanīgs, jo katra tavu izvēļu sekas var būt atšķirīgas, un ne visas izvēles beidzas veiksmīgi!")
    
    izvele = input("\nVai vēlies uzzināt spēles noteikumus un instrukcijas? (Jā/Nē)\nIzvēlies (Jā/Nē): ")

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
        print(f"Nederīga izvēle. Tev ir palikušas {dzivibas} dzīvības. Mēģini vēlreiz.")
    else:
        print("Tev beidzās dzīvības. Spēle beigusies!")
        exit()

# Spēles noteikumu paskaidrojums
def noteikumi():
    print("\n------------------------------------------")
    print("Spēles noteikumi:")
    print("1. Tu izvēlies, kuru māju tu vēlies apzagt. Katram īpašniekam ir savi izaicinājumi un ceļi, kā iekļūt mājā.")
    print("2. Katru reizi, kad tu veic izvēli, tev būs jāizdara secīga izvēle, lai pārvarētu šķēršļus un sagūstītu vērtīgos priekšmetus.")
    print("3. Tev ir jābūt uzmanīgam, jo dažas izvēles var novest pie aizturēšanas vai pat slēptiem zaudējumiem.")
    print("4. Dažas izvēles var izbeigt spēli ar aizturēšanu, citas ļaus tev veiksmīgi iznāk no mājas ar mantām.")
    print("5. Katrs īpašnieks ir atšķirīgs, tāpēc izvēles būs dažādas katram scenārijam.")
    print("\nSpēlē galvenais ir pieņemt pareizās izvēles, lai iegūtu dārgumus un izvairītos no aizturēšanas!")
    print("------------------------------------------")

    input("\nKad esi gatavs, spied jebkuru taustiņu, lai uzsāktu spēli...")
    pasakot_vairs_uzsakt()

def pasakot_vairs_uzsakt():
    izvele = input("1. Nabadzīga vecmāmiņa\n2. Baņķieris\n3. Slavenība - Kima Kardašiana\nIzvēlies (1/2/3): ")

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
    izvele = input("1. Iekļūt mājā pa logu.\n2. Iekļūt caur durvīm, izmantojot viltus stāstu.\n3. Mēģini piesist pie durvīm kā viesis.\nIzvēlies (1/2/3): ")
    
    if izvele == "1":
        caur_logu()
    elif izvele == "2":
        durvju_viltus_stasts()
    elif izvele == "3":
        viesis_stasts()
    else:
        zaude_dzivibu()
        vecmamina()

def caur_logu():
    print("\nTu mēģini ieiet pa logu, bet nejauši sabojā logu, un vecmāmiņa izsauc policiju. Beigas!")

def durvju_viltus_stasts():
    print("\nTu izmanto izdomātu stāstu un ielien mājā, taču vecmāmiņa ir uzmanīga un izsauc palīdzību. Beigas!")

def viesis_stasts():
    izvele = input("1. Mēģini apzagt viņu, kamēr viņa ir prom.\n2. Pajautā, vai viņa var tev dot naudu.\nIzvēlies (1/2): ")

    if izvele == "1":
        apzagt_vecmaminu()
    elif izvele == "2":
        nopecot_naudu()
    else:
        zaude_dzivibu()
        viesis_stasts()

def apzagt_vecmaminu():
    print("\nTu apzagji vecmāmiņu, bet viņa sāk kliegt un piezvana policijai. Tevi noķer!")

def nopecot_naudu():
    print("\nVecmāmiņa labprāt tev dod naudu, nezinot tavu patieso nodomu. Tu veiksmīgi aizbēdz ar naudu!")

# Baņķieris
def bankieris():
    izvele = input("1. Iekļūt mājā pa durvīm, izmantojot izdomātu stāstu.\n2. Iekļūt mājā pa logu.\n3. Mēģini apzagt viņu, kamēr viņš ir prom.\nIzvēlies (1/2/3): ")
    
    if izvele == "1":
        durvju_stasts_bankierim()
    elif izvele == "2":
        caur_logu_bankieris()
    elif izvele == "3":
        apzagt_bankieri()
    else:
        zaude_dzivibu()
        bankieris()

def caur_logu_bankieris():
    print("\nTu mēģini iekļūt caur logu, taču aktivizē trauksmes sistēmu. Tevi aiztur!")

def apzagt_bankieri():
    print("\nTu mēģini apzagt baņķieri, taču viņš aktivizē trauksmes pogu. Tevi noķer drošība!")

def durvju_stasts_bankierim():
    print("\nTu mēģini iekļūt mājā, izmantojot stāstu, bet baņķieris zvana apsargam. Beigas!")

# Kima Kardašiana
def kim_kardashian():
    izvele = input("1. Pārliecinies, vai viņas mājā nav drošības kameru.\n2. Mēģini izsist durvis un iekļūt caur ieeju.\n3. Izmanto viltus identitāti un piezvani viņai.\nIzvēlies (1/2/3): ")

    if izvele == "1":
        kameru_pārbaude()
    elif izvele == "2":
        caur_durvim_kim()
    elif izvele == "3":
        viltus_identitate()
    else:
        zaude_dzivibu()
        kim_kardashian()

def kameru_pārbaude():
    print("\nTu mēģini apiet kameras, bet tās aktivizē trauksmes signālu. Beigas!")

def caur_durvim_kim():
    print("\nTu mēģini izsist durvis, bet tās ir stipras, un trauksmes sistēma tiek iedarbināta. Tevi aiztur policija!")

def viltus_identitate():
    print("\nTu zvani Kimai, bet viņa paziņo drošības firmai. Tevi noķer!")
    
# Spēles sākums
start()

