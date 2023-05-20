import random

daljina_pole = 50
broy_igrachi = 4
pozicii = [1, 3, 5, 7]
simvoli_igrachi = ['i', 'a', 't', 'v']

while True:
    nex_t = int(input("Sledvasht hod. Natisni tzifra: "))
    for num_igrach in range(broy_igrachi):
        zar = random.randint(1, 6)
        
        new_position = pozicii[num_igrach] + zar
        occupied = [player for player in pozicii if player == new_position]
        
        if not occupied and new_position <= daljina_pole:
            pozicii[num_igrach] = new_position
        
        print("igrach N " + str(num_igrach) + " e na poziciya " + str(pozicii[num_igrach]) + ".")
    
    broi = 0
    
    for index_igrach in range(broy_igrachi):
        if pozicii[index_igrach] > daljina_pole:
            print("Igrach N " + str(index_igrach) + " izleze ot poleto.")
            broi += 1

    for tekushta_poziciya in range(1, daljina_pole + 1):
        simvol_za_izvejdane = "."
        
        for index_igrach in range(broy_igrachi):
            if tekushta_poziciya == pozicii[index_igrach]:
                simvol_za_izvejdane = simvoli_igrachi[index_igrach]
            
        print(simvol_za_izvejdane)

    print(zar)
    
    if broi == broy_igrachi:
        print("Vsichki sa izvan poleto.")
        break

print("Nyakoy specheli!")