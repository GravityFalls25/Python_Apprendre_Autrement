
transform middleright:
    xalign 0.7
    ypos 0.06
    
define flash = Fade(.25, 0.0, .75, color="#fff") 

screen quest_menu(id_tavern,quests,label,label_retour):
        frame:
                
            background Solid("#000000ae")
            
            vbox:
                
                spacing 5
                textbutton "Retour" action Jump(label_retour) style "retour_taverne"
                viewport:
                    draggable True
                    scrollbars "vertical"
                    mousewheel True
                    
                    grid 3 calculate_rows(quests, 3):  # Dynamiquement calculé
                        spacing 10
                        python:
                            #liste_quete = sorted(list(quests), key=lambda x: float(x[1]))
                            if quests is not None:
                                liste_quete = sorted(list(quests))
                            else:
                                liste_quete= []
                        for quest in liste_quete:
                            frame:
                                style "quest_frame"
                                vbox:
                                        text quest[0]
                                        text "Difficulté: {}".format(quest[2])
                                        textbutton quest[1] action Function(handle_quest_and_redirect, quest, site,None,"",id_tavern,label)

screen ecran_victoire(nom_quete,or_gagne,chap=0):
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20
        background "#444444"  # Une couleur de fond gris foncé

        vbox:
            align (0.5, 0.5)
            spacing 10

            text "Victoire !":
                style "titre_victoire"
            
            text "Quête: [nom_quete]":
                style "details_quete"
           
            if chap == 1: 
                text "Or gagné: [or_gagne]":
                    style "details_or"
                text "Or total: [persistent.gold]":
                    style "details_or"
            elif chap == 2: 
                text "Point de valeur gagné: [or_gagne]":
                    style "details_or"
                text "Point de valeur total: [persistent.point_de_valeur]":
                    style "details_or"
            elif chap == 3: 
                text "Argent gagné: [or_gagne]":
                    style "details_or"
                text "Argent total: [persistent.argent]":
                    style "details_or"
            
            text "Score Total: [persistent.score]":
                style "details_score"
            
            textbutton "Retour au jeu" action Return() style "bouton_retour"



screen Map(ch):
    add "carte_fin.png"
    imagebutton:
        xpos 1249
        ypos 649
        hover "village1_hover.png"
        idle "village1_idle.png"
        action Jump("place_village")
    if ch >=2:
        imagebutton :
            xpos 827
            ypos 653
            hover "dedale_hover.png"
            idle "dedale_idle.png"
            action Jump("place_dedale")
    if ch >=3:
        imagebutton :
            xpos 744
            ypos 473
            hover "temporium_hover.png"
            idle "temporium_idle.png"
            action Jump("auberge")

