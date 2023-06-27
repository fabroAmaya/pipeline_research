"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.18.10
"""
import pandas as pd

def drop_features(df: pd.DataFrame, list_drop_features: list) -> pd.DataFrame:
    df.dropna(inplace=True)
    df.drop(list_drop_features, axis=1, inplace=True)
    return df

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    # Aplicar one-hot encoding a la variable embarked
    embarked_onehot = pd.get_dummies(df["embarked"], prefix="embarked")
    df.drop("embarked", axis=1, inplace=True)

    # Concatenar el one-hot encoding al DataFrame original
    df = pd.concat([df, embarked_onehot], axis=1)

    # Convertir datos categóricos a numéricos
    df["sex"] = df["sex"].map({"female": 1, "male": 0})

    # Crear variable "family_size" que representa el tamaño de la familia (sibsp + parch + 1)
    df["family_size"] = df["sibsp"] + df["parch"] + 1

    # Crear variable "is_child" que indica si la persona es menor de edad (edad menor a 18 años)
    df["is_child"] = df["age"] < 18

    # Crear variable "age_group" que indica en qué rango de edades se encuentra la persona
    bins = [0, 18, 30, 50, 100]
    labels = ["0-18", "19-30", "31-50", "51+"]
    df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)
    age_group_onehot = pd.get_dummies(
        df["age_group"], prefix="age_group"
    )  # ,drop_first=True
    df = pd.concat([df, age_group_onehot], axis=1)
    df.drop("age_group", axis=1, inplace=True)

    return df