import mock
import importlib
from io import StringIO
import sys

output = StringIO()
sys.stdout = output
with mock.patch('builtins.input', side_effect=['Pierre', 'Papier']):
    import user
    sys.stdout = sys.__stdout__
    if output.getvalue().strip() == "J2 gagne":
        print('Correct')
    else:
        print('non')

output = StringIO()
sys.stdout = output
with mock.patch('builtins.input', side_effect=['Papier', 'Pierre']):
    importlib.reload(user)
    sys.stdout = sys.__stdout__
    if output.getvalue().strip() == "J1 gagne":
        print('Correct')
    else:
        print('non')

output = StringIO()
sys.stdout = output
with mock.patch('builtins.input', side_effect=['Papier', 'Papier']):
    importlib.reload(user)
    sys.stdout = sys.__stdout__
    if output.getvalue().strip() == "Egalité":
        print('Correct')
    else:
        print('non')

