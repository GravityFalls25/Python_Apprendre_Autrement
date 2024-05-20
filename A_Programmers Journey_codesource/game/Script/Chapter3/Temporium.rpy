label Temporium:
    scene black with fade
    "Nous sommes enfin arrivé aux portes de Temporium apres un voyage qui m'a semblé interminable"

    scene entree_ville with fade
    show garde

    garde "Halte la, declinez votre identité"

    j "Nous sommes des voyageurs à la recherche de la bibliotheque-monde, Je m'appelle Navi et suis accompagné de [name]"

    garde "Tres bien, vous pouvez rentrer"
    scene black with fade
    "Nous passons l'entrée de la ville"
    play sound "rezero-respawn.mp3"
    scene entree_ville with fade
    m "Tiens, tu as entendu ca ?"
    j "Entendu quoi ?"
    show garde at left
    #boucle 1
    garde "Ca faisait longtemps que nous n'avions plus de visiteur, la bibliotheque se trouve au bout de ce chemin, passez un agreable sejour"

    scene ville_et_vendeuse with fade
    "{i}Nous avancons alors sur le chemin indiqué par le garde{/i}"

    show fermier at tremble,center
    fermier "Blep"
    "Je vois un jeune homme de l'autre coté de la route étalé sur le sol couvert de boue"
    fermier "Vous pourriez quand meme faire attention"
    "Au moment où il dit ca une charette passant à vive allure écrasa ses pommes"
    fermier "Oh non mes pommes"

    "En voila un qui n'a pas de chance. Heureusement, il n'a pas l'air d'etre blessé mais ses pommes sont irrecuperables, il n'y a rien que je puisse faire"
    hide fermier
    "Continuons d'avancer"
    show vendeuse at right
    vendeuse "Approchez, approchez, venez voir mes produits venant des quatres coins du monde"

    m "Oh ce stand à l'air interressant, il vend plein de produits que je n'ai jamais vu"

    j "Malheureusement, notre argent ne vaut rien ici, il faudra à nouveau faire des quetes pour gagner l'argent qui fonctionnera dans cette ville"

    j "Mais on fera ca plus tard, pour l'instant concentrons-nous sur la bibliotheque"

    scene black with fade
    "Nos arrivames enfin en face de l'immense bibliotheque-monde"

    scene bibli with fade
    m "Wow, cette bibliotheque est vraiment immense !"
    m "Mais c'est quoi ce papier sur la porte ?"

    show papier at myfade(1.0), center

    m "Il semblerait qu'elle soit fermée pour aujourd'hui"

    j "Quel dommage !"
    
    j "C'est pas tres grave louons une chambre d'auberge en attendant. De plus, ca nous permettra de nous reposer de notre long periple"

    scene black with fade

    "Nous nous dirigeames vers l'auberge la plus proche"

    scene auberge with fade

    m "Bonjour, nous voudrions louer deux chambres pour passer la nuit"

    show female_tavernier
    A "Bien sur, les chambres sont à l'étage voici les clés"

    A "Reposez vous bien!"

    scene black with fade
    m "Je suis vraiment extenué, j'ai l'impression que je pourrais m'écrouler à tout moment"

    m "D'un autre coté, ça fait longtemps que je me suis pas autant amusé"
    # ça me change quand meme beaucoup de d'habitude
    m "Je me demande combien de temps s'est passé dans mon monde originel"

    "C'est sur cette pensée que je fini par m'assoupir"

    scene chambre_auberge
    play sound "crash_door.mp3" volume 0.9
    pause 2.0
    show Navi inquiet with moveinright
    j "Vite reveille-toi un truc horrible est en train de se passer !"

    m "Hein quoi qu'est-ce qui se passe ?"

    j "La bibliotheque-monde est en feu !"

    scene bibli_feu_soir with hpunch
    show Navi inquiet at right

    j "Allons vite voir de plus pres"

    "Nous nous precipitames sans meme prendre le temps de nous preparer mais le temps d'arriver à la bibliotheque, elle etait deja reduite en cendre"

    "On essaye quand meme de fouiller dans les debris pour voir si un livre a survecu mais rien a y faire, tout est irrecuperable"

    j "Oh non comment vas-t'on faire maintenant. C'etait le seul moyen de savoir où se trouvait Ouroboros et comment le vaincre"

    m "Retournons nous coucher, on trouvera une solution demain, à tete reposée"

    scene black with fade
    "On retourna dans nos chambres respectives mais comment trouver le sommeil apres ce qui vient de se passer ?"

    #2eme boucle
    play sound "rezero-respawn.mp3"
    scene entree_ville
    show garde at left
    m "Hein quoi où suis-je, comment je suis arrivé la ?"

    garde "Ca faisait longtemps que nous avions plus de visiteur, la bibliotheque se trouve au bout de ce chemin, passez un agreable sejour"

    "J'ai comme une impression de deja-vu"

    scene ville_et_vendeuse with fade
    "Nous avancons tout de meme sur le chemin indiqué par le garde"

    show Navi 
    j "Hey, tu sais comment on est retourné à l'entrée de la ville ?"

    m "Non je n'ai aucune idée et en plus, regarde au bout de ce chemin, ce n'est pas la bibliotheque que l'on a vu bruler hier soir ?"

    j "Peut-etre qu'on en saura plus si on se rapproche de la bibliotheque"
    hide Navi
    show fermier at tremble,center
    fermier "Blep"
    "C'est le meme jeune homme qu'hier qui est encore etalé au sol, couvert de boue"
    fermier "Vous pourriez quand meme faire attention"
    "Et encore une fois, une charette ecrasa ses pommes"
    fermier "Oh non mes pommes"
    hide fermier
    "On continue d'avancer"

    show vendeuse at right
    vendeuse "Approchez, approchez, venez voir mes produits venant des quatres coins du monde"

    "Le vendeuse est elle aussi encore la"

    scene black with fade
    "On arriva enfin en face de l'immense bibliotheque-monde"

    scene bibli with fade
    m "Le papier est toujours la"
    show papier at myfade(1.0), center

    m "Voila qui confirme mes soupcons, le jour n'a pas changé, d'une facon ou d'une autre nous avons remonté le temps"
    hide papier
    show Navi
    m "Tu sais ce qui a pu causer ca Navi ?"

    j "Je pense que c'est du à la capacité d'une des fonctions divines"

    j "Je suspecte l'utilisation de boucles"

    m "Et quels sont les effets d'une boucle ?"

    j "Si l'outil utilisé est le for alors on risque de repeter une boucle temporelle un nombre bien precis de fois mais dans le cas ou c'est un while..."

    j "Alors nous vivrons la meme journée jusqu'à la fin des temps"

    m "Est ce qu'il a un moyen de sortir d'une boucle ?"

    j "Oui c'est possible, mais pour ça, il nous faut un break"

    m "Comment ca se fait que tu saches autant de choses ?"

    j "Mon grand-pere était passionné par les fonctions divines et il en parlait à longueur de journée"

    j "Son reve etait de pouvoir copier les effets des fonctions divines malgres le fait qu'on y avait plus acces"

    m "Et il a reussi ?"

    j "Malheureusement, il n'a jamais reussi à copier les effets de fonctions plus complexe car selon lui \"Il faut ressentir les effets d'une fonction avant de pouvoir la recreer\""
    
    m "Je vois...."

    m "Mais dis-moi, la on ressent bien les effets de cette fonction, tu penses qu'on serait capable de la recreer ?"

    j "Theoriquement, oui, tu penses en etre capable ?"

    m "Bien sur ! Apres tout je suis le meilleur bricoleur des environs"

    "{i}Navi rigole legerement{/i}"

    j "Tres bien alors, laisse moi t'aider"

    scene black with fade

    "Quelques heures plus tard"

    scene bibli_soir with fade
    m "Ca nous aura prit tout le reste de la journée mais on a enfin reussi à copier les effets des boucles"

    call screen debloquer(3)

    j "Malheuresement quand bien meme on sait creer des boucles, on ne sait toujours pas comment en sortir d'une"

    m "Au moins on sera pret pour la prochaine fois que la boucle recommencera"

    m "Mais avant que cette itération ne se finisse, il faut decouvrir pourquoi la bibliotheque a prit feu"

    #play sound "start_fire.mp3"
    scene bibli_feu_soir with hpunch
    j "Il semblerait qu'on s'y prenne trop tard"

    m "Vite fait le tour du batiment par la gauche et essaie de voir si il y a quelque chose de suspect, moi je ferai le tour par la droite"

    "{i}Au moment où j'arrive devant le batiment, une figure encapuchonnée sort à toute vitesse de la bibliotheque {/i}"

    m "Hey vous, arretez-vous !"

    "En me voyant arriver le suspect accelere, j'essaye de le poursuivre mais il finit par me semer"

    m "Mince, il m'a filé entre les doigts mais au moins je sais maintenant que ce n'etait pas un accident mais bien un acte criminel"

    m "De plus, si c'est de sa faute qu'on soit coincé dans une boucle alors il possede surement aussi le moyen pour en sortir"

    m "Et pour finir, je sais par où il est passé donc je pourrais lui tendre un piege lors de la prochaine iteration mais il me faudra des outils et du materiel"

    scene black with fade
    m "Je pense qu'on est pret pour la prochaine iteration"

    $ parler_garde_global=False
    $ quete_forgeron=False
    $ quete_auberge_global=False
    $ quete_pomme=False
