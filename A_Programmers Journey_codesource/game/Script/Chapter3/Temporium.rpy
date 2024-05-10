label Temporium:
    scene black with fade
    "Nous sommes enfin arrivé aux portes de Temporium apres un voyage qui m'a semblé interminable"

    scene ville_temporium with fade
    show garde

    garde "Halte la, declinez votre identité"

    j "Nous sommes des voyageurs à la recherche de la bibliotheque-monde, Je m'appelle Navi et suis accompagné de [name]"

    garde "Tres bien, vous pouvez rentrer"

    "Nous passons l'entrée de la ville"
    #play sound "call_of_the_witch.mp3"

    m "Tiens, tu as entendu ca ?"
    j "Entendu quoi ?"
    #boucle 1
    garde "Ca faisait longtemps que nous n'avions plus de visiteur, la bibliotheque se trouve au bout de ce chemin, passez un agreable sejour"

    scene chemin_ville with fade
    "{i}Nous avancons alors sur le chemin indiqué par le garde{/i}"

    show fermier with vpunch
    fermier "Blep"
    "Je vois un jeune homme étalé sur le sol couvert de boue"
    fermier "Vous pourriez quand meme faire attention"
    "Au moment où il dit ca une charette passant à vive allure écrasa ses pommes"
    fermier "Oh non mes pommes"

    "En voila un qui n'a pas de chance. Heureusement, il n'a pas l'air d'etre blessé mais ses pommes sont irrecuperables, il n'y a rien que je puisse faire"

    "Continuons d'avancer"

    show vendeur
    vendeur "Approchez, approchez, venez voir mes produits venant des quatres coins du monde"

    m "Oh ce stand à l'air interressant, il vend plein de produits que je n'ai jamais vu"

    j "On ira voir plus tard, pour l'instant concentrons-nous sur la bibliotheque"

    scene black with fade
    "Nos arrivames enfin en face de l'immense bibliotheque-monde"

    scene bibliotheque with fade
    m "Wow, cette bibliotheque est vraiment immense !"
    m "Mais c'est quoi ce papier sur la porte ?"

    show papier

    m "Il semblerait qu'elle soit fermée pour aujourd'hui"

    j "Quel dommage !"
    
    j "C'est pas tres grave louons une chambre d'auberge en attendant. De plus, ca nous permettra de nous reposer de notre long periple"

    scene black with fade

    "Nous nous dirigeames vers l'auberge la plus proche et louons directement deux chambres pour passer la nuit"

    m "Je suis vraiment extenué, j'ai l'impression que je pourrais m'écrouler à tout moment"

    m "D'un autre coté, ça fait longtemps que je me suis pas autant amusé"
    # ça me change quand meme beaucoup de d'habitude
    m "Je me demande combien de temps s'est passé dans mon monde originel"

    "C'est sur cette pensée que je fini par m'assoupir"

    scene black with fade
    play sound "crash.mp3"
    show Navi inquiet with moveinright
    j "Vite reveille-toi un truc horrible est en train de se passer !"

    m "Hein quoi qu'est-ce qui se passe ?"

    j "La bibliotheque-monde est en feu !"

    scene bibliotheque_feu with hpunch
    show Navi inquiet at right

    j "Allons vite voir de plus pres"

    "Nous nous precipitames sans meme prendre le temps de nous preparer mais le temps d'arriver à la bibliotheque, elle etait deja reduite en cendre"

    "On essaye quand meme de fouiller dans les debris pour voir si un livre a survecu mais rien a y faire, tout est irrecuperable"
    # Tu crois qu'il reste encore quelques livres
    # Non, il ne reste plus rien, tout est irrecuperable
    j "Oh non comment vas-t'on faire maintenant. C'etait le seul moyen de savoir où se trouvait Ouroboros et comment le vaincre"

    m "Retournons nous coucher, on trouvera une solution demain, à tete reposée"

    scene black with fade
    "On retourna dans nos chambres respectives mais comment trouver le sommeil apres ce qui vient de se passer ?"

    #2eme boucle
    play sound "call of the witch.mp3"
    scene ville_temporium

    m "Hein quoi où suis-je, comment je suis arrivé la ?"

    garde "Ca faisait longtemps que nous avions plus de visiteur, la bibliotheque se trouve au bout de ce chemin, passez un agreable sejour"

    "J'ai comme une impression de deja-vu"

    scene chemin_ville with fade
    "Nous avancons tout de meme sur le chemin indiqué par le garde"

    show Navi with fade
    j "Hey, tu sais comment on est retourné à l'entrée de la ville ?"

    m "Non je n'ai aucune idée et en plus, regarde au bout de ce chemin, ce n'est pas la bibliotheque que l'on a vu bruler hier soir ?"

    j "Peut-etre qu'on en saura plus si on se rapproche de la bibliotheque"
    # "ça ne peux pas être possible, allons voir de plus pres"
    show fermier with vpunch
    fermier "Blep"
    "C'est le meme jeune homme qu'hier qui est encore etalé au sol, couvert de boue"
    fermier "Vous pourriez quand meme faire attention"
    "Et encore une fois, une charette ecrasa ses pommes"
    fermier "Oh non mes pommes"

    "On continue d'avancer"

    show vendeur
    vendeur "Approchez, approchez, venez voir mes produits venant des quatres coins du monde"

    "Le vendeur est lui aussi encore la"

    scene black with fade
    "On arriva enfin en face de l'immense bibliotheque-monde"

    scene bibliotheque with fade
    m "Le papier est toujours la"
    show paper

    m "Voila qui confirme mes soupcons, le jour n'a pas changé, d'une facon ou d'une autre nous avons remonté le temps"

    m "Tu sais ce qui a pu causer ca Navi ?"

    j "Je pense que c'est du à la capacité d'une des fonctions divines"

    j "Je suspecte l'utilisation de boucles"

    m "Et quels sont les effets d'une boucle ?"

    j "Si l'outil utilisé est le for alors on risque de repeter la boucle un nombre bien precis de fois mais dans le cas ou c'est un while..."

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

    scene bibliotheque
    m "Ca nous aura prit tout le reste de la journée mais on a enfin reussi à copier les effets des boucles"

    call screen debloquer

    j "Malheuresement quand bien meme on sait creer des boucles, on ne sait toujours pas comment en sortir d'une"

    m "Au moins on sera pret pour la prochaine fois que la boucle recommencera"

    m "Mais avant que cette itération ne se finisse, il faut decouvrir pourquoi la bibliotheque a prit feu"

    play sound "start_fire.mp3"

    j "Il semblerait que ca a deja commencé"

    m "Vite fait le tour du batiment par la gauche et essaie de voir si il y a quelque chose de suspect, moi je ferai le tour par la droite"

    "{i}Au moment où j'arrive derriere le batiment, une figure encapuchonnée sort à toute vitesse de la bibliotheque {/i}"

    m "Hey vous, arretez-vous !"

    "En me voyant arriver le suspect accelere, j'essaye de le poursuivre mais il finit par me semer"

    m "Mince, il m'a filé entre les doigts mais au moins je sais maintenant que ce n'etait pas un accident mais bien un acte criminel"

    m "De plus, si c'est de sa faute qu'on soit coincé dans une boucle alors il possede surement aussi le moyen pour en sortir"

    m "Et pour finir, je sais par où il est passé donc je pourrais lui tendre un piege lors de la prochaine iteration"

