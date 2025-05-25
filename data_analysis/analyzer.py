import pandas as pd
import os
from alerts.alerter import send_alert  # Importer depuis le module alerts

def detect_overconsumption(file_path, threshold=3.5):
    """Analyse la consommation et détecte les dépassements du seuil."""
    try:
        df = pd.read_csv(file_path)
        anomalies = df[df['consumption'] > threshold]
        
        # Envoyer des alertes pour les anomalies récentes (dernières 5 entrées)
        recent_df = df.tail(5)
        recent_anomalies = recent_df[recent_df['consumption'] > threshold]
        
        if not recent_anomalies.empty:
            for _, row in recent_anomalies.iterrows():
                send_alert(f"Consommation excessive ({row['consumption']} kWh) détectée à {row['timestamp']}")
        
        # Calcul des métriques d'efficacité
        df['efficiency'] = df['production'] / df['consumption']
        
        return anomalies
    except Exception as e:
        print(f"Erreur d'analyse : {e}")
        return pd.DataFrame()

def generate_daily_report(file_path):
    """Génère un rapport quotidien des données énergétiques."""
    try:
        df = pd.read_csv(file_path)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['date'] = df['timestamp'].dt.date
        
        # Regrouper par jour
        daily = df.groupby('date').agg({
            'production': 'sum',
            'consumption': 'sum'
        }).reset_index()
        
        daily['balance'] = daily['production'] - daily['consumption']
        daily['efficiency'] = daily['production'] / daily['consumption']
        
        return daily
    except Exception as e:
        print(f"Erreur de génération du rapport : {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    data_file = os.path.join('data_simulation', 'data.csv')
    if os.path.exists(data_file):
        anomalies = detect_overconsumption(data_file)
        if not anomalies.empty:
            print("Anomalies détectées :")
            print(anomalies)
        else:
            print("Aucune anomalie détectée.")
            
        # Générer un rapport quotidien
        report = generate_daily_report(data_file)
        if not report.empty:
            print("\nRapport quotidien :")
            print(report)