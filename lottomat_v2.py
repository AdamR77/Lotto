from random import sample

drawing_nrs = 1 #liczba kolejna zakładów
price = 3 #cena zakładu

def table_generate(elements: int):
    table = []
    for nr in range(1, elements +1):
        table.append(nr)
    return table

def randomize(table, nrs):
    randomized = sample(table, k = nrs)
    return randomized


lotto_numbers  = randomize(table_generate(49), 6)
mini_lotto_numbers = randomize(table_generate(42), 5)

print(" \n_________________________")
print("|     L O T T O M A T    |")
print("|        v. 2.0          | ")
print("|________________________| \n")

print("*losujemy na 'chybił-trafił' do skutku ")
print("*jeden zakład Lotto  cena: 3pln")
print("*przygotuj portfel :D  \n")

how_much = int(input("ile liczb chcesz trafić? : "))
print("\nWyniki losowania lotto to:")
print(lotto_numbers)
print("")

lp = 1
account = 0
hit_nrs = []
while how_much > account:    
    hit_nrs.clear()
    account = 0
    your_lotto_numbers = randomize(table_generate(49), 6)
    print(f' chybił trafił nr {lp}: {your_lotto_numbers}')
    for nr in your_lotto_numbers:
        if nr in lotto_numbers:
            account += 1
            hit_nrs.append(nr)
    lp += 1
    if account < how_much:
        print("   pudło! \n")    
quote = lp * price
print(f"trafiłeś {account} liczb: {hit_nrs} ")  
print(f"wydałeś {quote} pln") 
    





  

        







    
    
 


 
