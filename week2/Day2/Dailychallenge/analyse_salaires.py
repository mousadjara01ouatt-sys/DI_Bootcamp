"""
Défi quotidien : Gestion et analyse des données en Python
Dataset : Data Science Job Salary
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings("ignore")


print("=" * 65)
print("ETAPE 1 : CHARGEMENT ET EXPLORATION DU DATASET")
print("=" * 65)

df = pd.read_csv("ds_salaries.csv")

print(f"\nDimensions du dataset : {df.shape[0]} lignes x {df.shape[1]} colonnes")
print("\nApercu des 5 premieres lignes :")
print(df.head())

print("\nTypes de colonnes :")
print(df.dtypes)

print("\nStatistiques descriptives (colonnes numeriques) :")
print(df.describe())

print("\nValeurs manquantes par colonne :")
print(df.isnull().sum())

print("\nDistribution des niveaux d'experience :")
exp_map = {"EN": "Entry-level (Junior)", "MI": "Mid-level", "SE": "Senior", "EX": "Executive/Expert"}
print(df["experience_level"].map(exp_map).value_counts())




print("\n" + "=" * 65)
print("ETAPE 2 : NORMALISATION MIN-MAX DE LA COLONNE SALARY")
print("=" * 65)

print(f"\nSalaire avant normalisation :")
print(f"  Minimum  : {df['salary_in_usd'].min():>10,.0f} USD")
print(f"  Maximum  : {df['salary_in_usd'].max():>10,.0f} USD")
print(f"  Moyenne  : {df['salary_in_usd'].mean():>10,.0f} USD")
print(f"  Ecart-type: {df['salary_in_usd'].std():>10,.0f} USD")

# Application de la normalisation Min-Max
scaler = MinMaxScaler()
df["salary_normalized"] = scaler.fit_transform(df[["salary_in_usd"]])

print(f"\nSalaire apres normalisation Min-Max (colonne 'salary_normalized') :")
print(f"  Minimum  : {df['salary_normalized'].min():.6f}")
print(f"  Maximum  : {df['salary_normalized'].max():.6f}")
print(f"  Moyenne  : {df['salary_normalized'].mean():.6f}")
print(f"  Ecart-type: {df['salary_normalized'].std():.6f}")

print("\nVerification : les 5 premiers salaires bruts et leurs valeurs normalisees :")
check = df[["salary_in_usd", "salary_normalized"]].head()
check.columns = ["Salaire USD", "Salaire normalise (0-1)"]
print(check.to_string(index=False))

# Formule appliquee
sal_min = df['salary_in_usd'].min()
sal_max = df['salary_in_usd'].max()
print(f"\nFormule appliquee : (x - {sal_min:,}) / ({sal_max:,} - {sal_min:,})")
print("Toutes les valeurs salariales sont desormais comprises entre 0 et 1.")




print("\n" + "=" * 65)
print("ETAPE 3 : REDUCTION DE DIMENSIONNALITE AVEC PCA")
print("=" * 65)

# Encodage des variables categoriques pour la PCA
le = LabelEncoder()
df_encoded = df.copy()

categorical_cols = ["experience_level", "employment_type",
                    "employee_residence", "company_location", "company_size"]

for col in categorical_cols:
    df_encoded[col + "_enc"] = le.fit_transform(df_encoded[col])

# Selection des colonnes numeriques disponibles pour la PCA
numeric_cols = [
    "work_year",
    "salary_in_usd",
    "salary_normalized",
    "remote_ratio",
    "experience_level_enc",
    "employment_type_enc",
    "employee_residence_enc",
    "company_location_enc",
    "company_size_enc"
]

X = df_encoded[numeric_cols].values

print(f"\nNombre de caracteristiques (colonnes) avant PCA : {X.shape[1]}")
print(f"Colonnes utilisees : {numeric_cols}")

# Normalisation prealable a la PCA (bonne pratique)
scaler_pca = MinMaxScaler()
X_scaled = scaler_pca.fit_transform(X)

# Application de la PCA
pca = PCA()
pca.fit(X_scaled)

variance_ratio = pca.explained_variance_ratio_
variance_cumulative = np.cumsum(variance_ratio)

print("\nVariance expliquee par composante principale :")
print(f"  {'Composante':<15} {'Variance expliquee':>20} {'Variance cumulee':>18}")
print(f"  {'-'*55}")
for i, (var, cumvar) in enumerate(zip(variance_ratio, variance_cumulative)):
    marker = " <-- seuil 95%" if cumvar >= 0.95 and (i == 0 or variance_cumulative[i-1] < 0.95) else ""
    print(f"  PC{i+1:<13} {var*100:>19.2f}% {cumvar*100:>17.2f}%{marker}")

# Nombre de composantes pour 95% de variance
n_components_95 = np.argmax(variance_cumulative >= 0.95) + 1
print(f"\nNombre de composantes pour capturer 95% de la variance : {n_components_95}")

# Transformation finale avec le nombre optimal de composantes
pca_final = PCA(n_components=n_components_95)
X_pca = pca_final.fit_transform(X_scaled)

print(f"\nDimensions apres reduction PCA :")
print(f"  Avant : {X.shape[0]} lignes x {X.shape[1]} colonnes")
print(f"  Apres : {X_pca.shape[0]} lignes x {X_pca.shape[1]} composantes principales")
print(f"  Reduction : {X.shape[1] - X_pca.shape[1]} colonnes supprimees")
print(f"  Variance totale conservee : {pca_final.explained_variance_ratio_.sum()*100:.2f}%")

# Ajout des composantes au dataframe
for i in range(n_components_95):
    df_encoded[f"PC{i+1}"] = X_pca[:, i]

print("\nApercu des composantes principales (5 premieres lignes) :")
pc_cols = [f"PC{i+1}" for i in range(n_components_95)]
print(df_encoded[pc_cols].head().round(4).to_string())



print("\n" + "=" * 65)
print("ETAPE 4 : AGREGATION PAR NIVEAU D'EXPERIENCE")
print("=" * 65)

# Mapping des codes vers des libelles lisibles
experience_labels = {
    "EN": "Entry-level (Junior)",
    "MI": "Mid-level",
    "SE": "Senior",
    "EX": "Executive/Expert"
}

df["experience_label"] = df["experience_level"].map(experience_labels)

# Calcul des statistiques agregees
aggregation = df.groupby("experience_label")["salary_in_usd"].agg(
    Effectif="count",
    Salaire_Moyen="mean",
    Salaire_Median="median",
    Salaire_Min="min",
    Salaire_Max="max",
    Ecart_type="std"
).round(0)

# Tri par salaire moyen croissant
aggregation = aggregation.sort_values("Salaire_Moyen")

print("\nSalaires par niveau d'experience (en USD) :")
print("-" * 85)
print(f"  {'Niveau d experience':<25} {'Effectif':>9} {'Moyen':>12} {'Median':>12} {'Min':>10} {'Max':>10}")
print("-" * 85)

for level, row in aggregation.iterrows():
    print(f"  {level:<25} {int(row['Effectif']):>9,} "
          f"{int(row['Salaire_Moyen']):>12,} "
          f"{int(row['Salaire_Median']):>12,} "
          f"{int(row['Salaire_Min']):>10,} "
          f"{int(row['Salaire_Max']):>10,}")
print("-" * 85)

print("\nVariation salariale entre niveaux d'experience :")
levels = aggregation.index.tolist()
means = aggregation["Salaire_Moyen"].values
for i in range(1, len(levels)):
    delta = means[i] - means[i-1]
    pct = (delta / means[i-1]) * 100
    print(f"  {levels[i-1]} -> {levels[i]} : +{int(delta):,} USD (+{pct:.1f}%)")

print("\nEcart-type des salaires par niveau (dispersion) :")
for level, row in aggregation.iterrows():
    print(f"  {level:<25} : {int(row['Ecart_type']):,} USD")



print("\n" + "=" * 65)
print("SYNTHESE DES TRAITEMENTS EFFECTUES")
print("=" * 65)

print(f"""
1. CHARGEMENT
   - Dataset charge : {df.shape[0]} observations, {df.shape[1]} colonnes
   - Aucune valeur manquante detectee
   - Colonnes : {list(df.columns)}

