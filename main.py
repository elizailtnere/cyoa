def start():
    print("Tu esi sagatavojies apzagt māju. Pirms sākt, tev jāizvēlas, kuru māju tu gribēsi apzagt.")
    print("Izvēlies, kuru mājas īpašnieku tu vēlies apzagt:")
    
    izvele = input("1. Nabadzīga vecmāmiņa\n2. Baņķieris\n3. Slavenība - Kima Kardašiana\nIzvēlies (1/2/3): ")

    if izvele == "1":
        vecmamina()
    elif izvele == "2":
        bankieris()
    elif izvele == "3":
        kim_kardashian()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        start()

# Nabadzīga vecmāmiņa
def vecmamina():
    print("\nTu izvēlējies apzagt nabadzīgu vecmāmiņu. Māja ir maza un veca, bet vecmāmiņa ir ļoti laipna un aizsargāta.")
    izvele = input("1. Iekļūt mājā pa logu.\n2. Iekļūt caur durvīm, izmantojot viltus stāstu.\n3. Mēģini piesist pie durvīm kā viesis.\nIzvēlies (1/2/3): ")
    
    if izvele == "1":
        caur_logu()
    elif izvele == "2":
        durvju_viltus_stasts()
    elif izvele == "3":
        viesis_stasts()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        vecmamina()

def viesis_stasts():
    print("\nTu piesit pie durvīm un saki, ka esi radinieks, kas atnesis vecmāmiņai palīdzību. Viņa tev uzticas un ielaiž iekšā.")
    izvele = input("1. Mēģini apzagt viņu, kamēr viņa ir prom.\n2. Pajautā, vai viņa var tev dot naudu.\nIzvēlies (1/2): ")

    if izvele == "1":
        apzagt_vecmaminu()
    elif izvele == "2":
        nopecot_naudu()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        viesis_stasts()

def apzagt_vecmaminu():
    print("\nTu apzagji vecmāmiņu, bet viņa sāk kliegt un piezvana policijai. Tevi noķer!")
    print("Beigas! Tevi aiztur policija.")

def nopecot_naudu():
    print("\nVecmāmiņa labprāt tev dod naudu, jo viņa nezin, ka tu esi zaglis. Tu aizbrauc ar naudu un veic bēgšanu. Veiksmīgi!")
    print("Beigas: Tu aizbēdz ar naudu.")

# Baņķieris
def bankieris():
    print("\nTu izvēlējies apzagt baņķieri. Viņš dzīvo dārgā villā, un viņa māja ir pilna ar vērtīgiem priekšmetiem.")
    izvele = input("1. Iekļūt mājā pa durvīm, izmantojot izdomātu stāstu.\n2. Iekļūt mājā pa logu.\n3. Mēģini apzagt viņu, kamēr viņš ir prom.\nIzvēlies (1/2/3): ")
    
    if izvele == "1":
        durvju_stasts_bankierim()
    elif izvele == "2":
        caur_logu_bankieris()
    elif izvele == "3":
        apzagt_bankieri()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        bankieris()

def apzagt_bankieri():
    print("\nBaņķieris ir ļoti aizdomīgs un, kad tu mēģini apzagt viņu, viņš piespiež nospiest trauksmes pogu!")
    izvele = input("1. Mēģini aizbēgt ātri.\n2. Mēģini samierināt baņķieri, apgalvojot, ka tev vajag naudu.\nIzvēlies (1/2): ")
    
    if izvele == "1":
        aizbēgt_no_bankiera()
    elif izvele == "2":
        samierinaties_ar_bankieri()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        apzagt_bankieri()

def aizbēgt_no_bankiera():
    print("\nTu bēdz un izkļūsti no mājas, bet policija tevi izseko un noķer. Beigas!")
    
def samierinaties_ar_bankieri():
    print("\nBaņķieris piekrīt tev palīdzēt, bet viņam ir noslēpumaina aģenta palīdzība, un tu esi noķerts. Beigas!")

def durvju_stasts_bankierim():
    print("\nTu pieiet pie durvīm un piedāvā sevi kā palīdzību. Baņķieris ir aizdomīgs un zvana apsargam, kas pārbauda tavu identitāti. Tevi noķer.")
    print("Beigas! Tevi aiztur apsargs.")

def caur_logu_bankieris():
    print("\nTu iznāc pa logu un ieej mājā, bet kad sāk meklēt dārgumus, tu nejauši izsist trauksmes sistēmu!")
    izvele = input("1. Ātri paņem dārgumus un bēdz.\n2. Paliec mierīgs un mēģini izsist signālu.\nIzvēlies (1/2): ")
    
    if izvele == "1":
        aizbēgt_ar_dargumiem()
    elif izvele == "2":
        izmēģini_izsist_signālu()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        caur_logu_bankieris()

def aizbēgt_ar_dargumiem():
    print("\nTu paķeri dārgumus un bēdz, bet policija ātri ierodas. Tevi aiztur. Beigas!")
    
def izmēģini_izsist_signālu():
    print("\nTu mēģini izsist trauksmes signālu un pārtraukt to. Diemžēl tas neveicas, un tu esi noķerts, kad ierodas drošības firma.")
    print("Beigas! Tevi aiztur.")

# Kima Kardašiana
def kim_kardashian():
    print("\nTu izvēlējies apzagt Kimu Kardašianu! Viņas māja ir pilna ar dārgām rotaslietām, dizaineru apģērbiem un vēl daudz ko citu.")
    izvele = input("1. Pārliecinies, vai viņas mājā nav drošības kameru.\n2. Mēģini izsist durvis un iekļūt caur ieeju.\n3. Izmanto viltus identitāti un piezvani viņai.\nIzvēlies (1/2/3): ")

    if izvele == "1":
        kameru_pārbaude()
    elif izvele == "2":
        caur_durvim_kim()
    elif izvele == "3":
        viltus_identitate()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        kim_kardashian()

def kameru_pārbaude():
    print("\nTu pārbaudi kameru sistēmu, taču tā ir ļoti labi paslēpta, un tu nejauši iedarini trauksmes sistēmu.")
    izvele = input("1. Bēdz no mājas ar dārgumiem.\n2. Paliec, cerot, ka Kima nenonāks ātrāk nekā policija.\nIzvēlies (1/2): ")
    
    if izvele == "1":
        aizbēgt_ar_dargumiem()
    elif izvele == "2":
        noķerts_ar_polici()
    else:
        print("Nederīga izvēle. Mēģini vēlreiz.")
        kameru_pārbaude()

def caur_durvim_kim():
    print("\nTu mēģini izsist durvis, taču tās ir ļoti stipri slēgtas, un trauksmes signāls tiek aktivizēts. Policija ierodas un noķer tevi.")
    print("Beigas! Tevi aiztur.")

def viltus_identitate():
    print("\nTu izmanto viltus identitāti un zvani Kima Kardašianai, bet viņa ir ļoti uzmanīga un uzreiz paziņo par tevi drošības uzņēmumam.")
    print("Beigas! Tevi aiztur drošības firma.")

def noķerts_ar_polici():
    print("\nKima ir mājās, un viņa ļoti ātri paziņo drošības firmai. Tu tiek aizturēts.")
    print("Beigas!")
    
# Spēles sākums
start()
