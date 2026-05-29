# PRÉTRAITEMENT DES DONNÉES - DATASET TITANIC
# Exercices 1 à 7 : Pipeline complet de nettoyage et transformation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.impute import SimpleImputer
import warnings
warnings.filterwarnings("ignore")

plt.rcParams["figure.figsize"] = (10, 5)
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False
sns.set_palette("muted")

df = pd.read_csv("train.csv")
print("Dataset chargé avec succès !")
print(f"Dimensions initiales : {df.shape[0]} lignes x {df.shape[1]} colonnes\n")
print(df.head())


# EXERCICE 1 : DÉTECTION ET SUPPRESSION DES DOUBLONS

n_avant = len(df)
n_doublons = df.duplicated().sum()
print(f"\nNombre de lignes avant suppression : {n_avant}")
print(f"Nombre de lignes dupliquées détectées : {n_doublons}")

if n_doublons > 0:
    print("\nLignes dupliquées :")
    print(df[df.duplicated(keep=False)])

df = df.drop_duplicates(keep="first")
n_apres = len(df)

print(f"\nNombre de lignes après suppression : {n_apres}")
print(f"Lignes supprimées : {n_avant - n_apres}")


# EXERCICE 2 : GESTION DES VALEURS MANQUANTES

manquantes = df.isnull().sum()
manquantes = manquantes[manquantes > 0].sort_values(ascending=False)
print("\nColonnes avec valeurs manquantes :")
print(manquantes.to_frame("Nombre manquant")
                .assign(Pct=lambda x: (x["Nombre manquant"] / len(df) * 100).round(2)))

# Cabin : plus de 77% de valeurs manquantes, on supprime la colonne
df.drop(columns=["Cabin"], inplace=True)
print("\n[Cabin] Colonne supprimée (>77% de valeurs manquantes).")

# Age : ~20% manquant, imputation par la médiane (robuste aux outliers)
imputer_age = SimpleImputer(strategy="median")
df["Age"] = imputer_age.fit_transform(df[["Age"]])
print(f"[Age] Valeurs manquantes imputées par la médiane ({imputer_age.statistics_[0]:.1f} ans).")

# Embarked : seulement 2 valeurs manquantes, on remplace par le mode
mode_embarked = df["Embarked"].mode()[0]
df["Embarked"].fillna(mode_embarked, inplace=True)
print(f"[Embarked] 2 valeurs manquantes remplacées par le mode : '{mode_embarked}'.")

print(f"\nValeurs manquantes restantes : {df.isnull().sum().sum()}")


# EXERCICE 3 : INGÉNIERIE DES FONCTIONNALITÉS

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
print("\n[FamilySize] créé (SibSp + Parch + 1).")
print(df["FamilySize"].value_counts().sort_index())

df["IsAlone"] = (df["FamilySize"] == 1).astype(int)
print(f"\n[IsAlone] créé — {df['IsAlone'].sum()} passagers voyageaient seuls.")

df["Title"] = df["Name"].str.extract(r",\s*([^\.]+)\.", expand=False).str.strip()
print(f"\n[Title] Titres bruts extraits :")
print(df["Title"].value_counts())

titres_communs = ["Mr", "Miss", "Mrs", "Master"]
df["Title"] = df["Title"].apply(lambda t: t if t in titres_communs else "Rare")
print("\n[Title] Après regroupement :")
print(df["Title"].value_counts())

le_title = LabelEncoder()
df["Title_encoded"] = le_title.fit_transform(df["Title"])
print(f"\n[Title_encoded] créé. Mapping : "
      f"{dict(zip(le_title.classes_, le_title.transform(le_title.classes_)))}")


# EXERCICE 4 : DÉTECTION ET TRAITEMENT DES VALEURS ABERRANTES

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
df["Fare"].plot(kind="box", ax=axes[0], title="Fare avant traitement", color="steelblue")
df["Age"].plot(kind="box", ax=axes[1], title="Age avant traitement", color="salmon")
plt.tight_layout()
plt.savefig("outliers_avant.png", dpi=150)
plt.show()

def detect_outliers_iqr(series, name):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    n = ((series < lower) | (series > upper)).sum()
    print(f"[{name}] Q1={Q1:.2f}  Q3={Q3:.2f}  IQR={IQR:.2f} -> bornes [{lower:.2f}, {upper:.2f}] — {n} outliers détectés")
    return lower, upper

lower_fare, upper_fare = detect_outliers_iqr(df["Fare"], "Fare")
lower_age,  upper_age  = detect_outliers_iqr(df["Age"],  "Age")

# Fare est très asymétrique, on plafonne au quantile 0.98
fare_cap = df["Fare"].quantile(0.98)
print(f"\n[Fare] Quantile 0.98 = {fare_cap:.2f} — plafonnement appliqué.")
df["Fare"] = df["Fare"].clip(upper=fare_cap)

