"""
This is a boilerplate pipeline 'data_modelling'
generated using Kedro 0.18.10
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from typing import Dict, Tuple


def split_data(df: pd.DataFrame, test_size: float, random_state: int, target: str) -> Tuple:
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters/data_science.yml.
    Returns:
        Split data.
    """
    CLASE = target

    y = df[CLASE]
    X = df.drop([CLASE], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestClassifier:
    """Trains the linear regression model.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    return clf