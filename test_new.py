import mock
import importlib
from io import StringIO
import sys
import requests

gold = int(sys.argv[1])
id = int(sys.argv[2])
output = StringIO()
sys.stdout = output
ok = True
with mock.patch('builtins.input', side_effect=['1', '2']):
    import user
    sys.stdout = sys.__stdout__
    print(output.getvalue().strip())
    if output.getvalue().strip() == "Je vais bien\nMerci":
        print('Correct')
        

        
    else:
        print('non')
        ok = False
url = 'http://127.0.0.1:5000/update_mission_state'
myobj = {'player_id': '1','state': ok, 'gold':gold }


x = requests.post(url, json = myobj)
print(x.text)

