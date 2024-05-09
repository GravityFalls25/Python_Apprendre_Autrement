label Temporium:
    scene black with fade
    "Nous sommes enfin arrivé aux porte de Temporium apres un voyage qui m'a semblé interminable"

    scene ville_temporium with fade
    show garde

    garde "Halte la, declinez votre identité"

    j "Nous sommes Navi et [name], des voyageurs à la recherche de la bibliotheque-monde"

    garde "Tres bien, vous pouvez rentrer"

    "Nous passons l'entrée de la ville"
    play sound "call_of_the_witch.mp3"

    m "Tiens, tu as entendu ca ?"
    j "Entendu quoi ?"
    #boucle 1
    garde "Ca fesait longtemps que nous avions plus de visiteur, la bibliotheque se trouve au bout de ce chemin, passez un agreable sejour"

    scene chemin_ville with fade
    "{i}Nous avancons alors sur le chemin que nous a indiqué le garde{/i}"

    show fermier with vpunch
    fermier "Blep"
    "Je vois un jeune homme etalé sur le sol couvert de boue"
    fermier "Vous pourriez quand meme faire attention"
    "Au moment ou il dit ca une charette passant à vive allure ecrasa ses pommes"
    fermier "Oh non mes pommes"

    "En voila quelqu'un qui n'a pas de chance mais il n'a pas l'air d'etre blessé et ses pommes sont irrecuperables, il n'y a rien que je puisse faire"