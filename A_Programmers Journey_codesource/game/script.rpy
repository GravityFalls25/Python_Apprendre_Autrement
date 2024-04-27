# Déclarez les personnages utilisés dans le jeu.
define c = Character(_("Client"), color="#c8ffc8")
define flash = Fade(.25, 0.0, .75, color="#fff")
define i= Character(_("????"), color="#ffffff")
define j= Character(_("Navi"), color="#92eb2c")

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
        postData = {"valeur": quest_id}
        url = 'http://127.0.0.1:5000'
        response = renpy.fetch(url, json=postData)
        # if response.status == 200:
        #     return response.json()  # Traitez la réponse comme nécessaire
        # else:
        #     renpy.error("Erreur de requête: {}".format(response.status))
    def handle_quest_and_redirect(quest_id, url):
    # Envoie les données de la quête
        send_quest_data(quest_id)
        renpy.call("dialogue_aubergiste", quest_id, url)
    def load_quests():
        #print("Je passe surement ici pour rien")

        global cached_quests
        
        if voir_tavern_quete:
            #print("J'ai quand meme reussi a passer")
            if cached_quests is None:
                postData = list(Quete_faite)
                url = 'http://127.0.0.1:5000/get_mission_tavern'
                response = renpy.fetch(url, json=postData)
                decoded_response = response.decode('utf-8')
                json_data = json.loads(decoded_response)
                cached_quests = [(item[0], item[1], item[2]) for item in json_data]
            return set(cached_quests)
        return None

    Quete_faite = set()

    def getid():
        return str(uuid.uuid4())
    id = getid()

    def calculate_rows(quests, cols):
            return (len(quests) + cols - 1) // cols

screen quest_menu(id_tavern):
        python:
            quests = load_quests()
            voir_tavern_quete = False
            


            # Convertir la liste de tuples en un ensemble
        frame:
            
            background Solid("#000000ae")
            
            vbox:
                
                spacing 5
                textbutton "Retour à la taverne" action Jump("tavern_village") style "retour_taverne"
                viewport:
                    draggable True
                    scrollbars "vertical"
                    mousewheel True
                    
                    grid 3 calculate_rows(quests, 3):  # Dynamiquement calculé
                        spacing 10
                        python:
                            #liste_quete = sorted(list(quests), key=lambda x: float(x[1]))
                            liste_quete = sorted(list(quests))
                        for quest in liste_quete:
                            frame:
                                style "quest_frame"
                                vbox:
                                        text quest[0]
                                        text "Difficulté: {}".format(quest[2])
                                        textbutton quest[1] action Function(handle_quest_and_redirect, quest[0], "http://localhost/Python_Apprendre_Autrement/index2.html")
    


# Le jeu commence ici
label start:
    
    #play sound "voiture_qui_freine.mp3"
    "Je pense que c'est ici"

    scene maison with fade
    "C'est la dernière maison que je dois visiter et après j'aurai droit à un weekend bien merité."

    #play sound "toc_toc.mp3"
    define m= Character(_("[name]"),color="#0b29d4")
    show client at right
    c "Bonjour ?"

    "Bonjour je suis le bricoleur que vous avez appelé pour réparer votre mur"

    "Je me presente"

    python:
        name=renpy.input("je suis ")
        name=name.strip()
        if name == "":
            name="Bricoleur"

    "Je suis [name]"

    

    c "Ah parfait je vous attendais, suivez moi"

    scene chamber
    show client at right
    c "Voici le mur en question, il a l'air instable et j'ai peur qu'il s'effrondre"

    m "En effet, le mur a l'air .... suspect"

    m "Heureusement je suis le meilleur bricoleur des environs et je ferai de mon mieux pour reparer votre grâce à ma fidele boite à outils"

    "{i}Le client semble s'amuser à ma remarque{/i}"

    c "Bon et bien dans ce cas, je vous fait confiance."

    c "Bonne chance"

    hide client with moveoutright
    "{i} Le client repart en ricanant {/i}"

    m "Quel curieux personnage..."

    m "Bon allons-y"

    "{i}Je décide alors de me rapprocher du mur mais lorsque tout à coup, un immense flash de lumiere m'aveugla{i}"
    
    scene black with fade

    i "...llez bien .."

    "Aaaah... ma tete"

    i "Reveillez-vous.... ouvrez les yeux ...."

    "J'ai l'impression qu'on m'appelle"

    scene forest
    show children
    "Au moment où j'ouvre les yeux, je vois qu'une jeune fille se tient au-dessus moi"
    "Qu'est ce qu'elle fait la ?"

    m "...."

    "{i}mais au moment où j'ouvre la bouche aucun son ne sort{i}"

    i "Vous allez bien monsieur ? J'ai l'impression que vous avez pris un coup sur la tete"

    i "Répétez lentement apres moi:"

    i 'print("je vais bien")'

    "Huh ? mais qu'est ce qu'elle me raconte cette gamine"
