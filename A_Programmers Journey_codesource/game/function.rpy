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
    
    def send_quest_data(quest_id):
        postData = {"valeur": quest_id, "id":id}
        url = 'http://127.0.0.1:5000'
        response = renpy.fetch(url, json=postData)
        # if response.status == 200:
        #     return response.json()  # Traitez la réponse comme nécessaire
        # else:
        #     renpy.error("Erreur de requête: {}".format(response.status))
    def handle_quest_and_redirect(quest, url):
    # Envoie les données de la quête
        send_quest_data(quest[0])
        renpy.call("dialogue_aubergiste", quest[0],quest[1], url)
    def load_quests():
        postData = persistent.Quete_faite
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
