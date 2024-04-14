# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/', methods=["POST"])
# def traiter_requete():
#     data = request.json  # Récupère les données JSON de la requête
#     valeur = data.get('valeur')  # Accède à la valeur 'valeur' dans les données JSON
#     print(valeur)
#     if valeur == '1':
#         # Exécutez votre commande PHP ici
        
#         # subprocess.run(['php', 'chemin_vers_votre_script.php'])
#         return jsonify({"message": "Commande PHP exécutée avec succès"})
#     else:
#         return jsonify({"message": "Valeur incorrecte"})

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
def html(Quest = 0,Id = 0):
    # -*- coding: utf-8 -*-
    """
    Created on Wed Apr 10 09:50:41 2024

    @author: thiba
    """

    quete = Quest
    id = Id
    with open("quest.txt",'r',encoding='utf-8') as fin:
        texte = fin.read().split("\n")
        texte2 = list()
        for ligne in texte:
            if ligne == "nan":
                ligne = ""
            texte2.append( ligne.split(r"\n"))
        df = dict()
        n_ligne, n_colonne = list(map(int,texte2[0][0].split()))
        
        for i in range(n_colonne):
            df[texte2[i+1][0]] = texte2[n_colonne + 1 + i*n_ligne + quete]
            
    n1 = "\\n"         
    for j in range(n_colonne):
        # Créer une liste de tuples pour stocker les résultats des tests
        tests = []
        
        # Parcourir les colonnes input_test_1 à input_test_3 et output_test_1 à output_test_3
        var = df['n_test']
        for i in range(1, int(df['n_test'][0])+1):
            # Récupérer les valeurs des entrées et des sorties des tests
            var = df[f'input_test_{i}']
            side_effects = df[f'input_test_{i}']  # Convertir en liste et supprimer les valeurs NaN
            expected_output = ""
            for idx, line_output in enumerate(df[f'output_test_{i}']):
                # Vérifier si c'est le dernier élément
                if idx == len(df[f'output_test_{i}'])- 1:
                    # Pour le dernier élément, ne pas ajouter le n1
                    expected_output += line_output
                else:
                    # Pour les autres éléments, ajouter le n1
                    expected_output += line_output + n1
            # for line_output in df[f'output_test_{i}']:
                
            #     expected_output = expected_output + line_output + n1 # Prendre la première valeur non-NaN
            #side_effects_str = ', '.join([f'{item}' for item in side_effects])
            # Ajouter le tuple (entrées, sortie attendue) à la liste des tests
            
            expected_output = '"'+expected_output +'"'
            tests.append((side_effects, expected_output))
        
        # Mettre à jour la colonne Tests avec la liste des résultats des tests
        df['Tests'] = tests
        
            
    #Ecriture code test
    with open("test_new.py", 'w') as fout:
        fout.write("import mock\n")
        fout.write("import importlib\n")
        fout.write("from io import StringIO\n")
        fout.write("import requests\n")
        fout.write("import sys\n\n")
        fout.write("gold = sys.argv[1]\n")
        fout.write("id = sys.argv[2]\n")
        fout.write("ok = True\n")
        prime = True
        for side_effects, expected_output in df['Tests']: #Le 0 correspondra a la quete a faire
            
            fout.write("output = StringIO()\n")
            fout.write("sys.stdout = output\n")
            fout.write(f"with mock.patch('builtins.input', side_effect={side_effects}):\n")
            if prime:
                fout.write("    import user\n")
                prime = False
            else:
                fout.write("    importlib.reload(user)\n")
            fout.write("    sys.stdout = sys.__stdout__\n")
            fout.write(f'    if output.getvalue().strip() == {expected_output}:\n')
            fout.write("        print('Correct')\n")
            fout.write("    else:\n")
            fout.write("        print('non')\n\n")
            fout.write("        ok = False\n")
        fout.write("url = 'http://127.0.0.1:5000/update_mission_state'\n")
        fout.write("myobj = {'player_id': id,'state': ok, 'gold':gold }\n")
        fout.write("x = requests.post(url, json = myobj)\n")
    #Ecriture HTML
    with open("index3.txt",'r',encoding='utf-8') as fin:
        with open("index2.html",'w',encoding='utf-8') as fout:
            texte = fin.read().split("\n")
            for ligne in texte:
                if "<!-- Liste des input -->" in ligne:
                    input_exemple = df['input_exemple_1']
                    for exemple in input_exemple:
                        mot = exemple.strip('"')
                        fout.write(f"                <p>{mot}</p>\n")
                    continue
                
                if "<!-- Code init -->" in ligne:
                    fout.write(f"{df['Code_init'][0]}")
                    continue
                
                if "<!-- OutputText1 -->" in ligne:
                    fout.write(f"{df['output_attendu_1'][0]}")
                    continue
                if "<!-- InputText1 -->" in ligne:
                    fout.write(f"{df['input_exemple_1'][0]}")
                    continue
                if "<!-- Rappel de la quête -->" in ligne:
                    fout.write(f"{df['Rappel_de_la_quete'][0]}")
                    continue
                if "//Input initial" in ligne:
                    input_exemple = df['input_exemple_1']
                    for exemple in input_exemple:
                        mot = exemple.strip('"')
                        fout.write(f"<p>{mot}</p>")
                    continue
                if "//id var" in ligne:
                    fout.write(f"        var id = '{id}'\n")
                    continue
                
                fout.write(f"{ligne}\n")
                
    #Ecriture JS
    with open("script.txt", 'r', encoding='utf-8') as fin:
        with open("index.js",'w',encoding='utf-8') as fout:
            texte = fin.read().split("\n")
            n = "\n"
            n2 = r"\n\ ".strip(" ") + "\n" 
            for ligne in texte:
                if "//liste indice" in ligne:
                    
                    mots = df['Indice_1'] 
                    fout.write(f"'Premier indice: ")
                    for mot in mots:
                        mot = mot +"\n"
                        if "'" in mot:
                            mot =mot.replace("'","\\'")
                        mot = mot.replace(n,n2)
                        fout.write(f"{mot}',\n")
                    mots = df['Indice_2']
                    fout.write(f"'Deuxieme indice: ")
                    for mot in mots:
                        mot = mot +"\n"
                        if "'" in mot:
                            mot = mot.replace("'","\\'")
                        mot = mot.replace(n,n2)
                        fout.write(f"{mot}',\n")
                    mots = df['Indice_3']
                    fout.write(f"'Troisieme indice:{n2}")
                    
                    for mot in mots:
                        mot = mot +"\n"
                        if "'" in mot:
                            mot = mot.replace("'","\\'")
                        mot = mot.replace(n,n2)
        
                        fout.write(f"{mot}")
                    fout.write(f"',\n")
                    
                    continue
                if "//liste input" in ligne:
                    
                    mots = df['input_exemple_1']
                    fout.write('"')
                    for mot in mots:
                        mot = mot + n2
                        fout.write(f"{mot}")
                    fout.write('",\n')
                    mots = df['input_exemple_2']
                    fout.write('"')
                    for mot in mots:
                        mot = mot + n2
                        fout.write(f"{mot}")
                    fout.write('",\n')
                    mots = df['input_exemple_3']
                    fout.write('"')
                    for mot in mots:
                        mot = mot + n2
                        fout.write(f"{mot}")
                    fout.write('"\n')
                    continue
                if "//liste output" in ligne:
                    mot = str([df['output_attendu_1'][0], df['output_attendu_2'][0], df['output_attendu_3'][0]]).strip("[").strip("]")
                    fout.write(f"{mot}\n")
                    continue
            
                fout.write(f"{ligne}\n")
        
                
                



            
                    
                



    
                