label premiere:
    python:
        
        postData = {"valeur": "0", "id":id}
        url = 'http://127.0.0.1:5000'
        val = renpy.fetch(url, json = postData)
        url = "http://localhost/Python_Apprendre_Autrement/index2.html"
        lien = "{a="+url+"}Bon c'est pas grave, je vais quand meme essayer pour lui faire plaisir{/a}"
        renpy.say(None,lien)


    $ reussi = False
    python:
        # Remplacez l'URL ci-dessous par l'URL où votre script PHP est accessible
        url = 'http://127.0.0.1:5000/get_mission_state'

        try:
            request = renpy.fetch(url , json ={"player_id":id}, result="json")
            
            reussi, gold = request['mission_state']
            renpy.say(None, "Tu as gagné [gold]")
            if not reussi:
                renpy.say(None, "Essayer encore de cliquer sur le texte")
                reussi = False

        except Exception as erreur:
            # Gère les erreurs potentielles lors de la requête
            renpy.say(None, "Erreur lors de la requête : {}".format(str(erreur)))


    if reussi != True:
        jump premiere

    m "Je vais bien"

    "Wow cette fois j'ai réussi à parler"

    show children
    i "Ah parfait vous semblez avoir repris vos esprits"
    
    j "Je m'appelle Navi et vous, qui êtes vous ? Comment ça se fait que vous étiez allongé sur le sol ? "

    "Je pense avoir compris le truc pour parler"

    m "Je m'appelle [name] et j'etais en train de réparer un mur quand soudain je me suis retrouvé ici"

    j "Un mur ? Au plein milieu de cette foret ? Mais le village le plus proche se trouve à plus de 30 minutes à pied d'ici"

    m "Un village ? Mais où est ce que j'ai atterri ?"

    j "Vous êtes actuellement au plein milieu de la forêt des legendes et le village le plus proche s'appelle Stringfield"

    j "Avez-vous un endroit où passer la nuit ou voulez-vous que je vous emmène à mon village ?"

    "Il semblerait que j'ai été transporté à un autre endroit mais je n'ai jamais entendu qu'une foret s'appellait \"foret des legendes\""

    "On dirait un nom sorti tout droit d'un jeu video..."

    "Attend une minute."

    "Peut-etre que je n'ai pas été transporté juste dans un autre endroit mais plutot..."

    "Dans un autre monde ???!!!!!"

    "{i}Voyant mon visage inquiet Navi se rapproche{/i}"

    j "Du coup, vous avez un endroit où dormir ?"

    m "Ah oui desolé j'étais perdu dans mes pensées, je n'ai nulle part où aller donc j'accepte ta proposition"

    j "Parfait mais avant de rentrer je dois encore cueillir de quoi manger ce soir"

    "{i}Quelques dizaines de minutes plus tard{/i}"

    j "J'ai cueilli quelques champignons en plus mais je sais pas si ça sera assez car je suis pas très bonne pour calculer"
