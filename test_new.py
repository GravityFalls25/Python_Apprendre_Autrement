import mock
import importlib
from io import StringIO
import sys

output = StringIO()
sys.stdout = output
with mock.patch('builtins.input', side_effect=['1', '2']):
    import user
    sys.stdout = sys.__stdout__
    print(output.getvalue().strip())
    if output.getvalue().strip() == "Je vais bien\nMerci":
        print('Correct')
    else:
        print('non')