app = Flask(__name__)
CORS(app)  # Active les en-têtes CORS pour toutes les routes de l'application

@app.route('/', methods=["POST"])
def traiter_requete():
    data = request.json
    valeur = data.get('valeur')
    id = data.get('id')
    print(valeur)
    html(int(valeur), id)
     
    return jsonify({"message": "Commande PHP exécutée avec succès"})


# Dictionnaire pour stocker l'état de la mission pour chaque joueur
mission_states = {}

# Route pour mettre à jour l'état de la mission d'un joueur spécifique
@app.route('/update_mission_state', methods=['POST'])
def update_mission():
    data = request.json
    player_id = data.get('player_id')
    new_state = data.get('state')
    gold = data.get('gold')
    
    if player_id is None:
        return jsonify({'error': 'Identifiant du joueur manquant dans la requête'}), 400
    
    if new_state is None:
        return jsonify({'error': 'Nouvel état de la mission manquant dans la requête'}), 400
    
    # Mettre à jour l'état de la mission pour le joueur spécifié
    mission_states[player_id] = (new_state,gold)
    print(mission_states)
    return jsonify({'success': new_state}), 200

# Route pour récupérer l'état de la mission d'un joueur spécifique
@app.route('/get_mission_state', methods=['POST'])
def get_mission_state():
    data = request.json
    player_id = data.get('player_id')
    
    if not player_id:
        return jsonify({'error': 'Identifiant du joueur manquant dans la requête'}), 400
    
    # Récupérer l'état de la mission pour le joueur spécifié
    mission_state = mission_states.get(player_id)
    
    if mission_state is None:
        print(f"Mr {player_id} n'a pas de quete\n")
        return jsonify({'error': 'Aucun état de la mission trouvé pour le joueur spécifié'}), 404
    
    return jsonify({'mission_state': mission_state}), 200

if __name__ == "__main__":
    app.run(debug=False)


