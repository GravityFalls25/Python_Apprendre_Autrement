
transform middleright:
    xalign 0.7
    ypos 0.06
    
define flash = Fade(.25, 0.0, .75, color="#fff") 

screen quest_menu(id_tavern,quests,label):
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
                                        textbutton quest[1] action Function(handle_quest_and_redirect, quest, site,None,"",id_tavern,label)

screen ecran_victoire(nom_quete,or_gagne,score_total):
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
            
            text "Or gagné: [or_gagne]":
                style "details_or"
            
            text "Score Total: [score_total]":
                style "details_score"
            
            textbutton "Retour au jeu" action Return() style "bouton_retour"



screen Map():
    add "carte_fin.png"
    imagebutton:
        xpos 1249
        ypos 649
        hover "village1_hover.png"
        idle "village1_idle.png"
        action Jump("place_village")
    imagebutton:
        xpos 827
        ypos 653
        hover "dedale_hover.png"
        idle "dedale_idle.png"
        action Jump("place_dedale")
    imagebutton:
        xpos 745
        ypos 473
        hover "temporium_hover.png"
        idle "temporium_idle.png"
        action Jump("place_temporium")


screen debloquer():
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20
        background "#ffd700"
        vbox:
            textbutton "Next" action Show("debloquer_2"),Hide("debloquer")

screen debloquer_2():
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20
        background "#ffd700"
        vbox:
            textbutton "Retour au jeu" action Hide("debloquer_2"),Return()