from flask import Flask, render_template, jsonify
import pandas as pd
import os
import sys

# Ajouter le chemin du répertoire parent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importer depuis le module data_analysis
from data_analysis.analyzer import detect_overconsumption

app = Flask(__name__)

@app.route('/')
def index():
    data_file = os.path.join('data_simulation', 'data.csv')
    data = None
    if os.path.exists(data_file):
        df = pd.read_csv(data_file)
        # Ne prends que les 20 dernières lignes au lieu de 10 pour mieux visualiser les tendances
        data = df.tail(20).to_dict(orient='records')
        
        # Calculer des statistiques utiles
        stats = {
            "total_production": round(df['production'].sum(), 2),
            "total_consumption": round(df['consumption'].sum(), 2),
            "avg_production": round(df['production'].mean(), 2),
            "avg_consumption": round(df['consumption'].mean(), 2),
            "max_consumption": round(df['consumption'].max(), 2)
        }
        
        # Détecter les anomalies
        anomalies = detect_overconsumption(data_file)
        recent_anomalies = not anomalies.empty
    else:
        stats = {}
        recent_anomalies = False
        
    return render_template('index.html', data=data, stats=stats, has_anomalies=recent_anomalies)

# Ajouter une route API pour actualiser les données sans recharger la page
@app.route('/api/data')
def get_data():
    data_file = os.path.join('data_simulation', 'data.csv')
    if os.path.exists(data_file):
        df = pd.read_csv(data_file)
        data = df.tail(20).to_dict(orient='records')
        return jsonify(data)
    return jsonify([])

if __name__ == '__main__':
    # Assurez-vous que le dossier data_simulation existe
    os.makedirs('data_simulation', exist_ok=True)
    app.run(debug=True)