import mock
from io import StringIO
import sys
import multiprocessing

# Exception personnalisée pour gérer les inputs excédentaires
class InputExceededError(Exception):
    pass

def run_test(inputs):
    output = StringIO()
    sys.stdout = output
    def side_effect(*args, **kwargs):
        if side_effect.counter < len(inputs):
            result = inputs[side_effect.counter]
            side_effect.counter += 1
            return result
        raise InputExceededError("Plus d'inputs demandes que fournis")
    side_effect.counter = 0

    #Systeme de buffer pour les inputs
    with mock.patch('builtins.input', side_effect=side_effect):
        try:
            import user  # Recharger le module utilisateur pour chaque test
        except InputExceededError as e:
            return str(e)
        except Exception as e:
            return f"Erreur non gérée : {str(e)}"
        finally:
            sys.stdout = sys.__stdout__
    actual_output = output.getvalue().strip()
    return actual_output

def run_in_process(queue, inputs):
    result = run_test(inputs)
    queue.put(result)

def perform_test(inputs, timeout):
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=run_in_process, args=(queue, inputs))
    process.start()
    #Pour stopper si le programme dure trop longtemps, (risque de boucle infinie)
    process.join(timeout)
    if process.is_alive():
        process.terminate()
        return "Il y a surement une boucle infinie, verfie ton code"
    else:
        return queue.get()

def main():
    if len(sys.argv) == 1:
        inputs = ""
    else:
        inputs = sys.argv[1]
        if inputs:
            inputs = inputs.split(',')
    timeout = 2  # Temps limite en secondes pour chaque test
    result = perform_test(inputs, timeout)
    print(result)
    
if __name__ == '__main__':
    main()
