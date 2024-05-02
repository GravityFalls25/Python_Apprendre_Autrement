
label village_en_feu:
    scene village fire with fade

    "Quelle scene apocalyptique, il y a plusieurs maisons en feu"


label troisieme:
    python:
        postData = {"valeur": "2","id": id}
        url = 'http://127.0.0.1:5000'
        val = renpy.fetch(url, json = postData)
        url = site
        lien = "{a="+url+"}Vite il y a un puit la-bas, va chercher de l'eau{/a}"
        renpy.say(j,lien)

    $ reussi = False
    python:
        # Remplacez l'URL ci-dessous par l'URL où votre script PHP est accessible
        url = 'http://127.0.0.1:5000/get_mission_state'

        try:
            request= renpy.fetch(url, json = {"player_id":id}, result="json")
            reussi, gold_gagne = request['mission_state']
            persistent.gold = persistent.gold + int(gold_gagne)
            renpy.say(j, "Waouw merci, tu as gagné [gold_gagne]")
            if not reussi:
                renpy.say(None, "Mauvaise reponse reessayer encore une fois")
                reussi = False
                

        except Exception as erreur:
            # Gère les erreurs potentielles lors de la requête
            renpy.say(None, "Erreur lors de la requête : {}".format(str(erreur)))


    if reussi != True:
        jump troisieme
    python:
                url = 'http://127.0.0.1:5000/clear_quete'
                request= renpy.fetch(url, json = {"player_id":id}, result="json")
label test:
    m "Ouf, je pense qu'on a reussi à controler l'incendie mais qu'est ce qui a bien pu causer ca ?"

    define v= Character(_("Villageois"), color="#446d14")
    show villageoiq
    v "Ce sont les troupes d'Ouroboros qui ont causé ce chaos"

    v "Ils sont venu pour nous prendre de la nourriture et en voyant le peu de nourriture que nous avions, ces monstres se sont enervés et ont mis le feu a notre village"
    show villageoiq with ease:
        xzoom -1.0
        xalign 0.1
    show Navi angry with vpunch :
        xalign 0.9
        yalign 1.0
    j "Encore eux ?"

    j "ils ne lasseront donc jamais de causer du mal à des innocents ?"

    j "Il est grand temps d'arranger ce probleme une fois pour toute"

    v "Calme toi Navi, on doit juste tenir jusqu'à que le hero de la prophetie vienne nous secourir"

    j "Cette prophetie date d'il y a des dizaines voire de centaines d'années si ca se trouve on sera tous mort d'ici a que cet hero apparaisse"

    j "Je vais prendre les choses en main, apres tout parfois il faut savoir forcer le destin pour obtenir le futur voulu"
    hide villageoiq
    show Navi angry at center with ease
    j "[name], je pourrais pas me rebeller face à ce Serpent toute seule peut tu me preter main forte ?"

    menu:
        "Oui bien sur":
            j "Parfait, j'aime cette reponse rempli de confiance"
        "...":
            j "Je vois à ton regard rempli de determination que toi non plus tu refuse de voir les villageois souffrir plus longtemps"
    
    show Navi at center

    j "Mais avant de faire quoi que ce soit, il faut reparer les degats causé par l'incendie"

    m "Laissez-moi vous aider car apres tout je suis le meilleur bricoleur des environs"

    scene black with fade
    "Quelques heures plus tard"

    scene bg_village_lateday with fade
    show Navi at center
    j "Merci de ton aide [name], si tu avais pas été la ca aurait prit beaucoup plus de temps"

    m "De rien, c'etait la moindre des choses"

    m "D'ailleurs par rapport a ce que tu as dis plus tot, si tu veux vraiment t'attaquer au Serpent du temps, tu dois avoir un plan"

    j "J'avoue avoir dit ca sous le coup de la colere et je n'ai pas vraiment de plan mais ma determination est elle bien reelle"

    j "Juste laisse moi un peu de temps pour penser à un plan"

    m "Est-ce que je peux t'aider à quelque chose ?"

    j "Oui, comme dans tous les cas il faudra voyager on aura besoin d'un peu d'argent pour la nourriture et les autres frais du voyage"

    j "500 piece d'or devrait etre suffisant"

    j "Tu peux gagner un peu d'argent en acceptant des quetes dans la taverne"

    j "Une fois que tu as assez d'or vient me retrouver à l'entrée du village"

    m "Ok bien compris, à demain alors"
    scene black with fade

    "Le lendemain matin"
label place_village:
    scene bg_village_day with fade
    play music "mist_covered_mountains.mp3" if_changed
    $ quick_menu = True
    menu:
        "Bon que devrais-je faire maintenant"
        "Aller à la taverne":
            jump tavern_village
        "Aller à l'entrée du village":
            python:
                if int(persistent.gold)>=500:
                    renpy.jump("fin_chap1")
                else:
                    renpy.say(None,"j'ai pas encore assez d'or")
                    renpy.jump("place_village")
        "voir la map":
            $ quick_menu = False
            call screen Map with fade
label tavern_village:
    play music "Tavern_song.mp3" if_changed
    scene tavern
    show tavernier

    $ renpy.save_persistent()
    T "Bienvenue dans ma taverne que puis je faire pour vous"
    menu: 
        "Voir les quetes disponibles":
            $ quests = load_quests()
            call screen quest_menu(0,quests)
        "Repartir":
            
            jump place_village

label dialogue_aubergiste(quest_id,quest_nom, url):
    T "Bonjour, bon courage pour la quête!"
    menu:
        "Commencer la quête":
            T "Parfait, voici les détails..."
            $ webbrowser.open(url)  # Redirige vers la page web si validé
            call quete_aubergiste(quest_id,quest_nom, url)
        "Annuler":
            T "C'est dommage, peut-être une autre fois."
            jump tavern_village
label quete_aubergiste(quest_id,quest_nom, url):
    T "Alors, tu avances bien dans ta quete ?"
    menu:
        "Valider la quête":

            $ reussi = False
            python:
                # Remplacez l'URL ci-dessous par l'URL où votre script PHP est accessible
                url = 'http://127.0.0.1:5000/get_mission_state'

                try:
                    request= renpy.fetch(url, json = {"player_id":id}, result="json")
                    reussi, gold_gagne = request['mission_state']
                    persistent.gold = persistent.gold + int(gold_gagne)
                    renpy.say(T, "Waouw merci, tu as gagné [gold_gagne]")
                    if not reussi:
                        renpy.say(None, "Mauvaise reponse reessayer encore une fois")
                        reussi = False
                        

                except Exception as erreur:
                    # Gère les erreurs potentielles lors de la requête
                    renpy.say(None, "Erreur lors de la requête : {}".format(str(erreur)))


            if reussi != True:
                python:
                    url = 'http://127.0.0.1:5000/clear_quete'
                    request= renpy.fetch(url, json = {"player_id":id}, result="json")
                call quete_aubergiste(quest_id,quest_nom, url)

            $ persistent.Quete_faite.append((quest_id, quest_nom))
            python:
                url = 'http://127.0.0.1:5000/clear_quete'
                request= renpy.fetch(url, json = {"player_id":id}, result="json")

            jump tavern_village
        "Abandonner":
            T "C'est dommage, peut-être une autre fois."
            jump tavern_village
    