# Age : valeurs biologiquement plausibles, aucune modification nécessaire
print("[Age] Valeurs dans une plage plausible [0-80] — aucune modification.")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
df["Fare"].plot(kind="box", ax=axes[0], title="Fare après traitement", color="steelblue")
df["Age"].plot(kind="box",  ax=axes[1], title="Age après traitement",  color="salmon")
plt.tight_layout()
plt.savefig("outliers_apres.png", dpi=150)
plt.show()


# EXERCICE 5 : STANDARDISATION ET NORMALISATION

avant_scale = df[["Age", "Fare", "FamilySize"]].describe().round(2)

# Age -> StandardScaler (distribution proche de la normale)
scaler_std = StandardScaler()
df["Age_scaled"] = scaler_std.fit_transform(df[["Age"]])

# Fare et FamilySize -> MinMaxScaler (asymétriques ou bornées)
scaler_mm = MinMaxScaler()
df[["Fare_scaled", "FamilySize_scaled"]] = scaler_mm.fit_transform(df[["Fare", "FamilySize"]])

apres_scale = df[["Age_scaled", "Fare_scaled", "FamilySize_scaled"]].describe().round(3)

print("\nAvant mise à l'échelle :")
print(avant_scale)
print("\nAprès mise à l'échelle :")
print(apres_scale)


# EXERCICE 6 : ENCODAGE DES VARIABLES CATÉGORIELLES

# drop_first=True sur Sex pour éviter la multicolinéarité
dummies_sex      = pd.get_dummies(df["Sex"],      prefix="Sex",      drop_first=True)
dummies_embarked = pd.get_dummies(df["Embarked"], prefix="Embarked", drop_first=False)
dummies_title    = pd.get_dummies(df["Title"],    prefix="Title",    drop_first=False)

df = pd.concat([df, dummies_sex, dummies_embarked, dummies_title], axis=1)
df.drop(columns=["Sex", "Embarked", "Title"], inplace=True)

nouvelles_cols = list(dummies_sex.columns) + list(dummies_embarked.columns) + list(dummies_title.columns)
print("\nNouvelles colonnes créées :")
for c in nouvelles_cols:
    print(f"  {c}")
print(f"\nDimensions après encodage : {df.shape}")


# EXERCICE 7 : TRANSFORMATION DES DONNÉES — GROUPES D'AGE

bins   = [0, 12, 18, 60, 100]
labels = ["Enfant", "Adolescent", "Adulte", "Senior"]

df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels, right=True)
print("\n[AgeGroup] Distribution des groupes d'âge :")
print(df["AgeGroup"].value_counts().sort_index())

fig, ax = plt.subplots(figsize=(8, 4))
df["AgeGroup"].value_counts().sort_index().plot(
    kind="bar", ax=ax,
    color=["#4CAF50", "#2196F3", "#FF9800", "#9C27B0"],
    edgecolor="white", width=0.6
)
ax.set_title("Répartition des passagers par groupe d'âge")
ax.set_xlabel("Groupe d'âge")
ax.set_ylabel("Nombre de passagers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("age_groups.png", dpi=150)
plt.show()

dummies_age = pd.get_dummies(df["AgeGroup"], prefix="AgeGroup", drop_first=False)
df = pd.concat([df, dummies_age], axis=1)
df.drop(columns=["AgeGroup"], inplace=True)

print("\nColonnes créées pour AgeGroup :")
for c in dummies_age.columns:
    print(f"  {c}")


# RECAPITULATIF FINAL

print(f"""
Pipeline de prétraitement terminé :

  1. Doublons supprimés          : {n_avant - n_apres} ligne(s)
  2. Valeurs manquantes traitées :
       - Cabin     -> colonne supprimée (77% manquant)
       - Age       -> imputation par la médiane
       - Embarked  -> remplacement par le mode
  3. Nouvelles fonctionnalités   : FamilySize, IsAlone, Title
  4. Valeurs aberrantes          :
       - Fare      -> plafonnement au quantile 0.98
       - Age       -> aucune modification (plages plausibles)
  5. Mise à l'échelle            :
       - Age        -> StandardScaler
       - Fare, FamilySize -> MinMaxScaler
  6. Encodage catégoriel         : Sex, Embarked, Title (one-hot)
  7. Groupes d'âge               : AgeGroup créé et encodé

Dimensions finales : {df.shape[0]} lignes x {df.shape[1]} colonnes
""")

print("Colonnes finales :")
print(df.columns.tolist())

print("\nAperçu des 5 premières lignes :")
print(df.head())

df.to_csv("titanic_preprocessed.csv", index=False)
print("\nDataset prétraité sauvegardé : titanic_preprocessed.csv")