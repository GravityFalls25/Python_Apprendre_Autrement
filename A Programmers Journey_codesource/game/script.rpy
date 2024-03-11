# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define c = Character(_("Enfant Joyeux"), color="#c8ffc8")


# Le jeu commence ici
label start:

    "Aujourd'hui j'ai décidé de faire un tour sur la place du village"

    scene bg_village_day
    with fade

    "une fois arrivé sur la place je remarque un groupe d'enfants qui semblent s'amuser. Une jeune fille me remarque et decide de s'approcher de moi"

    show children
    c "Bonjour monsieur, mes amis et moi voulons jouer au pierre-papier-ciseaux mais on a oublié les régles"

    c "Pourriez-vous nous les rappeler ?"

    return