define get_fct=[
    ["Vous avez compris comment utiliser le print()\n","Le print sert à écrire ce qui est marqué dans ses parentheses que ce soit une phrase, un nombre ou la valeur d'une variable","nbr=4\nprint(\"nbr\")\nprint(nbr)\nprint(5)","nbr\n4\n5"],
    ["Vous avez appris à utiliser le input()\n","La fonction input() permet de recuperer une ligne de la liste des inputs. Vous pouvez par apres stocker cette ligne dans une variable mais attention par defaut la fonction input() va recuperer la ligne sous la forme d'un string c'est-à-dire qu'il va considerer que c'est un suite de lettres et il sera donc pas possible de faire des operations mathematiques dessus.\n\nPour transformer ce string en un autre type de variable plus pratique il faudra preciser à quel type de variable appartient l'input de cette facon:\n\n    int(input()) pour recuperer un entier\n    float(input()) pour recuperer un nombre à virgule\n    etc.","{color=#13ad0d}#Les inputs sont dans l'ordre \"hello world,5,5\"{/color}\nstr1=input()\nnbr1=int(input())\nnbr2=float(input())\n\nprint(str1)\nprint(nbr1)\nprint(nbr2)","hello world\n5\n5.0"],
    ["Vous avez appris à utiliser le if\n","Le if est une operation qui permet au programme de faire des decisions. Autrement dit le programme va lancer un certain code quand certaines conditions sont respectées.\n\nLa condition sera ecrite juste apres le if sur la meme ligne et se terminera par \":\"\nLe code qui sera executé quand la condition est respectée doit se trouver sur la ligne en-dessous du if et doit absolument etre decalé vers la droite en appuyant sur la touche \"tab\"\nLe fait de decaler une partie du code vers la droite s'appelle l'indentation et est un concept tres important en python si l'indentation n'est pas respecté alors le code risque ne pas donner les bonnes reponses ou de juste ne pas se lancer","a=3\nb=5\nif b>a: {color=#13ad0d}#La condition a respecter{/color}\n    {color=#13ad0d}#Le code a executer si la condition est respectée{/color}\n    print(\"b est plus grand que a\")","b est plus grand que a"],
    ["Vous avez debloqué le elif\n","Le elif s'utilise apres le code d'un if et est le moyen d'exprimer en python que \"Si la condition precedente n'est pas respectée alors essaye cette condition\"\n\nIl s'utilise de la meme facon que le if","a=5\nb=3\nif b>a: {color=#13ad0d}#La 1ere condition a respecter{/color}\n    print(\"b est plus grand que a\")\nelif a>b: {color=#13ad0d}#La 2eme condition a respecter{/color}\n    {color=#13ad0d}#Le code a executer si la 1ere condition n'est pas respectée mais la deuxieme condition oui{/color}\n    print(\"a est plus grand que b\")","a est plus grand que b"],
    ["Vous avez debloqué le else\n","Le else sert a executer un code quand aucune des conditons precedantes n'a été respecté\n\nIl s'utilise de la meme facon qu'un if ou un elif sauf qu'il ne faut pas specifier de condition","a=5\nb=5\nif b>a: {color=#13ad0d}#La 1ere condition a respecter{/color}\n    print(\"b est plus grand que a\")\nelif a>b: {color=#13ad0d}#La 2eme condition a respecter{/color}\n    print(\"a est plus grand que b\")\nelse:\n    {color=#13ad0d}#Le code a executer si aucune des conditions n'a été respecté{/color}\n    print(\"a et b sont egaux\")","a et b sont egaux"]
]
screen debloquer(id):
    frame:
        ypadding 20
        xalign 0.5
        yalign 0.5
        xpadding 20
        background None
        vbox:
            xalign 0.5
            yalign 0.5
            frame:
                xalign 0.5
                background "#d1b30a"
                vbox:
                    text "Felicitation !":
                        xalign 0.5
                        bold True
                        color "#000"
            frame:
                xalign 0.5
                xpadding 20
                ypadding 20
                background "#ffd700"
                vbox: 
                    text get_fct[id][0]:
                        color "#000"
                        line_leading 2
                    text get_fct[id][1]:
                        color "#000"
                        line_spacing 2
                    textbutton "Next" action Show("debloquer_2",id=id),Hide("debloquer"):
                        xalign 1.0

screen debloquer_2(id):
    frame:
        ypadding 20
        xalign 0.5
        yalign 0.5
        xpadding 20
        background None
        vbox:
            xalign 0.5
            yalign 0.5
            frame:
                xalign 0.5
                background "#d1b30a"
                vbox:
                    text "En pratique":
                        xalign 0.5
                        bold True
                        underline True
                        color "#000"
            frame:
                xalign 0.5
                yalign 0.5
                xpadding 20
                ypadding 20
                background "#ffd700"
                vbox:
                    text "Exemple de code":
                        color "#000"
                    frame:
                        background "#26282A"
                        text get_fct[id][2]
                    text "Output":
                        color "#000"
                    frame:
                        background "#26282A"
                        text get_fct[id][3]
                    hbox:
                        textbutton "Precedent" action Show("debloquer",id=id),Hide("debloquer_2")
                        textbutton "Retour au jeu" action Hide("debloquer_2"),Return()