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

import json
import os

#En fonction de la zone, retourne deux sets tout deux composés des quetes existante, l'un avec la diffictulté, l'autre non (en cas de changement de difficulté)
def lecture_txt(Tavern = 0):
    tavern = str(Tavern)
    fichier_txt = "Quete/quest" + tavern + ".txt"
    with open(fichier_txt,'r',encoding='utf-8') as fin:
        texte = fin.read().split("\n")
        texte2 = list()
        for ligne in texte:
            if ligne == "nan":
                ligne = ""
            texte2.append( ligne.split(r"\n"))
        Quete_tavern_complet = set()
        Quete_tavern_complet_0diff = set()
        n_ligne, n_colonne = list(map(int,texte2[0][0].split()))
        for quete in range(n_ligne):
            for i in range(n_colonne):
                if texte2[i+1][0] == "ID quete":
                    ID_quete = texte2[n_colonne + 1 + i*n_ligne + quete][0]
                    
                if texte2[i+1][0] == "Nom_Quete":
                    Nom_Quete = texte2[n_colonne + 1 + i*n_ligne + quete][0]
                if texte2[i+1][0] == "Difficulté":
                    Difficulté = texte2[n_colonne + 1 + i*n_ligne + quete][0]
            
            
            Quete_tavern_complet.add((ID_quete,Nom_Quete,Difficulté))
            Quete_tavern_complet_0diff.add((ID_quete,Nom_Quete))
                
    return Quete_tavern_complet,Quete_tavern_complet_0diff


#Créations des fichiers correspondant a la partie web/exercice
def html(Quest = 0,Id = 0, Tavern = 0):

    quete = Quest
    id = str(Id)
    tavern = str(Tavern)
    fichier_txt = "Quete/quest" + tavern + ".txt"
    

    with open(fichier_txt,'r',encoding='utf-8') as fin:
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
    ref_w = "test_new_" + id + ".py"
    with open(ref_w, 'w',encoding='utf-8') as fout:
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
    
    if quete == 1:
        ref_r = "Template/Page_aide_sup/assistant1html.txt"
    elif quete == 0:
        ref_r = "Template/Page_aide_sup/assistanthtml.txt"
    else :
        ref_r = "Template/index.txt"
    ref_w = "index_" + id + ".html"

    with open(ref_r,'r',encoding='utf-8') as fin:
        with open(ref_w,'w',encoding='utf-8') as fout:
            texte = fin.read().split("\n")
            for ligne in texte:
                if "<!-- Liste des input -->" in ligne:
                    input_exemple = df['input_exemple_1']
                    for exemple in input_exemple:
                        mot = exemple.strip('"')
                        fout.write(f"                <p>{mot}</p>\n")
                    continue
                if "<!-- Contenu de l'aide -->" in ligne:
                    aide = df['aide']
                    for phrase in aide:
                        phrase = phrase.strip('"')
                        fout.write(f"<p>{phrase}</p>\n")
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
                    rappel = df['Rappel_de_la_quete']
                    for phrase in rappel:
                        phrase = phrase.strip('"')
                        fout.write(f"<p>{phrase}</p>\n")
                    continue
                if '<script src="index.js"> </script>' in ligne:
                    new_line = '<script src="index_'+ id + '.js"> </script>\n'
                    fout.write(new_line)
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

    if quete == 1:
        ref_r = "Template/Page_aide_sup/assistant1js.txt"
    elif quete == 0:
        ref_r = "Template/Page_aide_sup/assistantjs.txt"
    else :
        ref_r = "Template/script.txt"
    ref_w = "index_" + id + ".js"
    with open(ref_r, 'r', encoding='utf-8') as fin:
        with open(ref_w,'w',encoding='utf-8') as fout:
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
                    outputs = df['output_attendu_1']
                    output_1 = ""
                    for output in outputs:
                          output_1 += output + n 
                    outputs = df['output_attendu_2']
                    output_2 = ""
                    for output in outputs:
                          output_2 += output + n 
                    outputs = df['output_attendu_3']
                    output_3 = ""
                    for output in outputs:
                          output_3 += output + n
                    mot = str([output_1,output_2,output_3]).strip("[").strip("]")
                    fout.write(f"{mot}\n")
                    continue
            
                fout.write(f"{ligne}\n")
    return df['Nom_Quete']
        
                
                



            
                    
                

import atexit


app = Flask(__name__)
CORS(app)  # Active les en-têtes CORS pour toutes les routes de l'application

def on_exit():
    print("Le programme a été arrêté.")

# Enregistrer la fonction on_exit pour qu'elle soit appelée lorsque le programme se termine
atexit.register(on_exit)
df_complet = lecture_txt()

#Crée la page quete
@app.route('/', methods=["POST"])
def traiter_requete():
    data = request.json
    valeur = data.get('valeur')
    id = data.get('id')
    print(valeur)
    name = html(int(valeur), id)
     
    return jsonify({"message": "Commande PHP exécutée avec succès","name": name})


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

#Obtenir toutes les missions pas encore faite pour le joueur
@app.route('/get_mission_tavern', methods=['POST'])
def get_mission_tavern():
    data = request.json
    # Convertir chaque paire "ID quete" et "Nom_Quete" en tuple et les ajouter à une liste
    pairs_list = [(item[0], item[1]) for item in data]

    # Convertir la liste de tuples en un ensemble
    Quete_faite = set(pairs_list)
    Quete_tavern_complet,Quete_tavern_complet_0diff = lecture_txt(0)

    Quete_a_faire_0diff = Quete_tavern_complet_0diff.difference(Quete_faite)
    Quete_a_faire = {(id_quete, nom_quete, difficulte) for id_quete, nom_quete, difficulte in Quete_tavern_complet if (id_quete, nom_quete) in Quete_a_faire_0diff}
    Quete_a_faire = json.dumps(list(Quete_a_faire), indent = 1)

    del(Quete_tavern_complet,Quete_tavern_complet_0diff,Quete_a_faire_0diff,Quete_faite)
    
    
    return Quete_a_faire, 200

#Supprime les fichiers en lien avec l quete créée
@app.route('/clear_quete', methods=['POST'])
def clear_quete():
    data = request.json
    Id_joueur = data.get('player_id')
    print(Id_joueur)
    if Id_joueur in mission_states:
        print("A supprimé")
        mission_states.pop(Id_joueur) 
    ref_html = "index_" + Id_joueur + ".html"
    ref_js = "index_" + Id_joueur + ".js"
    ref_py = "test_new_" + Id_joueur + ".py"
    if os.path.exists(ref_html):
        os.remove(ref_html)
    if os.path.exists(ref_js):
        os.remove(ref_js)
    if os.path.exists(ref_py):
        os.remove(ref_py)
    return jsonify({'success': 1}), 200

if __name__ == "__main__":
    app.run(debug=False)


