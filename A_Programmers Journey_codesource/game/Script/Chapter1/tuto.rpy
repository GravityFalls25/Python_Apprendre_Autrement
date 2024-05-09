# Le jeu commence ici
label start:
    play sound "door_opening.mp3"
    "Je pense que c'est ici"

    scene maison with fade
    "C'est la dernière maison que je dois visiter et après j'aurai droit à un weekend bien merité."

    play sound "triKnock01.mp3"
    show client at middleright
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
    show client at middleright
    show client at right with ease
    c "Voici le mur en question, il a l'air instable et j'ai peur qu'il s'effrondre"

    m "En effet, le mur a l'air .... suspect"

    m "Heureusement je suis le meilleur bricoleur des environs et je ferai de mon mieux pour reparer votre grâce à ma fidele boite à outils"
    
    show client content at right
    "{i}Le client semble s'amuser à ma remarque{/i}"

    c "Bon et bien dans ce cas, je vous fait confiance."

    c "Bonne chance"

    hide client with moveoutright
    "{i} Le client repart en ricanant {/i}"

    m "Quel curieux personnage..."

    m "Bon allons-y"

    "{i}Je décide alors de me rapprocher du mur mais lorsque tout à coup, un immense flash de lumiere m'aveugla{i}"
    
    scene black with flash

    j "...llez bien .."

    "Aaaah... ma tete"

    j "Reveillez-vous.... ouvrez les yeux ...."

    "J'ai l'impression qu'on m'appelle"

    scene forest
    show Navi
    "Au moment où j'ouvre les yeux, je vois qu'une jeune fille se tient au-dessus moi"
    "Qu'est ce qu'elle fait la ?"

    m "...."

    "{i}mais au moment où j'ouvre la bouche aucun son ne sort{/i}"

    j "Vous allez bien monsieur ? J'ai l'impression que vous avez pris un coup sur la tete"

    j "Répétez lentement apres moi:"

    j 'print("je vais bien")'

    "Huh ? mais qu'est ce qu'elle me raconte cette gamine"
label premiere:
    python:
        nom_quete = create_html(0,id,m,"Je devrais peut etre lui faire plaisir")
        reussi = False
        reussi,gold_gagne = verif_quete(id)

    if reussi != True:
        jump premiere
    python:
        remove_html(id)

    call screen ecran_victoire(nom_quete,gold_gagne,persistent.gold)
    m "Je vais bien"

    "Wow cette fois j'ai réussi à parler"
    call screen debloquer
    show Navi
    j "Ah parfait vous semblez avoir repris vos esprits"

    $ Navi_name="Navi"
    
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
    show Navi:
        ease 0.5 yalign 0.0 zoom 2.0
    
    j "Du coup, vous avez un endroit où dormir ?"

    m "Ah oui desolé j'étais perdu dans mes pensées, je n'ai nulle part où aller donc j'accepte ta proposition"
    show Navi:
        ease 0.7 yalign 1.0 zoom 1.0
    j "Parfait mais avant de rentrer je dois encore cueillir de quoi manger ce soir"

    "{i}Quelques dizaines de minutes plus tard{/i}"

    j "J'ai cueilli quelques champignons en plus mais je sais pas si ça sera assez car je suis pas très bonne pour calculer"
label deuxieme:
    python:
        nom_quete = create_html(1,id,j,"Peux tu les compter pour moi?")
        reussi = False
        reussi,gold_gagne = verif_quete(id)

    if reussi != True:

        jump deuxieme
    python:
        remove_html(id)

    call screen ecran_victoire("Compte les champignons",gold_gagne,persistent.gold)

    j "Merci beaucoup !"

    j "On peut maintenant rentrer au village"

    "Sur le chemin vers le village Navi et moi avons fait plus ample connaissance"

    m "D'ailleurs tu sais pourquoi cette foret s'appelle la \"forêt des legendes\" ?"

    j "Oui bien sur, ça vient d'une ancienne histoire que mon grand-pere me racontait"
    scene black with fade
    j "Voici l'histoire de ce monde :"

    j "Il y a fort fort longtemps à une époque où l'humanité n'était encore que dans son stade le plus primitif"
    scene ourobors with fade
    j "Ouroboros le Serpent du Temps, un être divin d'une puissance infinie, décida dans un geste de générosité d'octroyer aux humains des artefacts d'une puissance incommensurable"

    j "Il donna alors des outils divins à certains élus avec,pour seule exigence, qu'ils soient utilisés avec sagesse et compassion, pour le bien de tous les êtres vivants"

    j "Ces outils étaient nommés \"Les fonctions divines\""

    j "Grace à ces outils, les élus ont multiplié les recoltes, ont toujours pu faire le meilleur choix ou ont encore pu automatisé des taches qui etaient auparavant pénibles"

    j "L'humanité a alors regné en maitre sur la nature pendant des centaines voire des milliers d'années"

    j "Cependant, l'orgueil et l'avidité des humains finirent par corrompre leurs cœurs, détournant les bénédictions du Serpent du Temps à des fins égoïstes et destructrices"

    j "Voyant sa confiance baffouée, le Serpent du Temps rentra dans une colere noire et punissa l'humanité en tuant les elus, en recuperant les artifacts divins et en faisant regner le chaos sur terre"

    j "Mais dans ce chaos constant, tout espoir n'était pas perdu. En effet, un oracle a prophetisé qu'un hero apparaitra un jour dans la foret dans laquelle nous sommes"

    j "Cet hero sera destiné à nous liberer du joug du Serpent du Temps et ainsi ramenant la paix et la prosperité à l'humanité"
    
    scene black with fade
    "Wow l'histoire de ce monde est lourde"

    j "Ah! je vois les portes du village"

    scene village far fire with hpunch

    m "Mais dis-moi c'est normal qu'il y ait autant de fumée qui vienne du village ?"

    j "Non ce n'est pas normal, je pense que le village est en feu, depechons-nous"
    jump village_en_feu