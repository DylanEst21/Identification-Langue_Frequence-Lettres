import csv
import matplotlib.pyplot as plt


#1. Liste des fichiers textes disponibles
FILES_DICT = {
    0: "fables_.txt",
    1: "lacomediehumaine_.txt",
    2: "richardIII_.txt",
    3: "hamlet_.txt",
    4: "mobydick_.txt",
    5: "lusiadas_.txt",
    6: "osmaias_.txt",
    7: "donquijote_.txt",
    8: "faust_.txt",
    9: "ladivinecomedie_.txt",
    10: "deondergangdereersterareld_.txt",
    11: "follasnovas_.txt",
    12: "cantaresgallegos_.txt"
}



#2. Affichage du menu
def afficher_menu():
    print("\nVeuillez choisir un texte :")
    for num, nom_fichier in FILES_DICT.items():
        print(f"{num}: {nom_fichier}")
    print("13: Un autre texte (saisir son nom)")



#3. Choix du fichier
def choisir_fichier():

    while True:
        afficher_menu()
        choix_str = input("\nNuméro de votre choix : ")


        try:            # On essaie de convertir en entier
            choix = int(choix_str)

        except ValueError:
            print("Saisissez un nombre valide.\n")
            continue

        # Cas où l'utilisateur choisit un fichier existant dans la liste
        if 0 <= choix <= 12:
            nom_fic = FILES_DICT[choix]
            try:
                return open(nom_fic, "r", encoding="utf-8")

            except FileNotFoundError:
                print(f"Fichier {nom_fic} introuvable. Réessayez.\n")
                continue


        # Cas où l'utilisateur veut entrer un autre fichier
        elif choix == 13:
            nom_personnalise = input("Entrez le nom (ou chemin) du fichier : ")

            try:
                return open(nom_personnalise, "r", encoding="utf-8")

            except FileNotFoundError:
                print(f"Fichier {nom_personnalise} introuvable. Réessayez.\n")
                continue

        else:
            print("Choix hors intervalle. Réessayez.\n")




#4. Liste de caractères à ignorer
caract_spec = [",", "?", ";", ".", ":", "!", " ", "-", "'", "_", "¿", "¡", "...", "(", ")", "\n", "\ufeff", "»", "«", "'", '"', "%", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]



#5. Fonctions de comptage des lettres
def freq_caract_txt(lines_list):
    freq_dict = {}
    for ligne in lines_list:
        for char in ligne:
            caract = char.lower()
            if caract not in caract_spec:

                if caract not in freq_dict:
                    freq_dict[caract] = 1

                else:
                    freq_dict[caract] += 1

    return freq_dict



def compteur(lines_list):           # Renvoie le nombre total de lettres (hors caract_spec)
    compteur = 0
    for ligne in lines_list:
        for char in ligne:
            caract = char.lower()
            if caract not in caract_spec:
                compteur += 1

    return compteur



def freq_en_pourcentages(freq_dict, total):
    for lettre in freq_dict:
        freq_dict[lettre] = (freq_dict[lettre] / total) * 100

    return freq_dict



#6. Programme principal: ouverture, lecture, comptage
fichier = choisir_fichier()

# On lit toutes les lignes
contenu = fichier.readlines()
fichier.close()

# Calcul du nombre total de lettres (hors caractères spéciaux)
tot_caract_txt = compteur(contenu)

# Vérification si le texte n'est pas vide
if tot_caract_txt == 0:
    print("Le fichier choisi ne contient aucune lettre exploitable (ou est vide).")
    exit(0)

# Dictionnaire brut {lettre: occurrences}, puis en pourcentages
dict_freq_txt = freq_caract_txt(contenu)
dict_en_pourcentage_txt = freq_en_pourcentages(dict_freq_txt, tot_caract_txt)



#7. Lecture du CSV et création des 7 dictionnaires de langues
with open("language_letter_frequencies.csv") as fichier_csv:
    list_contenu = csv.reader(fichier_csv, delimiter=";")

    dict_anglais = {}
    dict_francais = {}
    dict_allemand = {}
    dict_espagnol = {}
    dict_portugais = {}
    dict_italien = {}
    dict_neerlandais = {}


    for ligne in list_contenu:
        lettre = ligne[0]

        try:
            dict_anglais[lettre] = float(ligne[1])

        except:
            dict_anglais[lettre] = 0.0

        try:
            dict_francais[lettre] = float(ligne[2])

        except:
            dict_francais[lettre] = 0.0

        try:
            dict_allemand[lettre] = float(ligne[3])

        except:
            dict_allemand[lettre] = 0.0

        try:
            dict_espagnol[lettre] = float(ligne[4])

        except:
            dict_espagnol[lettre] = 0.0

        try:
            dict_portugais[lettre] = float(ligne[5])

        except:
            dict_portugais[lettre] = 0.0

        try:
            dict_italien[lettre] = float(ligne[6])

        except:
            dict_italien[lettre] = 0.0

        try:
            dict_neerlandais[lettre] = float(ligne[7])

        except:
            dict_neerlandais[lettre] = 0.0




