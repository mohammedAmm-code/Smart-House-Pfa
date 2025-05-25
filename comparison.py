import pandas as pd
from optimizers.linear_optimizer import optimize as linear_optimize
from optimizers.metaheuristic_optimizer import optimize as meta_optimize
from utils.metrics import evaluate

def compare_methods(file_path: str) -> dict:
    """
    Compare les performances des deux méthodes d'optimisation sur un fichier de données.

    Args:
        file_path (str): Chemin vers le fichier CSV des données simulées.

    Returns:
        dict: Dictionnaire contenant les résultats des deux méthodes + la meilleure.
    """
    # Charger les données de base
    try:
        df_original = pd.read_csv(file_path)
    except Exception as e:
        print(f"Erreur de lecture du fichier : {e}")
        return {}

    results = {}

    # --- Méthode linéaire ---
    df_linear = linear_optimize(df_original)
    cost_linear, auto_linear = evaluate(df_linear, consumption_col='optimized_consumption')
    results["linear"] = {
        "data": df_linear,
        "cost": round(cost_linear, 2),
        "autoconsumption": round(auto_linear, 2)
    }

    # --- Méthode métaheuristique ---
    df_meta = meta_optimize(df_original)
    cost_meta, auto_meta = evaluate(df_meta, consumption_col='optimized_consumption')
    results["metaheuristic"] = {
        "data": df_meta,
        "cost": round(cost_meta, 2),
        "autoconsumption": round(auto_meta, 2)
    }

    # --- Détermination de la meilleure méthode ---
    if cost_linear < cost_meta and auto_linear >= auto_meta:
        best = "linear"
    elif cost_meta < cost_linear and auto_meta >= auto_linear:
        best = "metaheuristic"
    else:
        # En cas d'égalité approximative : privilégier l'autoconsommation
        best = "linear" if auto_linear >= auto_meta else "metaheuristic"

    results["best_method"] = best
    return results


# Test manuel
if __name__ == "__main__":
    file_path = "data_simulation/data.csv"
    results = compare_methods(file_path)

    if results:
        print(f"\n✅ Meilleure méthode : {results['best_method'].upper()}")
        print("---- Résultats ----")
        print("Méthode linéaire :")
        print(f"  ➤ Coût            : {results['linear']['cost']} €")
        print(f"  ➤ Autoconsommation: {results['linear']['autoconsumption']} %")
        print("Méthode métaheuristique :")
        print(f"  ➤ Coût            : {results['metaheuristic']['cost']} €")
        print(f"  ➤ Autoconsommation: {results['metaheuristic']['autoconsumption']} %")
