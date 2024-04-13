# Déclarez les personnages utilisés dans le jeu.
define c = Character(_("Client"), color="#c8ffc8")
define flash = Fade(.25, 0.0, .75, color="#fff")
define i= Character(_("????"), color="#000000")
define j= Character(_("Navi"), color="#92eb2c")
# Le jeu commence ici
label start:
    
    #play sound "voiture_qui_freine.mp3"
    "Je pense que c'est ici"

    scene maison_random with fade
    "C'est la dernière maison que je dois visiter et apres j'aurai droit à un weekend bien merité."

    #play sound "toc_toc.mp3"
    show client at right
    "Bonjour je suis le bricoleur que vous avez appellez pour reparer votre mur"

    "je me presente"

    python:
        name=renpy.input("je suis ")
        name=name.strip()
        if name == "":
            name="Bricoleur"

    "je suis [name]"

    define m= Character(_("[name]"),color="#0b29d4")

    c "Ah parfait je vous attendais, suivez moi"

    scene mur_suspect
    show client at right
    c "Voici le mur en question, il a l'air instable et j'ai peur qu'il s'effrondre"

    m "En effet, le mur a l'air .... suspect"

    m "Heureusement je suis le meilleur bricoleur des environs et je ferai de mon mieux pour le reparer grace a ma fidele boite à outils"

    "{i}Le client semble s'amuser à ma remarque{/i}"

    c "Bon et bien si vous travaillez aussi bien que vous parlez alors je vous fait confiance pour reparer tous ces problemes."

    c "Bonne chance"

    hide client with moveoutright
    "{i} Le client repart en ricanant {/i}"

    m "C'est vraiment un orignal ce client"

    m "Bon allons-y"

    "je me rapproche du mur et lorsque je tend ma main pour toucher le mur un immense flash de lumiere m'aveugle"
    
    scene black with fade

    i "...llez bien .."

    "Aaaah... ma tete"

    i "Reveillez-vous.... ouvrez les yeux ...."

    "J'ai l'impression qu'on m'appelle"

    scene forest
    show children
    "Au moment ou j'ouvre les yeux, je vois qu'une jeune fille se tient au-dessus moi"
    "Peut-etre qu'elle pourra m'aider a savoir ou je suis"

    m "...."

    "mais au moment ou j'ouvre la bouche aucun son ne sort"

    i "Vous allez bien monsieur ? Il semblerait que vous avez prit un coup sur la tete"

    i "Repetez lentement apres moi:"

    i 'print("je vais bien")'

    "Huh ? mais qu'est ce que raconte cette gamine"
label premiere:
    python:
        postData = {"valeur": "0"}
        url = 'http://127.0.0.1:5000'
        val = renpy.fetch(url, json = postData)
        url = "http://localhost/Python_Apprendre_Autrement/index2.html"
        lien = "{a="+url+"}Bon c'est pas grave, je vais quand meme essayer pour lui faire plaisir{/a}."
        renpy.say(None,lien)


    $ reussi = False
    python:
        # Remplacez l'URL ci-dessous par l'URL où votre script PHP est accessible
        url = "http://localhost/Python_Apprendre_Autrement/api.php"

        try:
            response = renpy.fetch(url, result="text")

            if response.strip() == "True":
                reussi = True
            else:
                renpy.say(None, "Essayer encore de cliquer sur le texte")
                reussi = False

        except Exception as erreur:
            # Gère les erreurs potentielles lors de la requête
            renpy.say(None, "Erreur lors de la requête : {}".format(str(erreur)))


    if reussi != True:
        jump premiere

    m "je vais bien"

    "Wow cette fois j'ai vraiment reussi a parler"

    show children happy
    i "Ah parfait vous semblez avoir repris les esprits"
    
    j "Je m'appelle Navi et vous, qui etes vous et comment ca se fait que vous etiez allongé sur le sol ? "

    "Je pense avoir compris le truc pour parler"

    m "Je m'appelle [name] et j'etais entrain de reparer un mur quand soudain je me suis retrouvé ici"

    j "Un mur ? Au plein milieu de cette foret ? mais le village le plus proche se trouve à plus de 30 minutes a pied d'ici"

    m "Un village ? mais ou est-je atterri ?"

    j "Vous etes actuellement au plein milieu de la foret des legendes et le village le plus proche s'appelle Stringfield"

    j "Avez-vous un endroit ou passer la nuit ou voulez-vous que je vous emmene à mon village ?"

    "Il semblerait que j'ai été transporté à un autre endroit mais je n'ai jamais entendu qu'une foret s'appellait \"foret des legendes\""

    "On dirait un nom sorti tout droit d'un jeu video..."

    "Attend une minute peut-etre que je n'ai pas été transporté juste dans un autre endroit mais plutot..."

    "Dans un autre monde ???!!!!!"

    "{i}Voyant mon visage inquiet Navi se rapproche{/i}"

    j "Ducoup vous avez un endroit ou dormir ?"

    m "Ah oui desolé j'etais perdu dans mes pensées, je n'ai nulle part ou aller donc j'accepte ta proposition"

    j "Parfait mais avant de rentrer je dois encore ceuillir de quoi manger ce soir"

    "{i}Quelques dizaines de minutes plus tard{/i}"

    j "J'ai ceuilli quelques champignons en plus mais je sais pas si ca sera assez car je suis pas tres bonne pour calculer"
    python:
        postData = {"valeur": "1"}
        url = 'http://127.0.0.1:5000'
        val = renpy.fetch(url, json = postData)
        url = "http://localhost/Python_Apprendre_Autrement/index2.html"
        lien = "{a="+url+"}Tu veux bien les compter ?{/a}."
        renpy.say(None,lien)

    $ reussi = False
    python:
        # Remplacez l'URL ci-dessous par l'URL où votre script PHP est accessible
        url = "http://localhost/Python_Apprendre_Autrement/api.php"

        try:
            response = renpy.fetch(url, result="text")

            if response.strip() == "True":
                #screen score  A faire
                reussi = True
            else:
                renpy.say(None, "Mauvaise reponse reessayer encore une fois")
                reussi = False

        except Exception as erreur:
            # Gère les erreurs potentielles lors de la requête
            renpy.say(None, "Erreur lors de la requête : {}".format(str(erreur)))


    if reussi != True:
        jump deuxieme
    
    j "Merci beaucoup !"

    j "On peut maintenant rentrer au village"

    "Sur le chemin vers le village Navi et moi avons fait plus ample connaissance et elle me compta aussi la raison pour laquelle cette foret s'appelle \"foret des legendes\""

