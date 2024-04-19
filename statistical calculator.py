#Kalkulator statystyczny

# Zdefiniowana operacja która oblicza średnią arytmetyczną oraz zwraca jej wynik
def SA():
    wynik=sum(zbior)/len(zbior)      
    return print(f"Średnia arytmetyczna: {wynik}")

# Zdefiniowana operacja która oblicza średnią geometryczną oraz zwraca jej wynik
def SG():
    wynik=sum(zbior)**(1/len(zbior))
    return print(f"Średnia geometryczna: {wynik}")

# Zdefiniowana operacja która rozpoznaje czy liczba elementów w liście jest pażysta czy
# nie parzysta, a następnie oblicza i zwraca medianę
def ME():
    zbiorME = zbior
    zbiorME.sort()
    if (len(zbiorME) % 2) == 0:
        pozycja1=len(zbiorME)/2 - 1
        pozycja2=len(zbiorME)/2
        wynik=(zbior[int(pozycja1)] + zbior[int(pozycja2)])/2
    else:
        pozycja1=len(zbiorME)/2 - 1/2
        pozycja2=len(zbiorME)-pozycja1-1
        wynik=zbiorME[int(pozycja2)]
       
    return print(f"Mediana: {wynik}")

# Zdefiniowana operacja która za pomocą pętli for sprawdza który element występuje
# w liście najczęściej oraz zwraca ten element jako wynik czyli zwraca modę
def MO():
    zlicz= dict()
    for i in range(len(zbior)):
        if zbior[i] in zlicz:
            zlicz[zbior[i]] += 1
        else:
            zlicz[zbior[i]] = 1
            
    maks = -1
    wynik = -1
    for (a, b) in zlicz.items():
        if b > maks:
            wynik = a
            maks = b
    
    return print(f"Moda: {wynik}")

# Zdefiniowana operacja która oblicza średnią i rozbieżność, a następnie oblicza odchylenie
# standardowe, wszystko zgodnie ze wzorem na odchylenie standardowe
def OS():
    srednia = sum(zbior)/len(zbior)      
    roz = sum([((x - srednia) ** 2) for x in zbior]) / len(zbior) 
    wynik = roz ** 0.5
    return print(f"Odchylenie standardowe: {wynik}")

# Zdefiniowana operacja która oblicza sume zbiorów, kwadrata 1 i 2 zbioru, a następnie wylicza współczynnik korelacji
def WK():
    i = 0
    o = 0
    n = len(zbior)
    suma_zbiorow = 0    
    kwadZbior = 0
    kwadZbiorWspol = 0
    
    print("Utwórz drugi zbiór liczb o takiej samej ilości elementów co pierwszy zbiór!")
    
    while (o < n):                    
            z=float(input("Podaj liczbę: "))
            zbiorWspol.append(z)
            print(f"Zbiór pierwszy {zbior}")
            print(f"Zbiór drugi {zbiorWspol}")
            o = o + 1
            
    while (i < n):
        
        suma_zbiorow = suma_zbiorow + zbior[i] * zbiorWspol[i]
        kwadZbior = kwadZbior + zbior[i] * zbior[i]
        kwadZbiorWspol = kwadZbiorWspol + zbiorWspol[i] * zbiorWspol[i]
        i = i + 1
    
    suma_zbior = sum(zbior)
    suma_zbiorWspol = sum(zbiorWspol)
    wynik = (n * suma_zbiorow - suma_zbior * suma_zbiorWspol)/(((n * kwadZbior - suma_zbior * suma_zbior)*(n * kwadZbiorWspol - suma_zbiorWspol * suma_zbiorWspol))**(1/2))
    
    while (r < len(zbiorWspol)):
        zbiorWspol.pop(len(zbiorWspol) - 1)
        
    return print(f"Współczynnik korelacji: {wynik}")

