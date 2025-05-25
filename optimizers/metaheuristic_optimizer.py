import pandas as pd
import random

def optimize(dataframe: pd.DataFrame, attempts=10) -> pd.DataFrame:
    """
    Optimisation "métaheuristique" simple : essaie plusieurs stratégies aléatoires de réduction de la consommation
    pour maximiser l'autoconsommation.

    Args:
        dataframe (pd.DataFrame): Données avec 'production' et 'consumption'.
        attempts (int): Nombre de tentatives d’optimisation aléatoire à tester.

    Returns:
        pd.DataFrame: DataFrame avec la meilleure stratégie (colonne 'optimized_consumption').
    """
    best_df = None
    best_score = -1

    for _ in range(attempts):
        df = dataframe.copy()

        # Réduction aléatoire de la consommation (entre 0% et 30%)
        df['optimized_consumption'] = df.apply(
            lambda row: row['consumption'] * random.uniform(0.7, 1.0),
            axis=1
        )

        # Calculer le score d’autoconsommation
        used_solar = df[['optimized_consumption', 'production']].min(axis=1).sum()
        total_consumption = df['optimized_consumption'].sum()
        autoconsumption_ratio = used_solar / total_consumption if total_consumption > 0 else 0

        if autoconsumption_ratio > best_score:
            best_score = autoconsumption_ratio
            best_df = df

    return best_df
