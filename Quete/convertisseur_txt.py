# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 00:40:00 2024

@author: thiba
"""

import pandas as pd

# Charger le fichier Excel
df = pd.read_excel('Classeur1.xlsx',dtype=str)
# df['Tests'] = None

# Parcourir chaque ligne du DataFrame
# for index, row in df.iterrows():
#     # Créer une liste de tuples pour stocker les résultats des tests
#     tests = []
    
#     # Parcourir les colonnes input_test_1 à input_test_3 et output_test_1 à output_test_3
#     for i in range(1, 4):
#         # Récupérer les valeurs des entrées et des sorties des tests
#         side_effects = df[f'input_test_{i}'][index]  # Convertir en liste et supprimer les valeurs NaN
#         expected_output = df[f'output_test_{i}'][index]  # Prendre la première valeur non-NaN
#         #side_effects_str = ', '.join([f'{item}' for item in side_effects])
#         # Ajouter le tuple (entrées, sortie attendue) à la liste des tests
#         tests.append((side_effects, expected_output))
    
#     # Mettre à jour la colonne Tests avec la liste des résultats des tests
#     df.at[index, 'Tests'] = tests

# Afficher le DataFrame avec les résultats des tests
#print(df['Tests'][0])

with open("quest0.txt",'w',encoding='utf-8') as fout:
    fout.write(f"{df.shape[0]} {df.shape[1]}\n")
    for column_name in df.columns:
        fout.write(f"{column_name}\n")
    for column_name in df.columns:
        var = df[column_name].values
        for i in range (len(var)):
            var[i] = str(var[i]).replace("\n","\\n")
            fout.write(f"{var[i]}\n")
            

    