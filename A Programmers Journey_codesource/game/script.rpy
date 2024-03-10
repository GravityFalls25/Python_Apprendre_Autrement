# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define c = Character(_("Enfants Joyeux"), color="#c8ffc8")


# Le jeu commence ici
label start:

    scene bg_village_day
    with fade
    show children
    c "Bonjour monsieur, mes amis et moi voulons jouer au pierre-papier-ciseaux mais on a oublié les régles"

    c "Pourriez-vous nous les rappeler ?"

    return
