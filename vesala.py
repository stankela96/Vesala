import _random
import random
reci = ["sara","marija","nevena","nikola","veljko","david"]
zadataRec = random.choice(reci)
brojSlova = len(zadataRec)
brojGresaka = 0
odgovor = ["_ "]*brojSlova
print(brojSlova)

while(brojGresaka < 7) :

    nadjenoSlovo = False
    print(''.join(odgovor) + "\n" )
    slovo = input("Unesi slovo : ")
    for i in range(0,brojSlova) :
        if(zadataRec[i] == slovo) :
            odgovor[i] = (slovo + " ")
            nadjenoSlovo = True

    if(nadjenoSlovo == False) :
        brojGresaka += 1
        print("\n" +"Imate jos " + str(7-brojGresaka) + " pokusaja" + "\n")

        if(brojGresaka == 1):
            print("<" + "\n")

        if (brojGresaka == 2):
            print("<O" + "\n")

        if (brojGresaka == 3):
            print("<O-" + "\n")

        if (brojGresaka == 4):
            print("<O->" + "\n")

        if (brojGresaka == 5):
            print("<O->|" + "\n")

        if (brojGresaka == 6):
            print("<O->|-" + "\n")

        if (brojGresaka == 7):
            print("<O->|-<" + "   zadata rec je --> " + zadataRec + "\n")


    if "_ " not in odgovor :
        print(''.join(odgovor))
        print("CESTITAMO")
        break