label deuxieme:
    python:
        
        postData = {"valeur": "1", "id": id}
        url = 'http://127.0.0.1:5000'
        val = renpy.fetch(url, json = postData)
        url = "http://localhost/Python_Apprendre_Autrement/index2.html"
        lien = "{a="+url+"}Tu veux bien les compter ?{/a}"
        renpy.say(None,lien)

    $ reussi = False
    python:
        # Remplacez l'URL ci-dessous par l'URL où votre script PHP est accessible
        url = 'http://127.0.0.1:5000/get_mission_state'

        try:
            request= renpy.fetch(url, json = {"player_id":id}, result="json")
            reussi, gold = request['mission_state']
            renpy.say(None, "Waouw merci, tu as gagné [gold]")
            if not reussi:
                renpy.say(None, "Mauvaise reponse reessayer encore une fois")
                reussi = False
                

        except Exception as erreur:
            # Gère les erreurs potentielles lors de la requête
            renpy.say(None, "Erreur lors de la requête : {}".format(str(erreur)))


    if reussi != True:
        jump deuxieme
    
    j "Merci beaucoup !"

    j "On peut maintenant rentrer au village"

    "Sur le chemin vers le village Navi et moi avons fait plus ample connaissance"

    m "D'ailleurs tu sais pourquoi cette foret s'appelle la \"forêt des legendes\" ?"

    j "Oui bien sur, ça vient d'une ancienne histoire que mon grand-pere me racontait"

    j "Il y a fort longtemps quand l'humanité n'était encore que dans son stade le plus primitif, le Serpent du Temps, un être divin d'une puissance infinie, décida dans un geste de générosité d'octroyer aux humains des artefacts d'une puissance incommensurable"

    j "Il donna alors des outils divins à certains élus avec,pour seule exigence, qu'ils soient utilisés avec sagesse et compassion, pour le bien de tous les êtres vivants"

    j "Ces outils étaient nommés \"Les fonctions divines\""

    j "Grace à ces outils, les élus ont multiplié les recoltes, ont toujours pu faire le meilleur choix ou ont encore pu automatisé des taches qui etaient auparavant pénibles"

    j "L'humanité a alors regné en maitre sur la nature pendant des centaines voire des milliers d'années"

    j "Cependant, l'orgueil et l'avidité des humains finirent par corrompre leurs cœurs, détournant les bénédictions du Serpent du Temps à des fins égoïstes et destructrices"

    j "Voyant sa confiance baffouée, le Serpent du Temps rentra dans une colere noire et punissa l'humanité en tuant les elus, en recuperant les artifacts divins et en faisant regner le chaos sur terre"

    j "Mais dans ce chaos constant, tout espoir n'était pas perdu. En effet, un oracle a prophetisé qu'un hero apparaitra un jour dans la foret dans laquelle nous sommes"

    j "Cet hero sera destiné à nous liberer du joug du Serpent du Temps et ainsi ramenant la paix et la prosperité à l'humanité"

    "Wow l'histoire de ce monde est lourde"

    j "Ah! je vois les portes du village"

    scene village far fire

    m "Mais dis-moi c'est normal qu'il y ait autant de fumée qui vienne du village ?"

    j "Non ce n'est pas normal, je pense que le village est en feu, depechons-nous"

    scene village fire

    "Quelle scene apocalyptique, il y a plusieurs maisons en feu"


label troisieme:
    python:
        postData = {"valeur": "2"}
        url = 'http://127.0.0.1:5000'
        val = renpy.fetch(url, json = postData)
        url = "http://localhost/Python_Apprendre_Autrement/index2.html"
        lien = "{a="+url+"}Vite il y a un puit la-bas, va chercher de l'eau{/a}"
        renpy.say(j,lien)

    $ reussi = False
    python:
        # Remplacez l'URL ci-dessous par l'URL où votre script PHP est accessible
        url = 'http://127.0.0.1:5000/get_mission_state'

        try:
            request= renpy.fetch(url, json = {"player_id":id}, result="json")
            reussi, gold = request['mission_state']
            renpy.say(j, "Waouw merci, tu as gagné [gold]")
            if not reussi:
                renpy.say(None, "Mauvaise reponse reessayer encore une fois")
                reussi = False
                

        except Exception as erreur:
            # Gère les erreurs potentielles lors de la requête
            renpy.say(None, "Erreur lors de la requête : {}".format(str(erreur)))


    if reussi != True:
        jump troisieme
    
    j "Ouf, je pense qu'on a reussi à controler l'incendie mais qu'est ce qui a bien pu causer ca ?"

    define v= Character(_("Villageois"), color="#446d14")
    
    v ""
    jump tavern_village

label dialogue_aubergiste(quest_id, url):
    T " Bonjour, bon courage pour la quête!"
    menu:
        "Commencer la quête":
            T "Parfait, voici les détails..."
            $ webbrowser.open(url)  # Redirige vers la page web si validé
            call quete_aubergiste(quest_id, url)
        "Annuler":
            T " C'est dommage, peut-être une autre fois."
            jump tavern_village
label quete_aubergiste(quest_id, url):
    T " Bonjour, bon courage pour la quête!"
    menu:
        "Valider la quête":
            
            
            jump tavern_village
        "Abandonner":
            T " C'est dommage, peut-être une autre fois."
            jump tavern_village

label tavern_village:
    define T= Character(_("Tavernier"), color="#446d14")
    scene tavern
    show tavernier

    T "Bienvenue dans ma taverne que puis je faire pour vous"
    menu: 
        "Voir les quetes disponibles":
            $ voir_tavern_quete = True
            call screen quest_menu(0)
        "Repartir":
            $ voir_tavern_quete = False
            return
    