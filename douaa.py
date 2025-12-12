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

# Affichage du tableau
print(df)
GTACGTAGC",
        "TTAACCGGAT"
    ],
    "Longueur": [12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}

df = pd.DataFrame(data)
# Affichage du tableau
print(df)

    "Longueur": [12, 12, 12, 10, 11, 10, 10],
    "Pourcentage_GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}

df = pd.DataFrame(data)

print("Tableau initial :")
print(df)
print("\n-----------------------------\n")
