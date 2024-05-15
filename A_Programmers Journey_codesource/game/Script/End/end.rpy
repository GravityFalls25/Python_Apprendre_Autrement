label endgame(pause_length=4.0):

    $ quick_menu = False

    stop music fadeout 2.0

    scene black

    show end
    with dissolve_scene_full

    pause pause_length

    $ quick_menu = True

    return


label presentation:
    $ quete_auberge_global = True
    $ quete_auberge = True
    $ heure = 0
    $ name = "Bricoleur"
    $ Navi_name="Navi"
    $ argent_actuel=0
    $ persistent.chap = 4
    jump auberge