#8. Fonction de comparaison (calcul de distance)
def comparer(freq_texte, freq_langue):
    """
    Calcule la somme des écarts absolus pour chaque lettre.
    freq_texte: {lettre: pourcentage dans le texte}
    freq_langue: {lettre: pourcentage dans la langue}
    """

    compteur_distance = 0.0

    # On parcourt les lettres de la langue
    for lettre_lang in freq_langue.keys():

        # On cherche si cette lettre est dans le texte
        if lettre_lang in freq_texte:
            compteur_distance += abs(freq_langue[lettre_lang] - freq_texte[lettre_lang])

        else:
            compteur_distance += abs(freq_langue[lettre_lang] - 0)

    return compteur_distance



#9. Comparer le texte avec chacune des 7 langues
dict_distances = {}

def tout_comparer(freq_texte):
    """
    Remplit un dict {Langue: distance},
    en utilisant la fonction 'comparer' ci-dessus.
    """

    dict_distances["Anglais"] = comparer(freq_texte, dict_anglais)
    dict_distances["Français"] = comparer(freq_texte, dict_francais)
    dict_distances["Allemand"] = comparer(freq_texte, dict_allemand)
    dict_distances["Espagnol"] = comparer(freq_texte, dict_espagnol)
    dict_distances["Portugais"] = comparer(freq_texte, dict_portugais)
    dict_distances["Italien"] = comparer(freq_texte, dict_italien)
    dict_distances["Néerlandais"] = comparer(freq_texte, dict_neerlandais)

    return dict_distances


dict_langues_distances = tout_comparer(dict_en_pourcentage_txt)


#10. Convertir les distances float en int, pour pouvoir appliquer le tri par comptage
def dict_float_en_int(dict):
    for cle, val in dict.items():
        dict[cle] = int(val)

    return dict


dict_distances_int = dict_float_en_int(dict_langues_distances)
print("Non trié! ", dict_distances_int)



#11. Tri par comptage (des distances entières)
def tri_comptage(dic):                                  # Dans ce tri les valeurs entières deviennent des indices
    """
    Tri par dénombrement sur les valeurs d'un dictionnaire.
    On commence par trouver la borne supérieure
    puis on compte les occurrences pour chaque entier.
    """

    borneSup = 0                                        # détermination de la borneSup/ la valeur entière maximale présente dans tab
    for val in dic.values():
        if val > borneSup:
            borneSup = val

    # Tableau de comptage (avec des "0")
    tabComptage = [0] * (borneSup + 1)
    for val in dic.values():
        tabComptage[val] += 1

    # Tableau trié
    tab_result = []
    for i in range(len(tabComptage)):
        for _ in range(tabComptage[i]):
            tab_result.append(i)

    return tab_result


tab_int_tries = tri_comptage(dict_distances_int)        #uniquement les valeurs int triées (sans keys)


#12. Reconstituer un dictionnaire final trié
def dic_trie(dic, tab):                                  #Créer dictionnaire où on rassemble les int triés et les keys
    """
    Construit un dict final selon l'ordre des valeurs int triées (tab).
    Note: si plusieurs clés ont la même valeur, elles apparaîtront
    au fur et à mesure de la première trouvée.
    """

    final_dic = {}
    for val in tab:
        for cle, v in dic.items():
            if v == val and cle not in final_dic:            # On l'ajoute si la clé n'est pas déjà dedans
                final_dic[cle] = v
                break       #Pour ne pas redonder la même clé

    return final_dic


dict_final = dic_trie(dict_distances_int, tab_int_tries)
print("Trié! ", dict_final)



#13. Préparation des données pour l'histogramme
langues = []
distances = []

for cle, val in dict_final.items():       #sépare en 2 liste, mais que l'on peut faire correspondre, car trié
    langues.append(cle)
    distances.append(val)



#14. Création et affichage de l'histogramme
plt.bar(langues,distances, width=0.6, color="royalblue", edgecolor="black", linewidth=2)
plt.xlabel("Langues", fontsize=12)
plt.ylabel("Distance par rapport au texte", fontsize=12)
plt.title("Distances des diverses langues par rapport au texte", fontsize=16)
plt.show()

