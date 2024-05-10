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
with mock.patch('builtins.input', side_effect=['2', '1', '3']):
    import user
    sys.stdout = sys.__stdout__
    if output.getvalue().strip() == "6":
        print('Correct')
    else:
        print('non')

        ok = False
output = StringIO()
sys.stdout = output
with mock.patch('builtins.input', side_effect=['4', '2', '1']):
    importlib.reload(user)
    sys.stdout = sys.__stdout__
    if output.getvalue().strip() == "7":
        print('Correct')
    else:
        print('non')

        ok = False
output = StringIO()
sys.stdout = output
with mock.patch('builtins.input', side_effect=['8', '5', '1']):
    importlib.reload(user)
    sys.stdout = sys.__stdout__
    if output.getvalue().strip() == "14":
        print('Correct')
    else:
        print('non')

        ok = False
output = StringIO()
sys.stdout = output
with mock.patch('builtins.input', side_effect=['5', '5', '1']):
    importlib.reload(user)
    sys.stdout = sys.__stdout__
    if output.getvalue().strip() == "11":
        print('Correct')
    else:
        print('non')

        ok = False
url = 'http://127.0.0.1:5000/update_mission_state'
myobj = {'player_id': id,'state': ok, 'gold':gold }
x = requests.post(url, json = myobj)
