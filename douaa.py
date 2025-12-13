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
# Question 4 : Pourcentage moyen de GC
moy_gc = df["Pourcentage GC"].mean()
print(format(moy_gc, ".3f"))

# Question 5 : Catégorie GC
def categorie_gc(gc):
    if gc > 55:
        return "Riche"
    elif 45 <= gc <= 55:
        return "Moyen"
    else:
        return "Faible"

df["Catégorie GC"] = df["Pourcentage GC"].apply(categorie_gc)
print(df)
        
    

# Question 6 : Nombre de G dans chaque séquence
df["Nombre de G"] = df["Séquence"].apply(lambda x: x.count("G"))
print(df)
# Question 7 : Écart-type
ecart_gc = df["Pourcentage GC"].std()
ecart_longueur = df["Longueur"].std()

print("Écart-type du %GC :", format(ecart_gc, ".3f"))
print("Écart-type de la longueur :", format(ecart_longueur, ".3f"))
# Question 8 : Sauvegarde en CSV
df.to_csv("tableau_sequences_adn.csv", index=False)
print("Fichier CSV sauvegardé avec succès")
    