import mock
import importlib
from io import StringIO
import requests
import sys

gold = sys.argv[1]
id = sys.argv[2]
ok = True
output = StringIO()
sys.stdout = output
with mock.patch('builtins.input', side_effect=['1', '5', '4', '2', '2', '3', '2', '1', '6', '4', '5', '2', '5', '2', '3', '1', '4', '6', '3', '1']):
    import user
    sys.stdout = sys.__stdout__
    if output.getvalue().strip() == "Il faut apporter 4000mL d'eau pour la maison 1\nIl faut apporter 1200mL d'eau pour la maison 2\nIl faut apporter 24000mL d'eau pour la maison 3\nIl faut apporter 3000mL d'eau pour la maison 4\nIl faut apporter 7200mL d'eau pour la maison 5\nIl faut apporter 39400mL d'eau au total":
        print('Correct')
    else:
        print('non')

        ok = False
output = StringIO()
sys.stdout = output
with mock.patch('builtins.input', side_effect=['2', '4', '6', '2', '1', '3', '2', '1', '5', '4', '5', '2', '6', '2', '3', '1', '4', '6', '2', '1']):
    importlib.reload(user)
    sys.stdout = sys.__stdout__
    if output.getvalue().strip() == "Il faut apporter 9600mL d'eau pour la maison 1\nIl faut apporter 600mL d'eau pour la maison 2\nIl faut apporter 20000mL d'eau pour la maison 3\nIl faut apporter 3600mL d'eau pour la maison 4\nIl faut apporter 4800mL d'eau pour la maison 5\nIl faut apporter 38600mL d'eau au total":
        print('Correct')
    else:
        print('non')

        ok = False
output = StringIO()
sys.stdout = output
with mock.patch('builtins.input', side_effect=['1', '1', '1', '2', '2', '3', '2', '1', '1', '4', '5', '2', '7', '2', '3', '1', '5', '6', '3', '2']):
    importlib.reload(user)
    sys.stdout = sys.__stdout__
    if output.getvalue().strip() == "Il faut apporter 200mL d'eau pour la maison 1\nIl faut apporter 1200mL d'eau pour la maison 2\nIl faut apporter 4000mL d'eau pour la maison 3\nIl faut apporter 4200mL d'eau pour la maison 4\nIl faut apporter 18000mL d'eau pour la maison 5\nIl faut apporter 27600mL d'eau au total":
        print('Correct')
    else:
        print('non')

        ok = False
url = 'http://127.0.0.1:5000/update_mission_state'
myobj = {'player_id': id,'state': ok, 'gold':gold }
x = requests.post(url, json = myobj)
