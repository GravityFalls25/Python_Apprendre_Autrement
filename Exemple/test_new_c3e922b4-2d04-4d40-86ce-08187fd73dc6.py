import mock
import importlib
from io import StringIO
import requests
import sys
import multiprocessing
import time
import ast

first = True

class InputExceededError(Exception):
    pass


class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.found = {
            'if': False,
            'match' : False,
            'for': False,
            'while': False,
            'list': False,
            'set' : False,
            'with': False,

            
        }
    def visit_List(self, node):
        self.found['list'] = True
        self.generic_visit(node)

    def visit_Set(self, node):
        self.found['set'] = True
        self.generic_visit(node)

    def visit_With(self, node):
        self.found['with'] = True
        self.generic_visit(node)

    

def check_code_restrictions(code):
    tree = ast.parse(code)
    analyzer = CodeAnalyzer()
    analyzer.visit(tree)
    return analyzer.found

def check_len_code(code,max_lines = 1000):
    lines = [line for line in code.split('\n') if line.strip() and not line.strip().startswith('#')]
    line_count = len(lines)
    if line_count > max_lines:
        print(f"On ne peut pas executer ca, ton code est trop long ! Fais attention, le pont est fragile, tu n'as droit qu'a {max_lines} (sans compter les commentaires et les lignes vides)")
        return False
# Utilisation dans votre système de test
def validate_student_code(code):
    if not check_code_restrictions(code): 
        return False

    restrictions = check_code_restrictions(code)
    # Ici, vous pouvez déterminer si certaines constructions sont utilisées et prendre des mesures en conséquence
    if any(restrictions.values()):
        print("Votre code utilise des constructions non autorisees.")
        return False
    return True




def run_test(inputs, expected_output):
    output = StringIO()
    sys.stdout = output
    def side_effect(*args, **kwargs):
        if side_effect.counter < len(inputs):
            result = inputs[side_effect.counter]
            side_effect.counter += 1
            return result
        raise InputExceededError("Plus d'inputs demandes que fourni")
    side_effect.counter = 0

    with mock.patch('builtins.input', side_effect=side_effect):
        try:
            importlib.reload(user)  # Recharger le module utilisateur pour chaque test
        except InputExceededError as e:
            return str(e)
        except Exception as e:
            return "autre"
        finally:
            sys.stdout = sys.__stdout__

          # Recharger le module utilisateur pour chaque test
    actual_output = output.getvalue().strip()
    return actual_output == expected_output

def run_test_1(inputs, expected_output):
    output = StringIO()
    sys.stdout = output
    def side_effect(*args, **kwargs):
        if side_effect.counter < len(inputs):
            result = inputs[side_effect.counter]
            side_effect.counter += 1
            return result
        raise InputExceededError("Plus d'inputs demandes que fournis")
    side_effect.counter = 0

    with mock.patch('builtins.input', side_effect=side_effect):
        try:
            import user  # Recharger le module utilisateur pour chaque test
        except InputExceededError as e:
            return str(e)
        except Exception as e:
            return "autre"
        finally:
            sys.stdout = sys.__stdout__

          # Recharger le module utilisateur pour chaque test
    actual_output = output.getvalue().strip()
    return actual_output == expected_output

def run_in_process(queue, inputs, expected_output):
    global first
    if first == True:
        result = run_test_1(inputs, expected_output)
        first = False
    else:
        result = run_test(inputs, expected_output)
    queue.put(result)

def perform_test(inputs, expected_output, timeout):
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=run_in_process, args=(queue, inputs, expected_output))
    process.start()
    process.join(timeout)
    if process.is_alive():
        process.terminate()
        return "Timeout"
    else:
        return queue.get()

def main():
    gold = sys.argv[1]
    id = sys.argv[2]
    ok = True
    tests = [
        (['a', '6'], '0\n1\n2\n3\n4\n5'),
        (['b', '8'], '1\n4\n9\n16\n25\n36\n49\n64'),
        (['d', '9'], '10\n9\n8\n7\n6\n5\n4\n3\n2'),
        (['c', '5'], '2\n4\n6\n8\n10'),

    ]

    with open("user.py", "r") as file:
        user_code = file.read()

    # Vérifier les restrictions
    if not validate_student_code(user_code):
        
        return

    timeout = 2  # Temps limite en secondes pour chaque test

    for i in range(len(tests)):
        result = perform_test(tests[i][0], tests[i][1], timeout)
        if not result:
            print(f"Test case #{i+1} echoue")
            ok = False
            break
        elif result == "Timeout":
            print("Ton code est anormalement long, verifie-le")
            ok = False
            break
        elif result == "Plus d'inputs demandes que fournis":
            print(result)
            ok = False
            break
        elif result == "autre":
            print(result)
            ok = False
            break
        else:
            print(f"Test case #{i+1} reussi")
    if ok:
        print("Quete reussite, tu peux retourner sur le jeu")
    url = 'http://127.0.0.1:5000/update_mission_state'
    myobj = {'player_id': id, 'state': ok, 'gold': gold}
    x = requests.post(url, json=myobj)

if __name__ == '__main__':
    main()