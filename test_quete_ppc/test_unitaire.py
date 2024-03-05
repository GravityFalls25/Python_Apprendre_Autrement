#import mock
#import importlib
#with mock.patch('builtins.input',side_effect=["Papier","Pierre"]):
#    import user
#with mock.patch('builtins.input',side_effect=["Pierre","Papier"]):
#    importlib.reload(user)
import unittest
import sys
from io import StringIO
import importlib
import unittest.mock

class TestPierrePapierCiseaux(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_egalite(self):
        with unittest.mock.patch('builtins.input', side_effect=["Papier", "Papier"]):
            import user
            self.assertEqual(self.output.getvalue().strip(), "Egalité")

    def test_j1_gagne(self):
        with unittest.mock.patch('builtins.input', side_effect=["Pierre", "Ciseaux"]):
            import user
            importlib.reload(user)
            
            self.assertEqual(self.output.getvalue().strip(), "J1 gagne")

    def test_j2_gagne(self):
        with unittest.mock.patch('builtins.input', side_effect=["Papier", "Ciseaux"]):
            import user
            importlib.reload(user)
            self.assertEqual(self.output.getvalue().strip(), "J2 gagne")

if __name__ == '__main__':
    unittest.main()
