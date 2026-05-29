import json

notebook_content = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# 🏬 Rapport d'Intelligence Économique : Analyse Stratégique de la Performance des Supermarchés\n",
                "**Rôle :** Analyste de Données Senior  \n",
                "**Objectif :** Traduire les données de vente au détail du jeu de données *US Superstore* en insights exploitables et en recommandations diagnostiques à l'attention des décideurs."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 1. Définition et Préparation des Données\n",
                "Cette section initialise l'environnement de travail, charge (ou simule) le jeu de données, traite les valeurs manquantes/doublons, aligne les types de données temporelles et procède à l'ingénierie de fonctionnalités métiers."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import pandas as pd\n",
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "import ipywidgets as widgets\n",
                "from ipywidgets import interact, Dropdown, IntSlider\n",
                "from IPython.display import display\n",
                "import time\n",
                "import warnings\n",
                "\n",
                "warnings.filterwarnings('ignore')\n",
                "sns.set_theme(style=\"whitegrid\")\n",
                "\n",
                "# --- SIMULATION DU JEU DE DONNÉES US SUPERSTORE ---\n",
                "np.random.seed(42)\n",
                "n_records = 5000\n",
                "\n",
                "categories = ['Furniture', 'Office Supplies', 'Technology']\n",
                "sub_categories = {\n",
                "    'Furniture': ['Chairs', 'Tables', 'Bookcases', 'Furnishings'],\n",
                "    'Office Supplies': ['Paper', 'Binders', 'Appliances', 'Art', 'Fasteners'],\n",
                "    'Technology': ['Phones', 'Copiers', 'Machines', 'Accessories']\n",
                "}\n",
                "states = ['California', 'New York', 'Texas', 'Washington', 'Pennsylvania', 'Florida', 'Illinois', 'Ohio', 'Michigan', 'Virginia']\n",
                "products = [f'Product {i}' for i in range(1, 150)]\n",
                "\n",
                "sim_dates = pd.date_range(start='2020-01-01', end='2023-12-31', periods=n_records)\n",
                "sim_cat = np.random.choice(categories, n_records, p=[0.25, 0.55, 0.20])\n",
                "sim_sub = [np.random.choice(sub_categories[c]) for c in sim_cat]\n",
                "sim_states = np.random.choice(states, n_records, p=[0.20, 0.15, 0.12, 0.10, 0.08, 0.07, 0.08, 0.07, 0.07, 0.06])\n",
                "sim_sales = np.random.exponential(scale=200, size=n_records) + 10\n",
                "sim_discounts = np.random.choice([0.0, 0.2, 0.4, 0.7, 0.8], n_records, p=[0.5, 0.3, 0.1, 0.05, 0.05])\n",
                "\n",
                "# Règle métier : les fortes réductions détruisent le profit\n",
                "sim_profit = (sim_sales * 0.15) - (sim_sales * sim_discounts * 1.1) + np.random.normal(0, 15, n_records)\n",
                "\n",
                "df = pd.DataFrame({\n",
                "    'Row ID': range(1, n_records + 1),\n",
                "    'Order Date': sim_dates,\n",
                "    'Ship Date': sim_dates + pd.to_timedelta(np.random.randint(2, 6, n_records), unit='D'),\n",
                "    'Category': sim_cat,\n",
                "    'Sub-Category': sim_sub,\n",
                "    'State': sim_states,\n",
                "    'Product Name': np.random.choice(products, n_records),\n",
                "    'Sales': sim_sales,\n",
                "    'Quantity': np.random.randint(1, 10, n_records),\n",
                "    'Discount': sim_discounts,\n",
                "    'Profit': sim_profit\n",
                "})\n",
                "\n",
                "# Introduction artificielle d'anomalies\n",
                "df.loc[df.sample(n=15).index, 'State'] = np.nan\n",
                "df = pd.concat([df, df.sample(n=10)], ignore_index=True)\n",
                "\n",
                "print(\"Forme du jeu de données initial :\", df.shape)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Nettoyage et Ingénierie des Fonctionnalités\n",
                "**Justification des choix :**\n",
                "- Les doublons de lignes stricts sont supprimés car ils faussent les calculs de volumes financiers.\n",
                "- Les valeurs manquantes de la colonne géographique `State` sont supprimées (`dropna`) car la localisation exacte est indispensable pour nos segmentations d'analyse spatiale."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Suppression des doublons\n",
                "print(f\"Doublons détectés : {df.duplicated().sum()}\")\n",
                "df = df.drop_duplicates()\n",
                "\n",
                "# Traitement des valeurs manquantes\n",
                "df = df.dropna(subset=['State'])\n",
                "\n",
                "# Correction des types de données\n",
                "df['Order Date'] = pd.to_datetime(df['Order Date'])\n",
                "df['Ship Date'] = pd.to_datetime(df['Ship Date'])\n",
                "\n",
                "# Feature Engineering (Indicateurs clés de performance)\n",
                "df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100\n",
                "df['Order Year'] = df['Order Date'].dt.year\n",
                "df['Order Month'] = df['Order Date'].dt.month\n",
                "df['Order Month-Year'] = df['Order Date'].dt.to_period('M')\n",
                "\n",
                "print(f\"Forme finale après nettoyage : {df.shape}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Analyse Exploratoire Approfondie (Matplotlib + ipywidgets)\n",
                "Cette partie déploie des fonctions dynamiques de diagnostic visuel interactif pour suivre l'évolution des ventes mensuelles par catégorie ainsi que la centralisation géographique des revenus."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Préparation des structures temporelles\n",
                "monthly_sales = df.groupby(['Order Month-Year', 'Category'])['Sales'].sum().reset_index()\n",
                "monthly_sales['Date'] = monthly_sales['Order Month-Year'].dt.to_timestamp()\n",
                "\n",
                "def plot_monthly_sales(category='All'):\n",
                "    plt.figure(figsize=(14, 5))\n",
                "    if category == 'All':\n",
                "        total_monthly = df.groupby('Order Month-Year')['Sales'].sum()\n",
                "        plt.plot(total_monthly.index.to_timestamp(), total_monthly.values, \n",
                "                 marker='o', linewidth=2, color='navy', label='Total Corporate Sales')\n",
                "        plt.title('Séries Temporelles : Tendance Mensuelle des Ventes (Global)', fontsize=14, fontweight='bold')\n",
                "    else:\n",
                "        cat_data = monthly_sales[monthly_sales['Category'] == category]\n",
                "        plt.plot(cat_data['Date'], cat_data['Sales'], \n",
                "                 marker='s', linewidth=2, color='darkorange', label=category)\n",
                "        plt.title(f'Séries Temporelles : Tendance Mensuelle des Ventes - {category}', fontsize=14, fontweight='bold')\n",
                "    \n",
                "    plt.xlabel('Date du cycle commercial')\n",
                "    plt.ylabel('Chiffre d\\\'affaires ($)')\n",
                "    plt.grid(True, alpha=0.3)\n",
                "    plt.legend(loc='upper left')\n",
                "    plt.tight_layout()\n",
                "    plt.show()\n",
                "\n",
                "categories_options = ['All'] + list(df['Category'].unique())\n",
                "interact(plot_monthly_sales, category=Dropdown(options=categories_options, value='All', description='Catégorie :'));"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Performance des Ventes par État Régional"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=True)\n",
                "\n",
                "def plot_top_states(top_n=10):\n",
                "    plt.figure(figsize=(12, max(5, top_n * 0.4)))\n",
                "    top_states = state_sales.tail(top_n)\n",
                "    \n",
                "    bars = plt.barh(range(len(top_states)), top_states.values, color='steelblue', edgecolor='black', alpha=0.8)\n",
                "    plt.yticks(range(len(top_states)), top_states.index)\n",
                "    plt.xlabel('Chiffre d\\\'affaires Cumulé ($)', fontsize=11)\n",
                "    plt.ylabel('États Fédéraux', fontsize=11)\n",
                "    plt.title(f'Top {top_n} des États Américains par Performance Commerciale', fontsize=14, fontweight='bold')\n",
                "    \n",
                "    # Annotations dynamiques des barres financières\n",
                "    for bar in bars:\n",
                "        width = bar.get_width()\n",
                "        plt.text(width + (state_sales.max() * 0.01), bar.get_y() + bar.get_height()/2, \n",
                "                 f'${width:,.0f}', va='center', ha='left', fontsize=9, fontweight='bold')\n",
                "        \n",
                "    plt.grid(axis='x', linestyle='--', alpha=0.4)\n",
                "    plt.tight_layout()\n",
                "    plt.show()\n",
                "\n",
                "interact(plot_top_states, top_n=IntSlider(min=5, max=10, value=7, description='Sélection Top N :'));"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Communication des Insights Stratégiques (Seaborn)\n",
                "Mise en exergue des produits les plus générateurs de marge et diagnostic critique des politiques de démarques agressives."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "product_profit = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)\n",
                "\n",
                "plt.figure(figsize=(12, 6))\n",
                "ax = sns.barplot(x=product_profit.values, y=product_profit.index, palette='plasma', orient='h')\n",
                "plt.title('Top 10 des Produits les plus Rentables (Synthèse de la Marge)', fontsize=14, fontweight='bold', pad=15)\n",
                "plt.xlabel('Profit Net Total Réalisé ($)', fontsize=11)\n",
                "plt.ylabel('Désignation Catalogue Produit', fontsize=11)\n",
                "\n",
                "for i, profit in enumerate(product_profit.values):\n",
                "    ax.text(profit + (product_profit.max() * 0.01), i, f'${profit:,.0f}', va='center', fontsize=10, fontweight='bold')\n",
                "\n",
                "plt.grid(axis='x', linestyle=':', alpha=0.6)\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Analyse de la Stratégie de Remise : Seuil de Rentabilité"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "plt.figure(figsize=(13, 7))\n",
                "sns.scatterplot(data=df, x='Discount', y='Profit', hue='Category', alpha=0.6, s=60, palette='Set2')\n",
                "sns.regplot(data=df, x='Discount', y='Profit', scatter=False, color='crimson', line_kws={'linewidth': 2.5, 'linestyle': '--'})\n",
                "\n",
                "plt.axhline(y=0, color='black', linestyle='-', alpha=0.5, linewidth=1.5)\n",
                "plt.text(0.02, df['Profit'].min()*0.1, 'Zone de Pertes Économiques nettes', color='red', fontsize=12, fontweight='bold')\n",
                "plt.title('Diagnostic Stratégique : Impact du Taux de Remise sur la Rentabilité Globale', fontsize=14, fontweight='bold')\n",
                "plt.xlabel('Taux de Remise (Discount Rate)', fontsize=11)\n",
                "plt.ylabel('Marge / Profit Généré ($)', fontsize=11)\n",
                "plt.legend(title='Univers Produits', bbox_to_anchor=(1.02, 1), loc='upper left')\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Évaluation Comparative de la Méthodologie et Outils\n",
                "Cette section évalue les performances opérationnelles et logiques de rendu des outils de data visualisation."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "print(\"=== ANALYSE COMPARATIVE : MATPLOTLIB vs SEABORN ===\")\n",
                "\n",
                "# Évaluation de la rapidité d'exécution\n",
                "start_mt = time.time()\n",
                "plt.figure(figsize=(5, 3))\n",
                "plt.plot(df.groupby('Order Year')['Sales'].sum())\n",
                "plt.close()\n",
                "time_matplotlib = time.time() - start_mt\n",
                "\n",
                "start_sb = time.time()\n",
                "plt.figure(figsize=(5, 3))\n",
                "sns.lineplot(data=df.groupby('Order Year')['Sales'].sum().reset_index(), x='Order Year', y='Sales')\n",
                "plt.close()\n",
                "time_seaborn = time.time() - start_sb\n",
                "\n",
                "print(f\"• Temps d'exécution de base Matplotlib : {time_matplotlib:.4f} secondes\")\n",
                "print(f\"• Temps d'exécution de base Seaborn    : {time_seaborn:.4f} secondes\\n\")\n",
                "\n",
                "print(\"Arbitrage Méthodologique de l'Analyste :\")\n",
                "print(\"Pour l'exploration de données rapide (EDA), j'utiliserai Matplotlib car son exécution est plus fluide, rapide\")\n",
                "print(\"et s'intègre nativement à l'écosystème ipywidgets pour créer des contrôles interactifs granulaires.\")\n",
                "print(\"Pour les livrables destinés au comité de direction, je privilégierai Seaborn car cette bibliothèque fournit\")\n",
                "print(\"des palettes élégantes par défaut et gère automatiquement l'affichage statistique complexe (comme les lignes de régression).\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 5. Résumé Exécutif Automatisé et Recommandations Métiers\n",
                "Calcul automatisé des métriques financières globales pour la direction générale."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "total_sales = df['Sales'].sum()\n",
                "total_profit = df['Profit'].sum()\n",
                "margin_glob = (total_profit / total_sales) * 100\n",
                "high_disc_loss = (df[df['Discount'] > 0.2]['Profit'] < 0).mean() * 100\n",
                "furniture_disc_loss = (df[(df['Category'] == 'Furniture') & (df['Discount'] > 0.2)]['Profit'] < 0).mean() * 100\n",
                "\n",
                "print(\"=== RAPPORT DE SYNTHÈSE DESTINÉ AUX ACTIONNAIRES ===\")\n",
                "print(f\"• Chiffre d'affaires Global : ${total_sales:,.2f}\")\n",
                "print(f\"• Résultat Net Cumulé       : ${total_profit:,.2f}\")\n",
                "print(f\"• Taux de Marge Opérationnel: {margin_glob:.2f}%\")\n",
                "print(f\"• Alerte Risque Démarques   : {high_disc_loss:.1f}% des remises > 20% détruisent directement la marge net.\")\n",
                "print(f\"• Focus Univers Furniture   : {furniture_disc_loss:.1f}% des ventes de Meubles avec remise > 20% génèrent des pertes nettes.\")\n",
                "print(\"\\n--- PLAN D'ACTION ET RECOMMANDATIONS STRATÉGIQUES ---\")\n",
                "print(\"1. Encadrement des Démarques : Fixer un seuil maximal de remise standard à 20% pour préserver la rentabilité.\")\n",
                "print(\"2. Flux d'approbation Furniture : Imposer une validation managériale pour toute remise supérieure à 20% sur la catégorie Furniture.\")\n",
                "print(\"3. Allocation d'investissements géographiques : Concentrer les efforts marketing sur l'état de Californie, leader des ventes.\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 🧠 Option Avancée : Tableau de bord multi-graphiques unifié"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "def build_unified_dashboard():\n",
                "    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))\n",
                "    \n",
                "    # G1: Évolution temporelle globale\n",
                "    t_sales = df.groupby('Order Month-Year')['Sales'].sum()\n",
                "    ax1.plot(t_sales.index.to_timestamp(), t_sales.values, marker='o', color='teal', linewidth=2)\n",
                "    ax1.set_title('Évolution du Chiffre d\\\'Affaires Historique', fontsize=12, fontweight='bold')\n",
                "    ax1.tick_params(axis='x', rotation=30)\n",
                "    \n",
                "    # G2: Parts de ventes par catégorie\n",
                "    cat_revenue = df.groupby('Category')['Sales'].sum()\n",
                "    ax2.bar(cat_revenue.index, cat_revenue.values, color=['#4f81bd', '#c0504d', '#9bbb59'])\n",
                "    ax2.set_title('Répartition des Ventes par Catégorie', fontsize=12, fontweight='bold')\n",
                "    \n",
                "    # G3: Top 10 États\n",
                "    top_10 = state_sales.tail(10)\n",
                "    ax3.barh(range(len(top_10)), top_10.values, color='indigo', alpha=0.7)\n",
                "    ax3.set_yticks(range(len(top_10)))\n",
                "    ax3.set_yticklabels(top_10.index)\n",
                "    ax3.set_title('Top 10 des États par Contribution Financiére', fontsize=12, fontweight='bold')\n",
                "    \n",
                "    # G4: Scatter Plot d'arbitrage Remise vs Profit\n",
                "    for cat in df['Category'].unique():\n",
                "        sub = df[df['Category'] == cat]\n",
                "        ax4.scatter(sub['Discount'], sub['Profit'], label=cat, alpha=0.5)\n",
                "    ax4.axhline(y=0, color='red', linestyle='--', alpha=0.7)\n",
                "    ax4.set_title('Analyse Pivot : Marge Économique vs Taux de Remise', fontsize=12, fontweight='bold')\n",
                "    ax4.set_xlabel('Remise')\n",
                "    ax4.set_ylabel('Profit')\n",
                "    ax4.legend()\n",
                "    \n",
                "    plt.suptitle('Tableau de Bord Unifié d\\\'Intelligence Commerciale - US Superstore', fontsize=16, fontweight='bold', y=0.98)\n",
                "    plt.tight_layout()\n",
                "    plt.show()\n",
                "\n",
                "build_unified_dashboard()"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
}

file_path = "analyse_performance_superstore.ipynb"
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(notebook_content, f, indent=2, ensure_ascii=False)

print(f"Fichier Jupyter Notebook généré avec succès sous le nom : '{file_path}'")