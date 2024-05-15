init python:
    import uuid
    import webbrowser
    import json
    
    cached_quests = None
    #Definitions des caractéristiques des écrans
    #Cases quetes
    style.quest_frame = Style(style.default)
    style.quest_frame.background = Frame("blue_background",xsize = 500, ysize = 200)
    style.quest_frame.xpadding = 10  # Espacement interne horizontal
    style.quest_frame.ypadding = 10  # Espacement interne vertical
    style.quest_frame.xmargin = 5  # Espacement externe horizontal
    style.quest_frame.ymargin = 5  # Espacement externe vertical
    style.quest_frame.xsize = 500
    style.quest_frame.ysize = 200
    
    style.quest_frame.box_wrap = True
    style.quest_frame.box_reverse = True
    style.quest_frame.box_spacing = 1  # Espace entre les bords de la boîte et le contenu

    # Définir un style personnalisé pour le bouton de retour
    style.retour_taverne = Style(style.default)
    style.retour_taverne.background = "#443322"
    style.retour_taverne.padding = (10, 5)  # Padding intérieur (vertical, horizontal)
    style.retour_taverne.margin = (5, 5)  # Marges autour du bouton
    
    style.titre_victoire = Style(style.default)
    style.titre_victoire.color = "#ffffff"
    style.titre_victoire.bold = True

    style.details_quete = Style(style.default)
    style.details_quete.color = "#ffff00"  # Jaune pour le texte


    style.details_or = Style(style.default)
    style.details_or.color = "#ffd700"  # Or


    style.details_score = Style(style.default)
    style.details_score.color = "#00ff00"  # Vert


    style.bouton_retour = Style(style.default)
    style.bouton_retour.background = "#333333"
    style.bouton_retour.color = "#ffffff"
    style.bouton_retour.padding = (5, 10)

    #Defini la taille de fenetre pour la taverne
    def calculate_rows(quests, cols):
            if quests == None:
                return (0 + cols - 1) // cols
            return (len(quests) + cols - 1) // cols
    
    # Envoie les données de la quête
    def handle_quest_and_redirect(quest, url,who,message,tavern,label):

        create_html(quest[0],id,who,message,tavern = tavern)
        renpy.call(label, quest[0],quest[1], url)
    
    #Recevoir quete tavern
    def load_quests(tavern):
        postData = {"quete":persistent.Quete_faite,"tavern":tavern}
        url = 'http://127.0.0.1:5000/get_mission_tavern'
        try:
            response = renpy.fetch(url, json=postData)
            decoded_response = response.decode('utf-8')
            json_data = json.loads(decoded_response)
            cached_quests = [(item[0], item[1], item[2]) for item in json_data]
        except Exception as erreur:
            # Gère les erreurs potentielles lors de la requête
            renpy.say(None, "Le serveur est éteint, reviens plus tard")
            return None
        return set(cached_quests)

    #Crée un id aleatoire pour le joueur
    def getid():
        return str(uuid.uuid4())
    id = getid()
    #Url de redirection de la page html
    site = "http://localhost/Python_Apprendre_Autrement/index_" + id + ".html"

    #Créer la page html
    def create_html(id_quest,id,who,message,tavern = 0):
        postData = {"valeur": id_quest, "id": id, "tavern" : tavern }
        url = 'http://127.0.0.1:5000'
        #Envoie de requete
        try:
            val = renpy.fetch(url, json = postData, result = "json")
            url = site
            lien = "{a="+url+"}"+message+"{/a}"
            if tavern == 0:
                #Affiche un message dans le jeu: (Qui parle, message)
                renpy.say(who,lien)
        except Exception as erreur:
            # Gère les erreurs potentielles lors de la requête
            renpy.say(None, "Le serveur est éteint, reviens plus tard")
            return None
        return val['name']
    
    #Verifier que la quete est réussie
    def verif_quete(id,chap = 0):
        url = 'http://127.0.0.1:5000/get_mission_state'
        reussi = None
        gold_gagne = None
        try:
            request = renpy.fetch(url , json ={"player_id":id}, result="json")
            
            reussi, gold_gagne = request['mission_state']
            if reussi:
                if chap == 1:
                    persistent.gold = persistent.gold + int(gold_gagne)
                elif chap == 2:
                    persistent.point_de_valeur = persistent.point_de_valeur + int(gold_gagne)
                elif chap == 3:
                    persistent.argent = persistent.argent + int(gold_gagne)
                elif chap == 4:
                    persistent.point_intelligence = persistent.point_intelligence + int(gold_gagne)
                persistent.score = persistent.score + int(gold_gagne)
            #renpy.say(j, "Waouw merci, tu as gagné [gold]")
            if not reussi:
                renpy.say(None, "Essaye encore de cliquer sur le texte")
                reussi = False

        except Exception as erreur:
            # Gère les erreurs potentielles lors de la requête
            renpy.say(None, "Je pense qu'il y a eu un probleme")
        
        return reussi,gold_gagne

    #Supprime la page Html
    def remove_html(id):
        url = 'http://127.0.0.1:5000/clear_quete'
        request= renpy.fetch(url, json = {"player_id":id}, result="json")

#Animation graphique

transform mymoveout(timing):
    linear timing xpos 2.0

transform myfade(timing):
    alpha 0.00
    linear timing alpha 1.00
transform tremble:
        alpha 1.0 xoffset 0
        choice:
            block:
                linear 0.05 xoffset 10
                linear 0.05 xoffset -10
                repeat 2
            block:    
                choice:
                    linear 0.05 xoffset 10
                    linear 0.05 xoffset -10
                    repeat 2
                choice:
                    linear 0.05 xoffset 10
                    linear 0.05 xoffset -10
                    linear 0.05 xoffset 10                    
                    repeat 2
        choice:
            block:
                linear 0.05 xoffset -10
                linear 0.05 xoffset 10
                repeat 2
            block:
                choice:
                    linear 0.05 xoffset -10
                    linear 0.05 xoffset 10
                    repeat 2        
                choice:
                    linear 0.05 xoffset -10                    
                    linear 0.05 xoffset 10
                    linear 0.05 xoffset -10
                    repeat 2
        linear 0.07 xoffset 0