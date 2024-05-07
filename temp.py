# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:56:40 2024

@author: thiba
"""



import json
import os
import pandas as pd

#En fonction de la zone, retourne deux sets tout deux composés des quetes existante, l'un avec la diffictulté, l'autre non (en cas de changement de difficulté)
def lecture_txt(Tavern = 0):
    tavern = str(Tavern)
    fichier_txt = "Quete/quest" + tavern + ".txt"
    df = pd.read_excel('Quete/Aventure.xlsx',dtype=str)
    df.fillna("", inplace=True)
    Quete_tavern_complet = set()
    Quete_tavern_complet_0diff = set()      
    for index, row in df.iterrows():   
        Quete_tavern_complet.add((str(df["ID quete"][index]),str(df["Nom_Quete"][index]),str(df["Difficulté"][index])))
        Quete_tavern_complet_0diff.add((str(df["ID quete"][index]),str(df["Nom_Quete"][index])))
                
    return Quete_tavern_complet,Quete_tavern_complet_0diff


#Créations des fichiers correspondant a la partie web/exercice
def html(Quest = 0,Id = 0, Tavern = 0):

    quete = Quest
    id = str(Id)
    tavern = str(Tavern)
    fichier_txt = "Quete/quest" + tavern + ".txt"
    

    df = pd.read_excel('Quete/Aventure.xlsx',dtype=str)
    df.fillna("", inplace=True)
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].str.replace("\n", "\\n")

    df = df[df['ID quete'] == str(Quest)]
    df['Tests'] = None

    for index, row in df.iterrows():
        # Créer une liste de tuples pour stocker les résultats des tests
        tests = []
        
        # Parcourir les colonnes input_test_1 à input_test_3 et output_test_1 à output_test_3
        var = df['n_test']
        for i in range(1, int(df['n_test'])+1):
            # Récupérer les valeurs des entrées et des sorties des tests
            side_effects = df[f'input_test_{i}'][index]  # Convertir en liste et supprimer les valeurs NaN
            expected_output = df[f'output_test_{i}'][index]  # Prendre la première valeur non-NaN
            #side_effects_str = ', '.join([f'{item}' for item in side_effects])
            # Ajouter le tuple (entrées, sortie attendue) à la liste des tests
            tests.append((side_effects, expected_output))
        
        # Mettre à jour la colonne Tests avec la liste des résultats des tests
        df['Tests'] = [tests]
        a = list(df['Tests'])


            
    n1 = "\\n"         
    
        
            
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
        print(list(df['Tests']))
        for index, row in df.iterrows():
            for side_effects, expected_output in row['Tests']: #Le 0 correspondra a la quete a faire
                
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
                    fout.write(f"{df['Code_init']}")
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

# html(Quest = 2,Id = 0, Tavern = 0) 
lecture_txt(1)