label debut_boucle:
    play sound "rezero-respawn.mp3"
    scene entree_ville
    $ parler_garde=False
    $ quete_auberge=False
    $ filet=False
    $ pelle=False
    $ paille=False
    $ lance= False
    $ argent_actuel=0
    $ heure=8
    show garde at left
    garde "Ca faisait longtemps que nous n'avions plus de visiteur, la bibliotheque se trouve au bout de ce chemin, passez un agreable sejour"
    "C'est reparti pour une nouvelle iteration"
label entree_temporium:
    scene entree_ville with fade
    menu:
        "Que devrais-je faire maintenant"
        "Parler au soldat":
            $ parler_garde=True
            $ parler_garde_global=True
            show garde at left
            m "Comment ca se fait que vous ayez une pelle en main ?"
            garde "Ma lance c'est brisé et je n'ai pas le temps de passer chez le forgeron pour me faire forger une nouvelle lance"
            m "Tu veux que j'y aille pour toi ?"
            garde "Tu ferais vraiment ca pour une personne que tu viens de rencontrer ?"
            m "Bien sur, ca me fait plaisir"
            $ heure += 0.1
            jump entree_temporium
        "Aller à l'auberge":
            $ heure += 0.4
            jump auberge
        "Aller au forgeron" if parler_garde_global and not lance :
            $ heure += 0.8 
            jump forgeron
        "Donner la lance au garde" if parler_garde and lance:
            show garde
            m "Voici votre nouvelle lance flabante neuve"
            show garde lance
            garde "Oh merci, je n'aurai plus l'air ridicule avec cette pelle, d'ailleurs tenez je n'en ai plus besoin"
            garde "On dirait pas mais c'est une pelle de tres bonne qualité, vous pouvez la vendre ou la garder. Elle est à vous maintenant"
            $ pelle = True
            if pelle and filet and paille:
                jump pose_piege
            else :
                jump entree_temporium
        "Avancer vers la bibliotheque":
            $ heure += 0.2
            jump chemin
        "Passer la journée":
            jump debut_boucle
