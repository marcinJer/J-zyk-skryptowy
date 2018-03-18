while True:
    x = input("Wybierz dzialanie: \n1 - Dodawanie \n2 - Odejmowanie \n3 - Mnozenie\n4 - Dzielenie\n0 - Koniec")
    x = int(x)

    if x == 1:
        a = int(input("Podaj 1 liczbe: \n"))
        b = int(input("Podaj 2 liczbe: \n"))
        print(a+b)
    elif x == 2:
        a = int(input("Podaj 1 liczbe: \n"))
        b = int(input("Podaj 2 liczbe: \n"))
        print(a-b)
    elif x == 3:
        a = int(input("Podaj 1 liczbe: \n"))
        b = int(input("Podaj 2 liczbe: \n"))
        print(a*b)
    elif x == 4:
        a = int(input("Podaj 1 liczbe: \n"))
        b = int(input("Podaj 2 liczbe: \n"))
        print(a/b)
    elif x == 0:
        break
