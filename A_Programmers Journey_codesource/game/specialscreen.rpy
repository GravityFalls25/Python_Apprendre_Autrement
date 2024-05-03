
transform middleright:
    xalign 0.7
    ypos 0.06
    
define flash = Fade(.25, 0.0, .75, color="#fff") 

screen quest_menu(id_tavern,quests):
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
                                        textbutton quest[1] action Function(handle_quest_and_redirect, quest, site)
    
screen Map():
    add "Game_plan.png"
    imagebutton:
        xpos 335
        ypos 685
        hover "vill1_hover.png"
        idle "vill1_idle.png"
        action Jump("place_village")
