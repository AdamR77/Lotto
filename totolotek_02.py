from random import sample

randomized = []
table = []
for nr in range(1,50):
    table.append(nr)
   
print("* * * * * * * * * * * *")
print("* * *  L O T T O  * * *")
print("* * * * * * * * * * * * \n")

your_nrs = []
i =0
draw = 1 #liczba kolejna zakładów
hit = 0 #liczba trafień
price = 3 #cena zakładu

# pierwsza pętla -> powtarzanie: pobranie 6 liczb od użytkownika i wpisanie do listy, losowanie 6 liczb i wpisanie do listy,
# porównanie obydwu list i komunikat o wygranej 3,4,5 lub 6 trafień, wyświetlenie całkowitego kosztu gry i sprawdzenie czu użytkownik chce grać dalej 
# jeśli nie -> przerwanie pętli
while True:  
    print(f"typowanie liczb -> nr: {draw}")
    for x in range(6):
        i+=1    
    
# druga pętla pobranie danych od użytkownika i sprawdzenie poprawności czy jest to liczba z predziału <1,49>  
# 2 zagnieżdżone pętle wewnętrzne, pierwsza - pobranie liczby 2ga walidacja danych (znaki czy liczby)
        while True:
            print(f"Liczba {i}: ", end =" ")
            while True:
                try:
                    nr = int(input("podaj liczbe całkowitą z przedziału 1-49: " ))
                except:
                    print("nie podałeś liczby ale litery albo inne znaki")
                else:
                    break

            if nr < 1 or nr > 49:
                print("Liczba poza przedziałem 1-49")  
            elif nr in your_nrs:
                print(f"Już podałeś {nr}, liczby nie mogą się powtarzać")
            else:
                your_nrs.append(nr)
                break
            

    print(f" Twoje liczby to: {your_nrs} \n" )  
    randomized = sample(table, k = 6)
    print(f" wylosowane liczby to: {randomized} \n")

    hit = 0 #liczba trafień w losowaniu
    for x in your_nrs:
        if x in randomized:
            hit += 1
            print(" trafiłeś: ", {x}  )

        if hit >= 3:
            print("trafiłeś {hit} liczb(y)")
        if hit == 6:
            print("GRATULACJE !!! stałeś sie bardzo bogaty :) ")
    
        else:
            print("Nie wygrałeś żadnej nagrody (trafienia 3,4,5 lub 6 liczb)")
        quote = price * draw
        print(f"wydałeś {quote} złotych")    
    while True:
        decision = input("chcesz grać dalej? [t/n]")
        if decision == "t" or "n":
            break
        if decision == "n":
            print(" Dzięki. Kończymy")
            break
        draw += 1
        break
        





    
    
 


 
