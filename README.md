# APP – Identification de Langue par Fréquence de Lettres



## Table des Matières
- [Description](#description)
- [Fonctionnalités principales](#fonctionnalités-principales)
- [Étapes Clés du Projet](#étapes-clés-du-projet)
- [Fichiers Utilisés](#fichiers-utilisés)
- [Choix Techniques](#choix-techniques)
- [Prérequis](#prérequis)
- [Utilisation](#utilisation)
- [Exemple d’Exécution](#exemple-dexécution)

---

## Description

Ce projet propose un **script Python** permettant de :

1. **Charger** les fréquences d'utilisation des lettres pour plusieurs langues depuis un fichier CSV (`language_letter_frequencies.csv`).
2. **Demander** à l’utilisateur de choisir ou de fournir un texte à analyser.
3. **Extraire** et **compter** la fréquence de chaque lettre dans le texte choisi.
4. **Comparer** la distribution des lettres du texte avec celles des langues de référence en calculant une **distance de similarité**.
5. **Trier** les langues par ordre **croissant** de distance pour déterminer la langue la plus probable du texte.
6. **Afficher** les résultats sous forme d’**histogramme** pour une visualisation rapide des distances.

---

## Fonctionnalités principales

- **Lecture des fréquences de lettres** depuis un CSV (`language_letter_frequencies.csv`).
- **Sélection interactive** du fichier texte à analyser via un menu.
- **Comptage des lettres** et calcul des **fréquences en pourcentage** dans le texte.
- **Calcul de distance** basée sur la somme des écarts absolus des fréquences de lettres.
- **Tri Comptage** des distances pour organiser les langues par proximité.
- **Affichage graphique** des distances via **Matplotlib**, avec mise en évidence de la langue la plus probable.

---

## Étapes Clés du Projet

1. **Choix du Texte :**
   - L'utilisateur peut sélectionner un fichier texte prédéfini ou saisir le nom d’un fichier personnalisé.

2. **Traitement du Texte :**
   - Lecture du contenu du fichier texte.
   - Comptage des occurrences de chaque lettre, en ignorant les caractères spéciaux définis.
   - Calcul des fréquences de chaque lettre en pourcentage par rapport au total des lettres.

3. **Chargement des Fréquences de Référence :**
   - Lecture du fichier CSV (`language_letter_frequencies.csv`) contenant les fréquences de lettres pour 7 langues différentes (Anglais, Français, Allemand, Espagnol, Portugais, Italien, Néerlandais).
   - Stockage des fréquences dans des dictionnaires dédiés à chaque langue.

4. **Comparaison des Fréquences :**
   - Pour chaque langue, calcul de la distance totale en sommant les écarts absolus entre les fréquences des lettres du texte et celles de la langue de référence.
   - Les lettres absentes dans le texte sont comparées avec une fréquence de 0.

5. **Tri des Langues par Distance :**
   - Utilisation du **tri comptage** pour ordonner les langues selon la distance calculée, de la plus proche à la plus éloignée.

6. **Visualisation des Résultats :**
   - Création d’un histogramme représentant les distances pour chaque langue.
   - Mise en évidence de la langue avec la distance minimale (la langue la plus probable).

---

## Fichiers Utilisés

- **`language_letter_frequencies.csv`** : Contient les fréquences d’utilisation des lettres pour chaque langue.
- **Fichiers textes** : Divers fichiers textes disponibles pour l’analyse (ex. `fables_.txt`, `mobydick_.txt`, etc.).

---

## Choix Techniques

- **Distance de Similarité :**
  - La distance est calculée comme la somme des écarts absolus des fréquences des lettres entre le texte et chaque langue de référence.
  - Cette méthode permet de quantifier la similarité globale des distributions de lettres.

- **Tri Comptage :**
  - Utilisé pour trier les distances de manière efficace.
  - Approprié étant donné que les distances sont des valeurs entières limitées dans une plage définie.

- **Visualisation avec Matplotlib :**
  - Permet de générer des histogrammes clairs et informatifs.
  - Mise en évidence visuelle de la langue la plus probable grâce à des annotations et des modifications de couleur.

---

## Prérequis

- **Python 3.x** (version recommandée : 3.6 ou plus).
- Bibliothèques Python :
  - `csv` (intégrée)
  - `matplotlib` (pour la visualisation)
- **Fichier `language_letter_frequencies.csv`** à placer dans le **même dossier** que le script Python.
- **Fichiers textes** disponibles pour l’analyse, placés dans le même répertoire ou spécifiés par l’utilisateur.

---

## Utilisation

1. **Exécuter le script Python :**

    ```bash
    python identification_langue.py
    ```

2. **Suivre les instructions à l’écran :**
   - Sélectionnez un fichier texte à analyser en entrant le numéro correspondant.
   - Ou choisissez l’option 13 pour saisir un fichier personnalisé.

3. **Visualiser les résultats :**
   - Après traitement, un histogramme s’affichera montrant les distances pour chaque langue.
   - La langue avec la distance minimale sera mise en évidence comme la langue la plus probable du texte analysé.

---

## Exemple d’Exécution

```plaintext
Veuillez choisir un texte :
0: fables_.txt
1: lacomediehumaine_.txt
2: richardIII_.txt
3: hamlet_.txt
4: mobydick_.txt
5: lusiadas_.txt
6: osmaias_.txt
7: donquijote_.txt
8: faust_.txt
9: ladivinecomedie_.txt
10: deondergangdereersterareld_.txt
11: follasnovas_.txt
12: cantaresgallegos_.txt
13: Un autre texte (saisir son nom)

Numéro de votre choix : 5
Non trié!  {'Anglais': 12, 'Français': 8, 'Allemand': 15, 'Espagnol': 10, 'Portugais': 9, 'Italien': 11, 'Néerlandais': 14}
Trié!  {'Français': 8, 'Portugais': 9, 'Espagnol': 10, 'Italien': 11, 'Anglais': 12, 'Néerlandais': 14, 'Allemand': 15}