label chemin:
    scene ville_et_vendeuse with fade
    if heure <= 8.25:
        show fermier
        menu:
            "Il semblerait que je sois arrivé juste avant que le jeune homme se fasse bousculer"
            "L'aider":
                show fermier at tremble,center
                fermier "Blep"
                m "Attention !"
                "Il est trop tard pour le rattraper avant qu'il tombe mais je peux encore sauver ses pommes"
                if quete_pomme:
                    "Heureusement je rappelle encore de comment faire pour sauver ses pommes"

                else:
                    label quete_pommes:
                        j "Vite ! Vas y, Je pense savoir à l'avance où elles vont tomber"
                        m "Compris !"
                        python:
                            nom_quete = create_html(5,id,j,"Tu es pret ?")
                            if nom_quete is None:
                                renpy.jump("quete_pommes")
                            reussi = False
                            reussi,gold_gagne = verif_quete(id,3)

                        if reussi != True:
                            jump quete_pommes
                        python:
                            remove_html(id)
                            quete_pomme =True
                        call screen ecran_victoire(nom_quete,gold_gagne,3)
                fermier "Merci d'avoir rattrapé ma marchandise"
                fermier "Vous voyez je suis un paysan qui etait venu vendre ma marchandise au marché et si il etait arrivé quelque chose à mes pommes j'aurai été forcé de vendre ma ferme"
                fermier "C'est pour ca que je voudrai vous remercier, suivez moi je vais vous amener dans ma ferme pour vous donner votre recompense"
                $ heure += 0.5
                scene ferme with fade
                show fermier at right
                fermier "Voici ma recolte de l'année, prenez ce qui vous fait plaisir"
                menu :
                    "Prendre des pommes":
                        "Je ne sais pas ce que j'en ferai mais on sait jamais"
                    "Prendre du foin":
                        $ paille = True
                        "Voila qui pourrai m'etre utile"
                    "Prendre des pommes de terre":
                        "Je ne sais pas ce que j'en ferai mais on sait jamais"
                fermier "Encore merci de m'avoir sauver moi et ma ferme, passez une bonne journée"
                $ heure += 0.5
                jump chemin
            "L'ignorer":
                show fermier at tremble,center
                fermier "Blep"
                "Comme d'habitude je vois un jeune homme de l'autre coté de la route étalé sur le sol couvert de boue"
                fermier "Vous pourriez quand meme faire attention"
                "Au moment où il dit ca une charette passant à vive allure écrasa ses pommes"
                fermier "Oh non mes pommes"
    menu:
        "Que devrais-je faire maintenant"
        "Aller à l'auberge":
            $ heure += 0.25
            jump auberge
        "Aller forgeron" if parler_garde_global and not lance:
            $ heure += 0.5
            jump forgeron
        "Aller a l'entree de la ville":
            $ heure += 0.2
            jump entree_temporium
        "Parler a la vendeuse":
            label magasin:
                show vendeuse at right
                menu:
                    "J'ai [argent_actuel] piece d'argent"
                    "Acheter un filet - 200 piece d'argent":
                        if argent_actuel >=200:
                            $ argent_actuel -= 200
                            $ filet = True
                            vendeuse "Merci pour votre achat, j'espere vous revoir bientot"
                            "Voila qui pourrait m'etre utile"
                        else:
                            "Je n'ai pas assez d'argent, je devrai passer à l'auberge pour me faire plus d'argent"
                        jump magasin
                    "Acheter un parfum - 250 piece d'argent":
                        if argent_actuel >=250:
                            $ argent_actuel -= 250
                            vendeuse "Merci pour votre achat, j'espere vous revoir bientot"
                            "Je ne sais pas ce que j'en ferai mais on sait jamais"
                        else:
                            "Je n'ai pas assez d'argent, je devrai passer à l'auberge pour me faire plus d'argent"
                        jump magasin
                    "Acheter de l'huile - 100 piece d'argent":
                        if argent_actuel >=100:
                            $ argent_actuel -= 100
                            vendeuse "Merci pour votre achat, j'espere vous revoir bientot"
                            "Je ne sais pas ce que j'en ferai mais on sait jamais"
                        else:
                            "Je n'ai pas assez d'argent, je devrai passer à l'auberge pour me faire plus d'argent"
                        jump magasin
                    "Acheter du savon - 150 piece d'argent":
                        if argent_actuel >=150:
                            $ argent_actuel -= 150
                            vendeuse "Merci pour votre achat, j'espere vous revoir bientot"
                            "Je ne sais pas ce que j'en ferai mais on sait jamais"
                        else:
                            "Je n'ai pas assez d'argent, je devrai passer à l'auberge pour me faire plus d'argent"
                        jump magasin
                    "Partir":
                        vendeuse "Passez une bonne journée !"
                        jump chemin
        "Passer la journée":
            jump debut_boucle


