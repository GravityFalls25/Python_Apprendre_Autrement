
label village_en_feu:
    scene village fire with fade

    "Quelle scène apocalyptique, il y a plusieurs maisons en feu"


label troisieme:
    python:
        nom_quete = create_html(2,id,m,"Vite! Il y a un puits là-bas, va vite chercher de l'eau")#pas la quete la plus claire
        if nom_quete is None:
            renpy.jump("troisieme")
        reussi = False
        reussi,gold_gagne = verif_quete(id,1)

    if reussi != True:
        jump troisieme
    python:
        remove_html(id)

    call screen ecran_victoire("Incendie au village",gold_gagne,1)
label test1:
    m "Ouf, je pense qu'on a réussi à contrôler l'incendie mais qu'est ce qui a bien pu causer ca ?"

    define v= Character(_("Villageois"), color="#446d14")
    show villageoiq
    v "Ce sont les troupes d'Ouroboros qui ont causé ce chaos"

    v "Ils sont venus pour nous prendre de la nourriture et en voyant le peu que nous avions, ces monstres se sont enervés et ont mis le feu à notre village"
    show villageoiq with ease:
        xzoom -1.0
        xalign 0.1
    show Navi angry with vpunch :
        xalign 0.9
        yalign 1.0
    j "Encore eux ?"

    j "Ils ne lasseront donc jamais de causer du mal à des innocents ?"

    j "Il est grand temps d'arranger ce problème une fois pour toute"

    v "Calme toi Navi, on doit juste tenir jusqu'à ce que le héros de la prophétie vienne nous secourir"

    j "Cette prophétie date d'il y a des dizaines voire des centaines d'années. Si ça se trouve, on sera tous morts d'ici à que ce héros apparaisse"

    j "Je vais prendre les choses en main. Après tout, parfois, il faut savoir forcer le destin pour obtenir le futur voulu"
    hide villageoiq
    show Navi angry at center with ease
    j "[name], je ne pourrais pas me rebeller face à ce Serpent toute seule. Peux-tu me prêter main forte ?"

    menu:
        "Oui, bien-sûr":
            j "Parfait, j'aime cette réponse remplie de confiance"
        "...":
            j "Je vois à ton regard rempli de détermination que toi aussi tu refuses de voir les villageois souffrir plus longtemps"
    
    show Navi at center

    j "Mais avant de faire quoi que ce soit, il faut réparer les dégâts causés par l'incendie"

    m "Laissez-moi vous aider car après tout, je suis le meilleur bricoleur des environs"

    scene black with fade
    "Quelques heures plus tard"

    scene bg_village_lateday with fade
    show Navi at center
    j "Merci de ton aide [name]. Si tu n'avais pas été la, on serait encore loin d'avoir fini"

    m "C'était la moindre des choses"

    m "D'ailleurs, par rapport à ce que tu as dis plus tôt, si tu veux vraiment t'attaquer au Serpent du Temps, tu dois avoir un plan"

    j "J'avoue avoir dit ça sous le coup de la colère mais je n'ai pas vraiment de plan. Mais je me battrai jusqu'au bout!"

    j "Juste, laisse-moi un peu de temps pour penser à un plan"

    m "Est-ce que je peux t'aider pour quelque chose ?"

    j "Oui, comme dans tous les cas il faudra voyager, on aura besoin d'un peu d'argent pour la nourriture et les autres frais du voyage"

    j "300 pièces d'or devraient être suffisantes"

    j "Tu peux gagner un peu d'argent en acceptant des quêtes dans la taverne"

    j "Une fois que tu as assez d'or, viens me retrouver à l'entrée du village"

    m "Ok bien compris, à demain alors"
    scene black with fade

    "Le lendemain matin"
    $ persistent.chap=1
label place_village:
    scene bg_village_day with fade
    play music "mist_covered_mountains.mp3" if_changed
    $ quick_menu = True
    menu:
        "Bon, que devrais-je faire maintenant ?"
        "Aller à la taverne":
            jump tavern_village
        "Aller à l'entrée du village":
            python:
                if int(persistent.gold)>=300:
                    renpy.jump("fin_chap1")
                else:
                    renpy.say(None,"Je n'ai pas encore assez d'or")
                    renpy.jump("place_village")
        "Voir la map":
            $ quick_menu = False
            call screen Map(persistent.chap) with fade
label tavern_village:
    play music "Tavern_song.mp3" if_changed
    scene tavern
    show tavernier

    $ renpy.save_persistent()
    T "Bienvenue dans ma taverne. Que puis-je faire pour vous ?"
    menu: 
        "Voir les quêtes disponibles":
            $ quests = load_quests(1)
            call screen quest_menu(1,quests,"dialogue_aubergiste","tavern_village")
        "Repartir":
            
            jump place_village

label dialogue_aubergiste(quest_id,quest_nom, url):
    T "Bonjour, bon courage pour la quête!"
    menu:
        "Commencer la quête":
            T "Parfait, voici les détails..."
            $ webbrowser.open(url)  # Redirige vers la page web si validé
            call quete_aubergiste(quest_id,quest_nom, url) from _call_quete_aubergiste
        "Annuler":
            T "C'est dommage, peut-être une autre fois."
            python:
                remove_html(id)
            jump tavern_village
label quete_aubergiste(quest_id,quest_nom, url):
    T "Alors, tu avances bien dans ta quête ?"
    menu:
        "Valider la quête":

            python:
                
                reussi = False
                reussi,gold_gagne = verif_quete(id,1)

            if reussi != True:
                call quete_aubergiste(quest_id,quest_nom, url)
            python:
                remove_html(id)
                persistent.Quete_faite.append((quest_id, quest_nom))
            call screen ecran_victoire(quest_nom,gold_gagne,1)

            jump tavern_village
        "Abandonner":
            T "C'est dommage, peut-être une autre fois."
            python:
                remove_html(id)
            jump tavern_village
    
label fin_chap1:
    scene entree_village with fade
    show children
    j "Voilà, je pense qu'on a réuni assez d'argent"
    
    j "De mon coté, j'ai fini le plan pour vaincre le Serpent du Temps."

    j "Comme tu le sais, nous avons perdu l'accès aux fonctions. Cependant, certains élus, sachant que leur heure était venue, ont eu le temps de cacher leur fonction"

    j "Selon la légende, une de ces fonctions a été cachée non loin d'ici dans le Grand Dédale des Mille Choix"

    j "C'est pourquoi nous commencerons par nous rendre là-bas. Une fois récupérée, nous nous rendrons à Temporium, la ville où se trouve la Bibliothèque-monde"

    j "Nous irons là-bas pour trouver toutes les informations qui peuvent nous être utiles pour vaincre le Serpent du Temps"

    "Est-ce qu'elle vient juste de dire qu'on irait dans un labyrinthe ?"

    "Ca m'a l'air dangereux"

    m "Comment on va faire pour ne pas se perdre dans le labyrinthe ?"

    j "Aucune idée, on verra à ce moment-là."

    "Cette fille va finir par me tuer."

    j "Bon, allons-y !"

    jump chap2