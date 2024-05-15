#Definition de variable
default Navi_name ="????"
default name="Bricoleur"
default mechant2_name="????"

#Variable qui reste lorsque l'on recharge le jeu
if not persistent.score:
        default persistent.score = 0
if not persistent.Quete_faite:
        default persistent.Quete_faite = list()
if not persistent.gold:
        default persistent.gold = 0
if not persistent.point_de_valeur:
        default persistent.point_de_valeur = 0
if not persistent.argent:
        default persistent.argent = 0
if not persistent.point_intelligence:
        default persistent.point_intelligence = 0
if not persistent.chap:
        default persistent.chap = 0