def WRL():
    o = 0
    n = len(zbior)
    zbiorDane = []
    
    print("Utwórz drugi zbiór liczb o takiej samej ilości elementów co pierwszy zbiór!")
    
    while (o < n):                    
            z=float(input("Podaj liczbę: "))
            zbiorWspol.append(z)
            print(f"Zbiór pierwszy {zbior}")
            print(f"Zbiór drugi {zbiorWspol}")
            zbiorDane.append((zbior[o], zbiorWspol[o]))
            o = o + 1
   
    suma_x = sum(x for x, y in zbiorDane)     
    suma_y = sum(y for x, y in zbiorDane)
    suma_xy = sum(x*y for x, y in zbiorDane)
    suma_x2 = sum(x**2 for x, y in zbiorDane)
    
    wynikA = (n * suma_xy - suma_x * suma_y) / (n * suma_x2 - suma_x**2)
    wynikB = (suma_y - wynikA * suma_x) / n
            
    while (r < len(zbiorWspol)):
        zbiorWspol.pop(len(zbiorWspol) - 1)
        zbiorDane.pop(len(zbiorDane) - 1)
        
    return print(f"Współczynnik regresji liniowej: {wynikA}, {wynikB}")
        


zbior=[]        #Zbiór liczb na których będą wykonywane działania
zbiorWspol=[]   #Drugi zbiór liczb potrzebny do obliczenia Współczynnika korelacji oraz Współczynnika regresji liniowej
war=0           #Zmienna która musi spełniać warunki pętli "while" aby ta mogła działać. Zmiana wartości na inną niż 0 spowoduje zakończenie pętli
r = 0
x="NIE" 
y="NIE"         

print("Witaj w kalkulatorze statystycznym")

#Na początku pętli zmienna x = "NIE" dzięki czemu pierwsza operacja która jest wykonywana to pojawienie się Menu z którego
#wybieramy jaką operację chcemy wykonać. Jesli operacja jest inna niż "Zakończenie programu" to użytkownik zostanie
#poproszony o utworzenie zbioru danych, a następnie na zbiorze zostanie wykonana wybrana przez nas operacja.
#Po operacji zbiór zostaje wyczyszczony, dzięki czemu możemy wykonać kolejną operację na zupełnie innych liczbach.
#W wypadku wybrania operacji wyliczenia Współczynnika korelacji lub Współczynnika regresji liniowej, po wprowadzeniu
#zbioru liczb, użytkownik zostanie poproszony o wprowadzenie drugiego zbioru o tej samej liczbie elementów.
#Po wykonaniu operacji obydwa zbiory są czyszczone co pozwala na wykonanie operacji ponownie na zupełnie innych liczbach
#Jesli użytkownik wprowadzi błędną komendę, to zostanie o tym poinformowany i odesłany do Menu
while (war == 0):                
    if(x == "NIE"):
        while (r < len(zbior)):
            zbior.pop(len(zbior) - 1)
            
        while y == "NIE":    
            print("Jakie działanie chcesz wykonać?")
            print("| SA - Średnia arytmetyczna | SG - Średnia geometryczna | ME - Mediana | MO - Moda |")
            print("| OS - Odchylenie standardowe | WK - Współczynnik korelacji | WRL - Współczynnik regresji liniowej |")
            print("| K - Zakończ program |")
            x=input()
            x=x.upper()
            if(x == "SA" or x == "SG" or x == "ME" or x == "MO" or x == "OS" or x == "WK" or x == "WRL"):
                print("Utwórz zbiór liczb!")
                z=float(input("Podaj pierwszą liczbę: "))
                zbior.append(z)
                y = "TAK"
            else:
                break
        
        while y == "TAK":
            if(x == "SA" or x == "SG" or x == "ME" or x == "MO" or x == "OS" or x == "WK" or x == "WRL"):            
                z=float(input("Podaj kolejną liczbę: "))
                zbior.append(z)
                print(f"Aktualny zbiór liczb to: {zbior}")
                y=input("Czy chcesz dodać kolejną liczbę? TAK | NIE : ")
                y=y.upper()
            
            else:
                break
        
    elif(x == "SA"):
        SA()
        x="NIE"
        
    elif(x == "SG"):
        SG()
        x="NIE"

    elif(x == "ME"):
        ME()
        x="NIE"
        
    elif(x == "MO"):
        MO()
        x="NIE"

    elif(x == "OS"):
        OS()
        x="NIE"    
        
    elif(x == "WK"):
        WK()
        x="NIE"  
        
    elif(x == "WRL"):
        WRL()
        x="NIE"  
    
    elif(x == "K"):
        print("Program został zakończony!")
        war = 1
        
    else:
        print("Nieprawidłowa komenda!")
        x="NIE"
        