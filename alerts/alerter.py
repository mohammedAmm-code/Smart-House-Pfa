import os
import json
from datetime import datetime

def send_alert(message):
    """Envoie une alerte et l'enregistre dans l'historique."""
    alert_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"🚨 ALERTE [{alert_time}] : {message}")
    
    # Enregistrer l'alerte dans un fichier JSON
    save_alert_to_history(alert_time, message)
    
    # Ici, vous pourriez ajouter du code pour envoyer un email ou un SMS
    # send_email_alert(message)
    # send_sms_alert(message)

def save_alert_to_history(timestamp, message):
    """Enregistre une alerte dans l'historique."""
    alert_dir = "alerts_history"
    if not os.path.exists(alert_dir):
        os.makedirs(alert_dir)
    
    alert_file = os.path.join(alert_dir, "alerts.json")
    
    # Charger l'historique existant
    if os.path.exists(alert_file):
        with open(alert_file, 'r') as f:
            try:
                alerts = json.load(f)
            except json.JSONDecodeError:
                alerts = []
    else:
        alerts = []
    
    # Ajouter la nouvelle alerte
    alerts.append({
        "timestamp": timestamp,
        "message": message
    })
    
    # Limiter à 100 alertes récentes
    if len(alerts) > 100:
        alerts = alerts[-100:]
    
    # Enregistrer l'historique mis à jour
    with open(alert_file, 'w') as f:
        json.dump(alerts, f, indent=4)

def get_recent_alerts(limit=10):
    """Récupère les alertes récentes."""
    alert_file = os.path.join("alerts_history", "alerts.json")
    
    if os.path.exists(alert_file):
        with open(alert_file, 'r') as f:
            try:
                alerts = json.load(f)
                return alerts[-limit:]  # Retourne les X dernières alertes
            except json.JSONDecodeError:
                return []
    return []

if __name__ == "__main__":
    send_alert("Consommation élevée détectée ! (Test)")
    
    # Afficher les alertes récentes
    recent_alerts = get_recent_alerts()
    if recent_alerts:
        print("\nAlertes récentes :")
        for alert in recent_alerts:
            print(f"[{alert['timestamp']}] {alert['message']}")