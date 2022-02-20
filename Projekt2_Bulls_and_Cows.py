import random
import datetime


#Vytvoření tajného 4místného čísla (číslice musí být unikátní a nesmí začínat 0)

def fce_hadane_cislo():

    prvni_cislice = random.randint(1, 9)
    #print(prvni_cislice)

    while True:
        druhe_cislice = random.randint(0, 9)
        #print(druhe_cislice)
        if druhe_cislice != prvni_cislice:
            break

    while True:
        treti_cislice = random.randint(0, 9)
        #print(treti_cislice)
        if treti_cislice != prvni_cislice and treti_cislice != druhe_cislice:
            break

    while True:
        ctvrta_cislice = random.randint(0, 9)
        #print(ctvrta_cislice)
        if ctvrta_cislice != prvni_cislice and ctvrta_cislice != druhe_cislice and ctvrta_cislice != treti_cislice:
            break

    cislo_celkem = 1000 * prvni_cislice + 100 * druhe_cislice + 10 * treti_cislice + ctvrta_cislice

    return (cislo_celkem)


#Pozdravení uživatele a vypsání úvodního textu

def fce_uvod():

    print("Vítej ve hře!")
    print("-" * 50)

    print("Generuji 4 ciferné číslo (bez duplicit), uhodneš ho?")
    print("bull - uhodls jak číslo, tak jeho umístění")
    print("cow - uhodls pouze číslo, ale ne jeho umístění")
    print("-" * 50)


#Hádání čísla

def fce_hadani_cisla(hadane_cislo):

    pocet_pokusu = 0

    while True:
        tip = input("Zadej číslo:")
        #print(tip)
        pocet_pokusu += 1
        if tip.isnumeric() == False:
            print("Nezadals číslo!")
        elif len(tip) != 4:
            print("Číslo není 4 ciferné!")
        elif tip[0] == '0':
            print("Číslo začíná 0!")
        elif tip[0] == tip[1] or tip[0] == tip[2] or tip[0] == tip[3] or tip[1] == tip[2] or tip[1] == tip[3] or tip[2] == tip[3]:
            print("Číslo obsahuje duplicity!")
        else:
            if int(tip) == hadane_cislo:
                print("VYHRÁLS!")
                print("-" * 50)
                print(f"Počet pokusů:{pocet_pokusu}")
                break
            else:
                bull_pocet = 0
                cow_pocet = 0

                for pom in range(0, 4):
                    if tip[pom] == str(hadane_cislo)[pom]:
                        bull_pocet += 1

                if tip[0] == str(hadane_cislo)[1] or tip[0] == str(hadane_cislo)[2] or tip[0] == str(hadane_cislo)[3]:
                    cow_pocet += 1
                if tip[1] == str(hadane_cislo)[0] or tip[1] == str(hadane_cislo)[2] or tip[1] == str(hadane_cislo)[3]:
                    cow_pocet += 1
                if tip[2] == str(hadane_cislo)[0] or tip[2] == str(hadane_cislo)[1] or tip[2] == str(hadane_cislo)[3]:
                    cow_pocet += 1
                if tip[3] == str(hadane_cislo)[0] or tip[3] == str(hadane_cislo)[1] or tip[3] == str(hadane_cislo)[2]:
                    cow_pocet += 1

                if bull_pocet == 1:
                    if cow_pocet == 1:
                        print(f"{bull_pocet} bull, {cow_pocet} cow")
                    else:
                        print(f"{bull_pocet} bull, {cow_pocet} cows")
                else:
                    if cow_pocet == 1:
                        print(f"{bull_pocet} bulls, {cow_pocet} cow")
                    else:
                        print(f"{bull_pocet} bulls, {cow_pocet} cows")
        print("-" * 50)

#Vše dohromady

def fce_Bulls_and_cows():

    hadane_cislo = fce_hadane_cislo()

    #print(hadane_cislo)

    fce_uvod()

    cas_zacatek = datetime.datetime.now()

    fce_hadani_cisla(hadane_cislo)

    cas_konec = datetime.datetime.now()

    doba_hrani = cas_konec - cas_zacatek

    print(f"Celková doba hraní: {doba_hrani}")
    print(f"Celková doba hraní v sekundách: {doba_hrani.seconds}")

fce_Bulls_and_cows()