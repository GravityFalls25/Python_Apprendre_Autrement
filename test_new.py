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
with mock.patch('builtins.input', side_effect=['']):
    import user
    sys.stdout = sys.__stdout__
    if output.getvalue().strip() == "Je vais bien":
        print('Correct')
    else:
        print('non')

        ok = False
url = 'http://127.0.0.1:5000/update_mission_state'
myobj = {'player_id': id,'state': ok, 'gold':gold }
x = requests.post(url, json = myobj)
