# Le jeu commence ici
label start:
    play sound "door_opening.mp3"
    "Je pense que c'est ici."

    scene maison with fade
    "C'est la dernière maison que je dois visiter et après j'aurai droit à un weekend bien merité."

    play sound "triKnock01.mp3"
    show client at middleright
    c "Bonjour ?"

    "Bonjour, je suis le bricoleur que vous avez appelé pour réparer votre mur"

    "Je me présente"

    python:
        name=renpy.input("je suis ")
        name=name.strip()
        if name == "":
            name="Bricoleur"

    "Je suis [name]."

    

    c "Ah parfait ! Je vous attendais, suivez-moi."

    scene chamber
    show client at middleright
    show client at right with ease
    c "Voici le mur en question, il a l'air instable et j'ai peur qu'il s'effrondre."

    m "En effet, le mur a l'air .... suspect."

    m "Heureusement, je suis le meilleur bricoleur des environs et je ferai de mon mieux pour réparer votre mur grâce à ma fidèle boite à outils"
    
    show client content at right
    "{i}Le client semble s'amuser à ma remarque{/i}"

    c "Bon, et bien dans ce cas, je vous fais confiance."

    c "Bonne chance"

    hide client with moveoutright
    "{i} Le client repart en ricanant {/i}"

    m "Quel curieux personnage..."

    m "Bon, allons-y"

    "{i}Je décide alors de me rapprocher du mur mais tout à coup, un immense flash de lumière m'aveugle{i}"
    
    scene black with flash

    j "...llez bien .."

    "Aaaah... ma tête"

    j "Réveillez-vous.... ouvrez les yeux ...."

    "J'ai l'impression qu'on m'appelle"

    scene forest
    show Navi
    "Au moment où j'ouvre les yeux, je vois qu'une jeune fille se tient au-dessus moi"
    "Qu'est ce qu'elle fait la ?"

    m "...."

    "{i}Mais au moment où j'ouvre la bouche, aucun son ne sort{/i}"

    j "Vous allez bien monsieur ? J'ai l'impression que vous avez pris un coup sur la tête"

    j "Répétez lentement après moi:"

    j 'print("Je vais bien")'

    "Huh ? Mais qu'est ce qu'elle me raconte cette gamine?"
label premiere:
    python:
        nom_quete = create_html(0,id,m,"Je devrais peut-être lui faire plaisir")
        if nom_quete is None:
            renpy.jump("premiere")
        reussi = False
        reussi,gold_gagne = verif_quete(id)

    if reussi != True:
        jump premiere
    python:
        remove_html(id)

    call screen ecran_victoire(nom_quete,gold_gagne)
    m "Je vais bien"

    "Wow, cette fois j'ai réussi à parler"
    call screen debloquer(0)
    show Navi
    j "Ah, parfait. Vous semblez avoir repris vos esprits"

    $ Navi_name="Navi"
    
    j "Je m'appelle Navi et vous, qui êtes vous ? Comment ça se fait que vous étiez allongé sur le sol ? "

    "Je pense avoir compris le truc pour parler"

    m "Je m'appelle [name] et j'étais en train de réparer un mur quand soudain je me suis retrouvé ici"

    j "Un mur ? Au plein milieu de cette forêt ? Mais le village le plus proche se trouve à plus de 30 minutes à pied d'ici"

    m "Un village ? Mais où est ce que j'ai atterri ?"

    j "Vous êtes actuellement au plein milieu de la forêt des légendes et le village le plus proche s'appelle Stringfield"

    j "Avez-vous un endroit où passer la nuit ou voulez-vous que je vous emmène à mon village ?"

    "Il semblerait que j'ai été transporté à un autre endroit mais je n'ai jamais entendu qu'une forêt s'appellait \"forêt des légendes\""

    "On dirait un nom sorti tout droit d'un jeu vidéo..."

    "Attends une minute."

    "Peut-être que je n'ai pas été transporté juste dans un autre endroit mais plutôt..."

    "Dans un autre monde ???!!!!!"

    "{i}Voyant mon visage inquiet, Navi se rapproche{/i}"
    show Navi:
        ease 0.5 yalign 0.0 zoom 2.0
    
    j "Du coup, vous avez un endroit où dormir ?"

    m "Ah oui, désolé, j'étais perdu dans mes pensées. Je n'ai nulle part où aller donc j'accepte ta proposition"
    show Navi:
        ease 0.7 yalign 1.0 zoom 1.0
    j "Parfait mais avant de rentrer, je dois encore cueillir de quoi manger ce soir"

    "{i}Quelques dizaines de minutes plus tard{/i}"

    j "J'ai cueilli trois types de champignons mais je ne sais pas si ça sera assez car je ne suis pas très bonne pour calculer"

    call screen debloquer(1)

label deuxieme:
    python:
        nom_quete = create_html(1,id,j,"Peux-tu les compter pour moi ?")
        if nom_quete is None:
            renpy.jump("deuxieme")
        reussi = False
        reussi,gold_gagne = verif_quete(id)

    if reussi != True:
        jump deuxieme
    python:
        remove_html(id)

    call screen ecran_victoire("Compte les champignons",gold_gagne)

    j "Merci beaucoup !"

    j "On peut maintenant rentrer au village"

    "Sur le chemin vers le village, Navi et moi avons fait plus amples connaissances"

    m "D'ailleurs, tu sais pourquoi cette forêt s'appelle la \"forêt des légendes\" ?"

    j "Oui, bien sûr, ça vient d'une ancienne histoire que mon grand-père me racontait"
    scene black with fade
    j "Voici l'histoire de ce monde :"

    j "Il y a fort fort longtemps, à une époque où l'humanité n'était encore que dans son stade le plus primitif"
    scene ourobors with fade
    j "Ouroboros le Serpent du Temps, un être divin d'une puissance infinie, décida dans un geste de générosité d'octroyer aux humains des artéfacts d'une puissance incommensurable"

    j "Il donna alors des outils divins à certains élus avec, pour seule exigence, qu'ils soient utilisés avec sagesse et compassion, pour le bien de tous les êtres vivants"

    j "Ces outils étaient nommés \"Les fonctions divines\""

    j "Grâce à ces outils, les élus ont multiplié les récoltes, ont toujours pu faire le meilleur choix ou ont encore pu automatiser des tâches qui étaient auparavant pénibles"

    j "L'humanité a alors régné en maître sur la nature pendant des centaines voire des milliers d'années"

    j "Cependant, l'orgueil et l'avidité des humains finirent par corrompre leurs cœurs, détournant les bénédictions du Serpent du Temps à des fins égoïstes et destructrices"

    j "Voyant sa confiance bafouée, le Serpent du Temps rentra dans une colère noire et punit l'humanité en tuant les élus, en récuperant les artéfacts divins et en faisant régner le chaos sur Terre"

    j "Mais dans ce chaos constant, tout espoir n'était pas perdu. En effet, un oracle a prophétisé qu'un héros apparaitra un jour dans la fôret dans laquelle nous sommes"

    j "Cet héros sera destiné à nous libérer du joug du Serpent du Temps et ainsi ramener la paix et la prospérité à l'humanité"
    
    scene black with fade
    "Wow, l'histoire de ce monde est lourde"

    j "Ah! Je vois les portes du village"

    scene village far fire with hpunch

    m "Mais dis-moi, c'est normal qu'il y ait autant de fumée qui vienne du village ?"

    j "Non, ce n'est pas normal! Je pense que le village est en feu, dépêchons-nous"
    jump village_en_feu