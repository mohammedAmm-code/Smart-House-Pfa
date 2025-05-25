import pandas as pd

def optimize(dataframe: pd.DataFrame, margin_ratio=1.1) -> pd.DataFrame:
    """
    Optimise la consommation en limitant la consommation à la production solaire + marge.
    
    Args:
        dataframe (pd.DataFrame): Données originales contenant 'production' et 'consumption'.
        margin_ratio (float): Coefficient autorisé au-dessus de la production (ex : 1.1 = +10%)
    
    Returns:
        pd.DataFrame: Nouvelle version du DataFrame avec colonne 'optimized_consumption'.
    """
    df = dataframe.copy()

    # Appliquer la règle : consommation limitée à production * marge
    df['optimized_consumption'] = df.apply(
        lambda row: min(row['consumption'], row['production'] * margin_ratio),
        axis=1
    )
    
    return df
