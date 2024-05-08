init python:
    import uuid
    import webbrowser
    import json
    
    cached_quests = None
    #Cases quetes
    style.quest_frame = Style(style.default)
    style.quest_frame.background = Frame("blue_background",xsize = 500, ysize = 200)
    #style.quest_frame.background = "#1c2de3"  # Couleur de fond
    style.quest_frame.xpadding = 10  # Espacement interne horizontal
    style.quest_frame.ypadding = 10  # Espacement interne vertical
    style.quest_frame.xmargin = 5  # Espacement externe horizontal
    style.quest_frame.ymargin = 5  # Espacement externe vertical
    style.quest_frame.xsize = 500
    style.quest_frame.ysize = 200
    
    #
    style.quest_frame.box_wrap = True
    style.quest_frame.box_reverse = True
    style.quest_frame.box_spacing = 1  # Espace entre les bords de la boîte et le contenu

    # Définir un style personnalisé pour le bouton de retour
    style.retour_taverne = Style(style.default)
    style.retour_taverne.background = "#443322"  # Couleur de fond marron
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


    def send_quest_data(quest_id):
        postData = {"valeur": quest_id, "id":id}
        url = 'http://127.0.0.1:5000'
        response = renpy.fetch(url, json=postData)
        # if response.status == 200:
        #     return response.json()  # Traitez la réponse comme nécessaire
        # else:
        #     renpy.error("Erreur de requête: {}".format(response.status))
    def handle_quest_and_redirect(quest, url,who,message,tavern,label):
    # Envoie les données de la quête
 
        create_html(quest[0],id,who,message,tavern = tavern)
        renpy.call(label, quest[0],quest[1], url)
    def load_quests(tavern):
        postData = {"quete":persistent.Quete_faite,"tavern":tavern}
        url = 'http://127.0.0.1:5000/get_mission_tavern'
        response = renpy.fetch(url, json=postData)
        decoded_response = response.decode('utf-8')
        json_data = json.loads(decoded_response)
        cached_quests = [(item[0], item[1], item[2]) for item in json_data]
        return set(cached_quests)

    
    def getid():
        return str(uuid.uuid4())
    id = getid()
    site = "http://localhost/Python_Apprendre_Autrement/index_" + id + ".html"

    def calculate_rows(quests, cols):
            return (len(quests) + cols - 1) // cols

    def create_html(id_quest,id,who,message,tavern = 0):
        postData = {"valeur": id_quest, "id": id, "tavern" : tavern }
        url = 'http://127.0.0.1:5000'
        val = renpy.fetch(url, json = postData, result = "json")
        url = site
        lien = "{a="+url+"}"+message+"{/a}"
        if tavern == 0:
            renpy.say(who,lien)
        return val['name']
    
    def verif_quete(id):
        url = 'http://127.0.0.1:5000/get_mission_state'
        reussi = None
        gold_gagne = None
        try:
            request = renpy.fetch(url , json ={"player_id":id}, result="json")
            
            reussi, gold_gagne = request['mission_state']
            persistent.gold = persistent.gold + int(gold_gagne)
            #renpy.say(j, "Waouw merci, tu as gagné [gold]")
            if not reussi:
                renpy.say(None, "Essaye encore de cliquer sur le texte")
                reussi = False

        except Exception as erreur:
            # Gère les erreurs potentielles lors de la requête
            renpy.say(None, "Erreur lors de la requête : {}".format(str(erreur)))
        
        return reussi,gold_gagne

    def remove_html(id):
        url = 'http://127.0.0.1:5000/clear_quete'
        request= renpy.fetch(url, json = {"player_id":id}, result="json")
