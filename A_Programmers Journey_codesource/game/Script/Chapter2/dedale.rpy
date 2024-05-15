label chap2:
    scene black with fade
    #ca serait bien de mettre une cinematique ou ils voyagent
    "{i}Quelques heures plus tard{/i}"

    scene entree_labyrinthe with fade
    show children:
        xalign 0.9
        yalign 1.0
    j "Et voici l'entrée du grand dédale des mille choix"
    
    m "Mais c'est juste une porte, il n'y a rien derriere"

    j "Ne te laisse pas tromper par son apparence. Lorsque tu traverseras la porte, tu verras le labyrinthe"

    j "Ne perdons pas plus de temps et allons-y directement !"

    hide children with moveoutright
    m "Hey attend moi !"

    scene interieur_labyrinthe with flash
    m "C'est donc à ca que ressemble le dédale de l'interieur"

    show children:
        xalign 0.1
        yalign 1.0
    j "Viens voir il y a message marqué sur le mur..."

    "Bienvenue dans ce dédale de choix, où chaque pas est une décision à prendre, chaque tournant une opportunité nouvelle. Ici, les chemins se croisent et se séparent. Le dédale te donnera la capacité de choisir"

    "Au bout de ce dédale, tu découvriras que la vraie récompense réside dans la liberté de décider de ton destin. Alors avance avec courage, et que chaque décision te rapproche de cette précieuse récompense : le pouvoir de faire tes propres choix."

    j "\"Le dédale te donnera la capacité de choisir\" Je me demande ce que ca veut dire"
    call screen debloquer(2)
    call screen debloquer(3)
    call screen debloquer(4)
    m "Il semblerait qu'on puisse utiliser les pouvoirs de la fonction divine tant qu'on est dans le labyrinthe"

    j "Parfait alors enfonçons nous dans la labyrinthe !"

    scene labyrinthe_porte
    show children at right

    m "Il semblerait que ce soit le premier choix qu'il faille faire, quelle porte on choisit ?"

    j "Regarde il y a un autre message sur ce mur"

label quatrieme:
    python:
        nom_quete = create_html(3,id,j,"Resolvez cette enigme et le meilleur choix s'offrera a vous") #rajouter quete
        if nom_quete is None:
            renpy.jump("quatrieme")
        reussi = False
        reussi,gold_gagne = verif_quete(id,2)

    if reussi != True:
        jump quatrieme
    python:
        remove_html(id)

    call screen ecran_victoire(nom_quete,gold_gagne,2)
label test1:
    j "Parfait on peut continuer d'avancer maintenant"

    scene interieur_labyrinthe with fade
    m "Tiens il y a encore des ecritures sur le mur mais on dirait que ce n'est pas la meme personne qui l'a ecrit"

    "Mon nom est Elsa et je suis l'elue responsable de la fonction if-else ou du moins je l'étais avant que Ouroboros renie l'humanité"
    
    "J'ai déjà perdu nombre de mes camarades et je sais que je serai bientot la prochaine. C'est pourquoi j'ai decidé de cacher ma fonction au centre de ce dédale, protegé par un immense minotaure"

    "Ce labyrinthe a été créé pour perdre le serpent, en effet celui-ci etant tres impatient il ne prendra jamais le temps de lire ces ecritures"

    "De plus, pour trier les intrus des meritants, j'ai chiffré le message permettant d'acceder au centre du labyrinthe"

    "Ontq sqntudq kd bdmsqd cd bd cdczkd hk rteehs cd chqd z gztsd unhw kz enqltkd rthuzmsd \"vhsg nodm(\"cnnq.nai\",'v')\" "

    m "Par contre, comment allons nous dechiffrer ca ?"
    scene indice_mur
    j "Regarde il y a encore des choses écrites sur ce mur, peut-etre cela pourrait nous aider ?"

label cinquieme:
    python:
        nom_quete = create_html(4,id,m,"Bien vu, ca sera suffisant pour que je decode ca")
        if nom_quete is None:
            renpy.jump("cinquieme")
        reussi = False
        reussi,gold_gagne = verif_quete(id,2)

    if reussi != True:
        jump cinquieme
    python:
        remove_html(id)

    call screen ecran_victoire(nom_quete,gold_gagne,2)
