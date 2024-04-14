import requests
import sys

# URL de l'API Flask
api_url = 'http://127.0.0.1:5000/get_mission_state'

# ID du joueur dont vous souhaitez récupérer l'état de la mission
player_id = sys.argv[1]  # Remplacez 'player123' par l'identifiant réel du joueur

# Paramètres de la requête GET
params = {'player_id': player_id}

# Envoi de la requête GET
response = requests.get(api_url, params=params)

# Vérification du code de statut de la réponse
if response.status_code == 200:
    # Conversion de la réponse JSON en un dictionnaire Python
    data = response.json()
    
    # Vérification si la réponse contient une clé 'mission_state'
    if 'mission_state' in data:
        mission_state = data['mission_state']
        print(f"L'état de la mission du joueur {player_id} est : {mission_state}")
    else:
        print("La réponse ne contient pas la clé 'mission_state'.")
else:
    print(f"Erreur lors de la requête : {response.status_code}")
