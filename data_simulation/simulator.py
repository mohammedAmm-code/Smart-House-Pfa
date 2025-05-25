import random
import time
import os
import pandas as pd
from datetime import datetime, timedelta

def generate_data(simulate_past=False, past_hours=None):
    """Génère des données de production et consommation énergétique."""
    if simulate_past and past_hours:
        timestamp = datetime.now() - timedelta(hours=past_hours)
    else:
        timestamp = datetime.now()
    
    hour = timestamp.hour

    # Production solaire
    if 8 <= hour <= 18:
        production = round(random.uniform(2.0, 5.0), 2)
    else:
        production = round(random.uniform(0.1, 1.5), 2)
    
    # Consommation énergétique
    if 7 <= hour <= 9 or 18 <= hour <= 22:
        consumption = round(random.uniform(2.5, 4.5), 2)
    else:
        consumption = round(random.uniform(0.5, 3.0), 2)
    
    # Coût d’énergie du réseau (valeur constante ou simulée)
    grid_cost = round(random.uniform(0.12, 0.20), 2)  # €/kWh

    return {
        "timestamp": timestamp,
        "production": production,
        "consumption": consumption,
        "grid_cost": grid_cost
    }


def simulate_data(filepath, interval=5, populate_history=False):
    """Simule l'écriture continue de données dans un fichier CSV."""
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_exists = os.path.exists(filepath)
    
    # Optionnellement générer des données historiques pour avoir un jeu initial
    if populate_history and not file_exists:
        print("Génération de l'historique des données...")
        history_data = []
        for i in range(48):  # 48 heures d'historique
            history_data.append(generate_data(simulate_past=True, past_hours=48-i))
        
        df_history = pd.DataFrame(history_data)
        df_history.to_csv(filepath, index=False)
        file_exists = True
        print(f"Historique généré avec {len(history_data)} entrées.")
    
    print(f"Début de la simulation en continu. Données enregistrées dans {filepath}")
    print("Appuyez sur Ctrl+C pour arrêter la simulation.")
    
    try:
        while True:
            data = generate_data()
            df = pd.DataFrame([data])
            df.to_csv(filepath, mode='a', index=False, header=not file_exists)
            print(f"Données simulées : {data}")
            file_exists = True
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nSimulation arrêtée par l'utilisateur.")

if __name__ == "__main__":
    data_file = os.path.join("data_simulation", "data.csv")
    simulate_data(data_file, interval=5, populate_history=True)