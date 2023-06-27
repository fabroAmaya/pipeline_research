# %% [markdown]
# # Lectura de datos

# %%
import os
import pandas as pd
import papermill as pm
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# %%
df = pd.read_csv("storage/01_titanic_dataset.csv")
df.head(3)

# %% [markdown]
# ## Limpieza de datos

# %%
# Eliminar filas con valores faltantes
df.dropna(inplace=True)

# Eliminar columnas que no serán utilizadas en el modelo
df.drop(["deck", "embark_town", "alive", "class", "who"], axis=1, inplace=True)

# %% [markdown]
# ## Preprocesamiento

# %%
# Aplicar one-hot encoding a la variable embarked
embarked_onehot = pd.get_dummies(df["embarked"], prefix="embarked")
df.drop("embarked", axis=1, inplace=True)

# Concatenar el one-hot encoding al DataFrame original
df = pd.concat([df, embarked_onehot], axis=1)

# %%
# Convertir datos categóricos a numéricos
df["sex"] = df["sex"].map({"female": 1, "male": 0})

# %%
# Crear variable "family_size" que representa el tamaño de la familia (sibsp + parch + 1)
df["family_size"] = df["sibsp"] + df["parch"] + 1

# %%
# Crear variable "is_child" que indica si la persona es menor de edad (edad menor a 18 años)
df["is_child"] = df["age"] < 18

# %%
# Crear variable "age_group" que indica en qué rango de edades se encuentra la persona
bins = [0, 18, 30, 50, 100]
labels = ["0-18", "19-30", "31-50", "51+"]
df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)
age_group_onehot = pd.get_dummies(
    df["age_group"], prefix="age_group"
)  # ,drop_first=True
df = pd.concat([df, age_group_onehot], axis=1)
df.drop("age_group", axis=1, inplace=True)

# %% [markdown]
# ## Modelado

# %%
CLASE = "survived"

y = df[CLASE]
X = df.drop([CLASE], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, shuffle=True, stratify=y, random_state=42
)

# %%
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# %%
joblib.dump(clf, "storage/model.pkl")