label auberge:
    play music "Tavern_song.mp3" if_changed
    scene auberge
    show female_tavernier
    $ renpy.save_persistent()
    A "Bienvenue dans mon auberge, comment puis-je vous aider ?"
    if quete_auberge_global and not quete_auberge:
        "Refaisons rapidement les quetes que j'ai deja fait dans les iterations precedentes"
        scene auberge with fade
        show female_tavernier
        A "Vous avez gagné un total de [persistent.argent] piece d'argent"
        $ argent_actuel = persistent.argent
        "Voila qui est fait"
        $ quete_auberge = True
    menu: 
        "Voir les quetes disponibles":
            $ quests = load_quests(3)
            call screen quest_menu(3,quests,"dialogue_aubergiste_Temporium","auberge")
        "Repartir":
            $ heure += 0.25
            jump chemin

label dialogue_aubergiste_Temporium(quest_id,nom_quete, url):
    A "Bon courage pour la quête!"
    menu:
        "Commencer la quête":
            A "Parfait, voici les détails..."
            $ webbrowser.open(url)  # Redirige vers la page web si validé
            call quete_aubergiste_temporium(quest_id,nom_quete, url) from _call_quete_aubergiste_temporium
        "Annuler":
            A "C'est dommage, peut-être une autre fois."
            python:
                remove_html(id)
            jump auberge
