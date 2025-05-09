# 🏦 Algorithme de Luhn : Vérification de Numéro de Carte

## ✅ Statut : Terminé

---

## 📖 Description

Ce projet implémente l'algorithme de Luhn, une méthode utilisée pour valider les numéros de carte bancaire, cartes de crédit, ou autres types de numéros d'identification. Il permet de vérifier si un numéro est valide ou non selon cette méthode.

---

## 🚀 Objectifs

- Implémenter l'algorithme de Luhn en Python.
- Manipuler les chaînes de caractères pour préparer les données d'entrée (numéro de carte).
- Effectuer des calculs simples sur les chiffres des numéros de carte.

---

## 🛠️ Fonctionnalités

### Vérification de la validité d'un numéro de carte

L'algorithme de Luhn suit les étapes suivantes :
1. Inverser le numéro de carte.
2. Additionner les chiffres à des positions impaires.
3. Multiplier les chiffres à des positions paires par 2 et sommer les chiffres obtenus.
4. Vérifier si la somme totale est divisible par 10.

#### Exemple :
- **Numéro de carte** : `4111-1111-4555-1141`
- **Résultat** : `VALID!`

---

## 🧠 Concepts Python utilisés

- **Manipulation des chaînes de caractères** : Utilisation de `translate()` pour retirer les symboles comme les tirets ou espaces.
- **Manipulation des indices de liste** : Inversion de chaîne et indexation pour séparer les chiffres pairs et impairs.
- **Conditions** : Validation du numéro de carte avec `(total % 10 == 0)`.

---

## 📁 Structure du projet

- **`luhn_algorithm.py`** : Contient l'implémentation principale de l'algorithme.
- **`README.md`** : Documentation expliquant le projet.

---

## 📜 Exemple d'exécution

```bash
python luhn_algorithm.py
```

### Sortie attendue :
```plaintext
54
VALID!
```

---

## 📝 Fonctionnement du code

### 1. Fonction `verify_card_number(card_number)`
- Prend un numéro de carte en entrée.
- Inverse le numéro et effectue les calculs nécessaires :
    - Addition des chiffres à des positions impaires.
    - Doublement des chiffres à des positions paires, avec gestion des résultats supérieurs ou égaux à 10.
- Retourne `True` si la somme totale est divisible par 10, indiquant que le numéro est valide.

### 2. Fonction `main()`
- Prend un numéro de carte sous forme de chaîne.
- Supprime les tirets ou espaces.
- Appelle `verify_card_number` pour déterminer la validité.

---

## 🙌 Contribution

Si vous avez des suggestions ou rencontrez des problèmes, ouvrez une issue ou une pull request. Toute contribution est la bienvenue !