J1 =input("Pierre, Papier ou Ciseaux: ")
J2 = input("Pierre, Papier ou Ciseaux: ")
    
    
if J1 == J2:
    print('Egalite')
    
elif J1 == "Pierre" and J2 == "Papier":
    print("J2 gagne")
    pass
    
elif J1 == "Pierre" and J2 == "Ciseaux":
    print("J1 gagne")
    pass
elif J1 == "Papier" and J2 == "Ciseaux":
    print("J2 gagne")
        
    pass
elif J1 == "Papier" and J2 == "Pierre":
    print("J1 gagne")
    pass
elif J1 == "Ciseaux" and J2 == "Pierre":
    print("J2 gagne")
    pass
elif J1 == "Ciseaux" and J2 == "Papier":
    print("J1 gagne")
    pass
else:
    print("Erreur")