label quete_aubergiste_temporium(quest_id,nom_quete, url):
    A "Alors, tu avances bien dans ta quete ?"
    menu:
        "Valider la quête":

            python:
                
                reussi = False
                reussi,gold_gagne = verif_quete(id,3)
                argent_actuel +=int(gold_gagne)
            if reussi != True:
                call quete_aubergiste_temporium(quest_id,nom_quete, url)
            python:
                remove_html(id)
                persistent.Quete_faite.append((quest_id, nom_quete))
            call screen ecran_victoire(nom_quete,gold_gagne,3)

            jump auberge
        "Abandonner":
            A "C'est dommage, peut-être une autre fois."
            python:
                remove_html(id)
            jump auberge

label forgeron:
    scene forge with fade
    show forgeron 
    forgeron "Tu veux quoi gamin ?"
    
    m "Je viens pour forger une nouvelle lance"

    forgeron "Qu'est-ce qu'une crevette comme toi ferai d'une lance ?"

    m "Ce n'est pas pour moi mais c'est pour le garde à l'entree du village qui a cassé la sienne"

    forgeron "Très bien, je trouvais aussi étrange qu'un garde se ballade avec une pelle au lieu d'une lance"

    if heure > 10:
        forgeron "Par contre faudra repasser demain, une lance ça se forge dans la fraicheur d'un bon matin"
        
        forgeron "Tu es arrivé trop tard et la journée a eu le temps de se rechauffer et tout ca n'est pas bon pour le metal"

        forgeron "Si tu etais arrivé avant 10 heure, je te l'aurai fait sans probleme"

        forgeron "Aller maintenant part et laisse moi me reconcentrer sur mon travail"

        "Mince je suis arrivé trop tard, j'aurai peut etre plus de chance lors de la prochaine iteration"

        $ heure += 0.5
        jump chemin 
    else:
        forgeron "Je veux bien m'occuper de ta commande donc repasse demain pour recuperer la lance finie"

        m "Malheureusement ca ne peut pas attendre demain, pouvez vous la terminer aujourd'hui ?"

        forgeron "Le probleme c'est que mon idiot d'assistant est tombé malade et sans lui le forgeage d'une nouvelle arme prend beaucoup plus de temps"

        m "Peut-etre pourrais-je remplacer votre assistant le temps de forger ma lance et echange vous finirez ma commande aujourd'hui"

        forgeron "Marché conclu"
        if not quete_forgeron:
            label quete_forge:
                python:
                    nom_quete = create_html(6,id,forgeron,"Alors commençons")
                    if nom_quete is None:
                        renpy.jump("quete_forge")
                    reussi = False
                    reussi,gold_gagne = verif_quete(id,3)

                if reussi != True:
                    jump quete_forge
                python:
                    remove_html(id)

                    quete_forge =True
                    heure += 5.5
                call screen ecran_victoire(nom_quete,gold_gagne,3)
        else:
            "Faisons ça rapidement vu que je me rappelle de comment faire"
        
        forgeron "Mine de rien, tu es doué et tu m'as été d'une grande aide. Tu es sur de ne pas vouloir devenir mon assistant à temps plein"
        
        forgeron "Enfin bref, une promesse est une promesse voici ta lance"
        $ lance=True
        jump chemin