label test2:
    m "Pour trouver le centre de ce dédale il suffit de dire à haute voix la formule suivante \"with open(\"door.obj\",'w')\" "
    
    play sound "stone_door.mp3"
    j "Wow, le mur s'ouvre vraiment !"

    scene centre_labyrinthe
    show children at right
    m "Cet endroit est vraiment magnifique mais si on est vraiment au centre du labyrinthe, ça vaut aussi dire que..."

    play sound "giant-walking.mp3" volume 0.3
    scene centre_labyrinthe with hpunch
    m "...le minotaure..."

    play sound "giant-walking.mp3" volume 0.6
    scene centre_labyrinthe with hpunch
    m "...est ici"

    play sound "giant-walking.mp3" volume 1.0
    scene centre_labyrinthe with hpunch
    show minotaure scary with moveinleft
    mino "Qui ose s'introduire dans mon domaine ?"
    
    "Je savais que c'était une mauvaise idée de venir ici, on va tous mourir ici de la main de cet immense et terrifiant minautaure"
    play music "Minotaur_song.mp3"
    show minotaure 
    mino "Au mon dieu, est-ce que ce sont des humains ? ça fait des lustres depuis que la derniere fois que j'en ai vu"

    mino "Oh non, je ne suis pas bien habillé et je n'ai même pas fait le menage"

    jm "Hein ?"

    mino "Excusez-moi j'en oublie mes manieres, je me presente: Je suis le gardien de ce dédale"
    show minotaure happy
    mino "Comment puis-je vous aider ?"

    "Ouf plus de peur que de mal, il a l'air gentil"

    j "Nous sommes à la recherche de la fonction divine qui se trouverait dans ce labyrinthe"

    mino "Je vois c'est bien moi qui ai cet artefact"
    show minotaure
    mino "Malheureusement, je suis desolé mais mon maitre m'a interdit de le donner à un aventurier tant qu'il n'a pas prouvé sa valeur"

    mino "Si cela vous convient, je vous propose de répondre à mes enigmes, si vous accumulez assez de points de valeur en répondant correctement, j'accepeterais de vous ceder l'artefact"

    mino "Encore desolé du derangement"

    m "Parfait ça nous convient"
    $ persistent.chap=2
label place_dedale:
    scene centre_labyrinthe with fade
    play music "Minotaur_song.mp3" if_changed
    $ quick_menu = True
    menu:
        "Bon que devrais-je faire maintenant"
        "Resoudre les enigmes du minotaure":
            jump tavern_dedale
        "Recuperer l'artefact":
            python:
                if int(persistent.point_de_valeur)>=200:
                    renpy.jump("fin_chap2")
                else:
                    renpy.say(None,"je n'ai pas encore assez de points de valeur, il me faut au moins 200 points")
                    renpy.jump("place_dedale")
        "voir la map":
            $ quick_menu = False
            call screen Map(persistent.chap) with fade

label tavern_dedale:
    play music "Minotaur_song.mp3" if_changed
    scene centre_labyrinthe
    show minotaure happy

    $ renpy.save_persistent()
    mino "Tu es pret à resoudre mes enigmes ?"
    menu: 
        "Voir les enigmes disponibles":
            $ quests = load_quests(2)
            call screen quest_menu(2,quests,"dialogue_aubergiste_minotaur","tavern_dedale")
        "Repartir":
            
            jump place_dedale
label dialogue_aubergiste_minotaur(quest_id,quest_nom, url):
    mino "J'espere que tu es pret"
    menu:
        "Commencer l'enigme":
            mino "Parfait, alors l'enigme est..."
            $ webbrowser.open(url)  # Redirige vers la page web si validé
            call quete_aubergiste_minotaur(quest_id,quest_nom, url) from _call_quete_aubergiste_minotaur
        "Annuler":
            mino "C'est dommage, peut-être une autre fois."
            python:
                remove_html(id)
            jump tavern_dedale
label quete_aubergiste_minotaur(quest_id,quest_nom, url):
    mino "Alors, tu penses avoir resolu mon enigme ?"
    menu:
        "Valider l'enigme":

            python:
                
                reussi = False
                reussi,gold_gagne = verif_quete(id,2)

            if reussi != True:
                call quete_aubergiste_minotaur(quest_id,quest_nom, url)
            python:
                remove_html(id)
                persistent.Quete_faite.append((quest_id, quest_nom))
            call screen ecran_victoire(quest_nom,gold_gagne,2)

            jump tavern_dedale
        "Abandonner":
            mino "C'est dommage, peut-être une autre fois."
            python:
                remove_html(id)
            jump tavern_dedale

label fin_chap2:
    mino "Je pense que tu as suffisamment prouvé ta valeur. Tu es donc digne de recuperer cet artefact"
    #mettre ecran de victoire "if permanent"
    j "Felicitation [name], maintenant on peut continuer notre voyage"

    m "Quel est notre prochaine destination ?"

    j "Notre prochain objectif est d'en apprendre davantage sur notre ennemi à la Bibliotheque-monde"

    j "car tu sais ce qu'on dit: \"Le savoir est l'arme la plus efficace contre les tyrants\""

    "C'est beau ce qu'elle dit"

    "Je me demande bien qui sont les gens qui disent ça"

    m "Très bien alors, allons-y !"

    jump Temporium

