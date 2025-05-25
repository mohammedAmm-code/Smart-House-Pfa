import pandas as pd

def evaluate(dataframe: pd.DataFrame, consumption_col='optimized_consumption') -> tuple:
    """
    Évalue les performances d'un plan énergétique : coût + autoconsommation.

    Args:
        dataframe (pd.DataFrame): Données contenant 'production', 'grid_cost' et la consommation optimisée.
        consumption_col (str): Nom de la colonne à utiliser pour la consommation (par défaut : 'optimized_consumption').

    Returns:
        tuple: (coût total en €, taux d'autoconsommation en %)
    """
    df = dataframe.copy()

    # Calcul de l'énergie manquante (besoin d'acheter au réseau)
    df['grid_usage'] = (df[consumption_col] - df['production']).clip(lower=0)

    # Coût total en euros = énergie prélevée * prix par kWh
    total_cost = (df['grid_usage'] * df['grid_cost']).sum()

    # Autoconsommation = part de la consommation couverte par la production solaire
    used_solar = df[[consumption_col, 'production']].min(axis=1).sum()
    total_consumption = df[consumption_col].sum()
    autoconsumption_ratio = used_solar / total_consumption if total_consumption > 0 else 0

    return total_cost, round(autoconsumption_ratio * 100, 2)
