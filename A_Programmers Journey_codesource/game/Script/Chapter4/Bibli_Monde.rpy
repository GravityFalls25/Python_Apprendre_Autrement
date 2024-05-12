label Bibli_monde:
    scene bibli_int
    show bibliothecaire:
        ypos 0.2
        xpos 0.25
        xzoom 1.75
        yzoom 1.75
    play music "Tavern_song.mp3" if_changed
    bibli "Bienvenue. Que puis faire pour vous ?"
    $ renpy.save_persistent()
    
    menu: 
        "Voir les livres de quetes disponibles":
            $ quests = load_quests(4)
            call screen quest_menu(4,quests,"dialogue_bibli","Bibli_monde")
        "Repartir":
            jump chemin

label dialogue_bibli(quest_id,quest_nom, url):
    j "Essayons celui la"
    menu:
        "Commencer le livre":
            m "Alors..."
            $ webbrowser.open(url)  # Redirige vers la page web si validé
            call quete_bibli(quest_id,quest_nom, url)
        "Annuler":
            m "C'est dommage, peut-être une autre fois."
            jump Bibli_monde
label quete_bibli(quest_id,quest_nom, url):
    j "C'est bon ? Tu as fini de la solution du livre ?"
    menu:
        "Valider l'enigme":

            python:
                
                reussi = False
                reussi,gold_gagne = verif_quete(id,4)
            if reussi != True:
                jump Bibli_monde
            python:
                remove_html(id)
                persistent.Quete_faite.append((quest_id, quest_nom))
            call screen ecran_victoire(quest_nom,gold_gagne,4)

            jump Bibli_monde
        "Abandonner":
            j "C'est dommage, peut-être une autre fois."
            jump Bibli_monde