2. NORMALISATION MIN-MAX
   - Colonne cible : salary_in_usd
   - Plage originale : [{sal_min:,} USD ; {sal_max:,} USD]
   - Plage apres normalisation : [0.000000 ; 1.000000]
   - Nouvelle colonne creee : salary_normalized

3. REDUCTION DE DIMENSIONNALITE (PCA)
   - {X.shape[1]} caracteristiques numeriques encodees en entree
   - {n_components_95} composantes principales conservees
   - Variance expliquee : {pca_final.explained_variance_ratio_.sum()*100:.2f}%
   - Reduction de {X.shape[1] - n_components_95} dimensions

4. AGREGATION PAR EXPERIENCE
   - 4 niveaux d'experience analyses : EN, MI, SE, EX
   - Salaire moyen Junior (EN)    : {int(aggregation.loc['Entry-level (Junior)', 'Salaire_Moyen']):,} USD
   - Salaire moyen Mid-level (MI) : {int(aggregation.loc['Mid-level', 'Salaire_Moyen']):,} USD
   - Salaire moyen Senior (SE)    : {int(aggregation.loc['Senior', 'Salaire_Moyen']):,} USD
   - Salaire moyen Expert (EX)    : {int(aggregation.loc['Executive/Expert', 'Salaire_Moyen']):,} USD
""")

print("Script termine avec succes.")
