label chap2:
    scene black with fade
    #ca serait bien de mettre une cinematique ou ils voyagent
    "{i}Quelques heures plus tard{/i}"

    scene entree_labyrinthe with fade
    show children:
        xalign 0.9
        yalign 1.0
    j "Et voici l'entrée du grand dedale des milles choix"
    
    m "Mais c'est juste une porte, il n'y a rien derriere"

    j "Ne te laisse pas tromper par son apparence car lorsque tu traversera la porte, tu verra le labyrinthe"

    j "Ne perdons pas plus de temps et allons-y directement"

    hide children with moveoutright
    m "Hey attend moi"

    scene interieur_labyrinthe with flash
    m "C'est donc à ca que ressemble le dedale de l'interieur"

    show children:
        xalign 0.1
        yalign 1.0
    j "Vient voir il y a message marqué sur le mur"

    "Bienvenue dans ce dedale de choix, où chaque pas est une décision à prendre, chaque tournant une opportunité nouvelle. Ici, les chemins se croisent et se séparent et pour savoir où aller le dedale te donnera la capacité de choisir"

    "Au bout de ce dédale, tu découvriras que la vraie récompense réside dans la liberté de décider de ton destin. Alors avance avec courage, et que chaque décision te rapproche de cette précieuse récompense : le pouvoir de faire tes propres choix."

    j "\"le dedale te donnera la capacité de choisir\" je me demande ce que ca veut dire"
    #pop-up ou on explique comment if-else fct
    m "Il semblerait qu'on peut utiliser les pouvoirs de la fonction divine tant qu'on est dans le labyrinthe"

    j "Parfait alors enfoncons nous dans la labyrinthe"

    scene portes
    show children at right

    m "il semblerait que ce soit le premier choix qu'il faille faire, quelle porte on choisit ?"

    j "Regarde il y a un autre message sur ce mur"

label quatrieme:
    python:
        nom_quete = create_html(3,id,j,"Resolvez cette enigme et le meilleur choix s'offrera a vous")
        reussi = False
        reussi,gold_gagne = verif_quete(id)

    if reussi != True:
        jump quatrieme
    python:
        remove_html(id)

    call screen ecran_victoire(nom_quete,gold_gagne,persistent.gold)
label test1:
    j "Parfait on peut continuer d'avancer maintenant"

    scene interieur_labyrinthe with fade
    m "Tiens il y a encore des ecritures sur le mur mais on dirait que ce n'est pas la meme personne qui l'a ecrit"

    "Mon nom est Elsa et je suis l'elue responsable de la fonction if-else ou du moins je l'etait avant que Ouroboros renie l'humanité"
    
    "J'ai deja perdu nombre de mes camarades et je sais que je serai bientot la prochaine. C'est pourquoi j'ai decidé de cacher ma fonction au centre de ce dedale protegé par un immense minotaure"

    "Ce labyrinthe a été créé pour perdre le serpent, en effet celui-ci etant tres impatient il ne prendra jamais le temps de lire ces ecritures"

    "Alors qu'en realité il suffit de lire ces ecritures suivantes pour acceder au centre du labyrinthe. De plus, pour trier les intrus des meritants, j'ai chiffré le message"

    "Ontq sqntudq kd bdmsqd cd bd cdczkd hk rteehs cd chqd z gztsd unhw kz enqltkd rthuzmsd \"vhsg nodm(\"cnnq.nai\",'v')\" "

    m "Par contre, comment allons nous dechiffrer ca ?"
    scene indice_mur
    j "Regarde il y a encore des choses ecrites sur ce mur, peut-etre ca pourrait nous aider ?"

label cinquieme:
    python:
        nom_quete = create_html(4,id,m,"Bien vu, ca sera suffisant pour que je decode ca")
        reussi = False
        reussi,gold_gagne = verif_quete(id)

    if reussi != True:
        jump cinquieme
    python:
        remove_html(id)

    call screen ecran_victoire(nom_quete,gold_gagne,persistent.gold)
label test2:
    m "Pour trouver le centre de ce dédale il suffit de dire a haute voix la formule suivante \"with open(\"door.obj\",'w')\" "
    
    play sound "stone_door.mp3"
    j "Wow, le mur s'ouvre vraiment !"

    scene centre_labyrinthe
    show children at right
    m "Cet endroit est vraiment magnifique mais si on est vraiment au centre du labyrinthe ca vaut aussi dire que..."

    play sound "giant-walking.mp3" volume 0.3
    scene centre_labyrinthe with hpunch
    m "...le minotaure..."

    play sound "giant-walking.mp3" volume 0.6
    scene centre_labyrinthe with hpunch
    m "...est ici"

    play sound "giant-walking.mp3" volume 1.0
    scene centre_labyrinthe with hpunch
    show minotaure scary with moveinleft
    mino "Qui ose s'introduire de mon domaine ?"
    
    "Je savais que c'était une mauvaise idée de venir ici, on va tous mourir ici de la main de cet immense et terrifiant minautaure"
    play music "Minotaur_song.mp3"
    show minotaure 
    mino "Au mon dieu, est-ce que ce sont des humains ? Ca fait des dizaines d'années depuis que la derniere fois que j'ai vu un humain"

    mino "En plus, je ne suis pas bien habillé et je n'ai meme pas fait le menage"

    jm "Hein ?"

    mino "Excusez-moi j'en oublie mes manieres, je me presente suis le gardien de ce dedale"
    show minotaure happy
    mino "Comment puis-je vous aider ?"

    "J'imagine que c'est ca que Elsa entendait quand elle disait qu'il ne ferait pas de mal a une mouche"

    j "On est a la recherche de la fonction divine qui se trouverait dans ce labyrinthe"

    mino "Je vois c'est bien moi qui ai cette artefact"
    show minotaure
    mino "Malheureusement, je suis desolé mais mon maitre m'a interdit de le donner à un aventurier tant qu'il n'a pas prouvé sa valeur"

    mino "Si cela vous convient, je vous propose que si vous arrivez a accumuler 5 points de valeur en repondant à mes enigmes alors je vous cederais l'artefact"

    mino "Encore desolé du derangement"

    m "Parfait ca nous convient"

label place_dedale:
    scene centre_labyrinthe with fade
    play music "Minotaur_song.mp3" if_changed
    $ quick_menu = True
    menu:
        "Bon que devrais-je faire maintenant"
        "Resoudre des enigmes du minotaure":
            jump tavern_dedale
        "Recuperer l'artefact":
            python:
                if int(persistent.point_de_valeur)>=5:
                    renpy.jump("fin_chap2")
                else:
                    renpy.say(None,"j'ai pas encore assez de points de valeur")
                    renpy.jump("place_dedale")
        "voir la map":
            $ quick_menu = False
            call screen Map with fade

label tavern_dedale:
    play music "Minotaur_song.mp3" if_changed
    scene centre_labyrinthe
    show minotaure happy

    $ renpy.save_persistent()
    T "Tu es pret à resoudre mes enigmes ?"
    menu: 
        "Voir les enigmes disponibles":
            $ quests = load_quests()
            call screen quest_menu(1,quests)
        "Repartir":
            
            jump place_dedale

