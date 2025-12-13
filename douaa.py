import pandas as pd

# Création du tableau
data = {
    "Séquence": [
        "ATGCGTACGTA",
        "GCTAGCTAGGCC",
        "ATGCGCGTAAGT",
        "TACGATCGTA",
        "ATGAAAGGCTT",
        "CGTACGTAGC",
        "TTAACCGGAT"
    ],
    "Longueur": [12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}
df = pd.DataFrame(data)

print("Tableau initial :")
print(df)
print("\n-----------------------------\n")
# Question 2 : Afficher la colonne Longueur
print(df["Longueur"])
# Question 3 : Filtrer les séquences de longueur > 10
seq_longues = df[df["Longueur"] > 10]
print(seq_longues)

# Sauvegarder le DataFrame dans un fichier CSV
df.to_csv('sequences.csv', index=False)
print("\nLes informations ont été sauvegardées dans 'sequences.csv'")

# Sauvegarder les séquences longues dans un fichier CSV séparé
seq_longues.to_csv('sequences_longues.csv', index=False)
print("Les séquences de longueur > 10 ont été sauvegardées dans 'sequences_longues.csv'")
