from math import pi, sin, radians, tan, log, cos



def zemepisne_delky():
    x = radians(i) * polomer / meritko
    X = round(x,1)
    if x > 100 or x < -100:
        X_souradnice.append("-")
    else:
        X_souradnice.append(X)


def lambertovo_sirky():
    y = polomer * sin(radians(a)) / meritko
    Y = round (y,1)
    if y > 100 or y < -100:
        Y_souradnice.append("-")
    else:
        Y_souradnice.append(Y)


def marinovo_sirky():
    y = 6371.11 * radians(a) / meritko
    Y = round(y, 1)
    if y > 100 or y < -100:
        Y_souradnice.append("-")
    else:
        Y_souradnice.append(Y)


def braunovo_sirky():
    y = 2 * 6371.11 * tan((radians(a) / 2)) / meritko
    Y = round(y, 1)
    if y > 100 or y < -100:
        Y_souradnice.append("-")
    else:
        Y_souradnice.append(Y)


def mercatorovo_sirky():
    y = 6371.11 * log(cos(radians((90 - a) / 2)) / sin(radians((90 - a) / 2))) / meritko
    Y = round(y, 1)
    if y > 100 or y < -100:
        Y_souradnice.append("-")
    else:
        Y_souradnice.append(Y)


print ("Vitejte v apliakci pro vypocet pruseciku zemepisne site")
for k in range (1000):
    ver = input("Vyberte valcove zobrazeni\n\n Zadejte pismeno v uvozovkach pro vyber zobrazeni \n\n 'l' pro Lambertovo zobrazeni \n 'm' pro Marinovo zobrazeni \n 'b' pro Braunovo zobrazeni \n 'e' pro Mercatorovo zobrazeni\n\n")
    if ver == "l" or ver == "m" or ver == "b" or ver == "e":
        print("Dobre zadano\n")
        break
    else:
        print("Chybne zadani, opakujte zadani")
        continue

if ver == "l":
    print("Vybral jste Lambertovo zobrazeni \n\n")
elif ver == "m":
    print("Vybral jste Marinovo zobrazeni \n\n")
elif ver == "b":
    print("Vybral jste Braunovo zobrazeni \n\n")
elif ver == "e":
    print("Vybral jste Mercatorovo zobrazeni \n\n")

mer = float(input("Zadejte meritko ve formatu 1:50000 = 50000"))
meritko = mer / 100000

polomer = float(input("Zadejte polomer zeme v kilometrech"))

Zemepisne_delky = []
X_souradnice = []
i = 0

for i in range (37):
    i = 10 * i - 180
    Zemepisne_delky.append(i)
    zemepisne_delky()

Zemepisne_sirky = []
Y_souradnice = []
a = 0


for a in range (19):
    a = 10 * a - 90
    Zemepisne_sirky.append(a)
    if ver == "l":
        lambertovo_sirky()
    elif ver == "m":
        marinovo_sirky()
    elif ver == "b":
        braunovo_sirky()
    elif ver == "e":
        if a == 90 or a == -90:
            Y_souradnice.append("-")
        else:
            mercatorovo_sirky()


#print ("Stupne zemepisne delky: " + str(Zemepisne_delky))
print ("Poledniky: " + str(X_souradnice) + "\n")
#print ("Stupne zemepisne sirky: " + str(Zemepisne_sirky))
print ("Rovnobezky: " + str(Y_souradnice) + "\n")