label pose_piege:

    "C'est bon j'ai tous le materiel pour tendre un piege à l'autre pyromane"
    
    scene black with fade
    show Navi at right
    #play sound "pelle.mp3"

    m "Ok c'est bon je pense que le piege est en place"

    j "Vite cachons nous avant qu'il n'arrive"
    hide Navi with moveoutright
    #play sound "buisson.mp3"
    scene bibli_soir with fade

    j "Normalement il ne va pas tarder"

    with hpunch
    mechant1 "AAAAAH"

    m "C'est bon on l'a eu, approchons nous"
    show Navi at right with moveinright
    show mechant1 at left:
        ypos 1.1
        xzoom -1.0
    mechant1 "Qui ose m'attraper de la sorte"

    m "Qui es tu et pourquoi voulais tu mettre feu à la bibliotheque-monde"

    mechant1 "Je n'ai rien à dire à un sale humain"

    m "Je ne pense pas que sois en position de faire des caprices. Est-ce que je dois te rappeller la situation dans laquelle tu es"

    m "Reponds maintenant avant que je ne decide de faire une interrogation plus forcée"

    mechant1 "Tres bien je me rends, pas besoin d'aller aussi loin"

    m "Parle maintenant"

    mechant1 "Je suis un soldat sous les ordres du Serpent du Temps et j'etais venu pour bruler la bibliotheque-monde car elle contient des ecrits blasphématoire contre mon maitre"

    m "Des écrits blasphématoire ?"

    j "Je pense qu'il parle des livres qui parlent des faiblesses de Ouroboros"

    m "Je vois"

    m "Deuxieme question, pourquoi tu nous as enfermé dans une boucle et comment peut-on en sortir la ?"

    with hpunch
    mechant1 "QUOI ?"
    
    mechant1 "On est coincé dans une boucle temporelle ?"

    mechant1 "Ca ne peut signifier qu'une seule chose, l'autre vieillard nous a trahi"

    show mechant2 at myfade(1.0), center

    mechant2 "Alors comme ca on parle de moi dans mon dos ?"

    mechant1 "Explique toi, Rhotszix tu as osé trahir le maitre ?"
    
    $ mechant2_name = "Rhotszix"

    mechant2 "Je n'ai rien à dire à une vermine comme toi, hors de ma vue"

    show mechant1 at mymoveout(0.2)
    "Le pyromane est alors ejecté à une vitesse incroyable en direction d'un mur adjacent"
    play sound "wall-smash.mp3"
    "Il s'évanouit instantanement"
    jump endgame
