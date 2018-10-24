def zaklad_zobrazeni (mer,verze):
    "1 = lambert 2 = Marinovo 3 = Braunovo 4 = Mercatorovo"
    from math import pi, sin, radians, tan, log, cos
    print ("Vitejte v apliakci pro vypocet pruseciku zemepisne site")
    verz = input("Vyberte kuzelove zobrazeni (1,2,3,4) \n\n 1 = Lambertovo zobrazeni \n 2 = Marinovo zobrazeni \n 3 = Braunovo zobrazeni \n 4 = Mercatorovo zobrazeni")
    verze = float(verz)
    x = []
    Z = []
    i = 0
    meritko = mer / 100000
    for i in range (37):
        i = 10 * i - 180
        x.append(i)
        z = radians(i) * 6371.11 / meritko
        Z.append(z)
    print (x)
    print (Z)
    y = []
    U = []
    a = 0
    for a in range (19):
        a = 10 * a - 90
        y.append(a)
        if verze == 1:
            u = 6371.11 * sin(radians(a)) / meritko
            U.append(u)
        elif verze == 2:
            u = 6371.11 * radians(a) / meritko
            U.append(u)
        elif verze == 3:
            u = 2*6371.11 * tan((radians(a)/2)) / meritko
            U.append(u)
        elif verze == 4:
            u = 6371.11 * log((cos(radians(a))/sin(radians((90-a)/2)))) / meritko
            U.append(u)

    print (y)
    print (U)


zaklad_zobrazeni(30000000,4)