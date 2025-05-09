# 🔐 Projet de Chiffrement : César et Vigenère

## ✅ Statut : Terminé

## 📖 Description

Ce projet implémente deux algorithmes classiques de chiffrement de texte en utilisant Python :

- **Chiffrement de César** : Un chiffrement par décalage simple où chaque lettre du texte est décalée d'un nombre spécifié dans l'alphabet.
- **Chiffrement de Vigenère** : Un algorithme de chiffrement plus complexe qui utilise une clé pour appliquer un décalage variable sur chaque lettre du texte.

### 🚀 Objectifs

- Apprendre la manipulation des chaînes de caractères en Python.
- Utiliser des fonctions pour implémenter des algorithmes classiques de chiffrement.
- Manipuler des boucles et des structures conditionnelles pour coder ces algorithmes.

---

## 🛠️ Fonctionnalités

### 1. **Chiffrement de César**

Le chiffrement de César déplace chaque lettre du texte par un nombre fixe de positions dans l'alphabet. Il est simple à mettre en œuvre et peut être utilisé pour des applications basiques de sécurité.

- **Exemple** :  
    - Texte original : `Hello Zaira`  
    - Décalage : `3`  
    - Texte chiffré : `Khoor Cdlud`

### 2. **Chiffrement de Vigenère**

Le chiffrement de Vigenère est plus avancé. Il utilise un mot-clé pour déterminer le décalage de chaque lettre du texte. C'est un chiffrement polyalphabétique qui améliore la sécurité par rapport au chiffre de César.

- **Exemple** :  
    - Texte chiffré : `mrttaqrhknsw ih puggrur`  
    - Clé : `python`  
    - Texte déchiffré : (résultat déchiffré affiché lors de l'exécution)

---

## 🧠 Concepts Python utilisés

- **Manipulation des chaînes de caractères** : Utilisation des boucles `for` pour parcourir chaque caractère du texte.
- **Calculs d'index** : Utilisation de l'index de l'alphabet pour réaliser les décalages dans les deux algorithmes.
- **Fonctions Python** : Création de fonctions pour le chiffrement et le déchiffrement avec des paramètres adaptés.

---

## 📁 Structure du projet

- **`cipher.py`** : Le fichier principal contenant l'implémentation des algorithmes de chiffrement.
- **`README.md`** : Ce fichier de documentation pour expliquer le projet.

---

## 📜 Exemple d'exécution

```bash
python cipher.py
```

**Sortie attendue :**

```
=== Chiffrement de César ===
Texte original : Hello Zaira
Décalage : 3
Texte chiffré : Khoor Cdlud

=== Chiffrement de Vigenère ===
Texte chiffré : mrttaqrhknsw ih puggrur
Clé : python
Texte déchiffré : exemple de texte déchiffré
```

---

## 📝 Fonctionnement du code

1. **Chiffrement de César** :  
     La fonction `caesar(text, shift)` prend un texte et un décalage en paramètre, puis applique un décalage sur chaque caractère alphabétique. Les autres caractères (espaces, symboles, etc.) sont conservés sans modification.

2. **Chiffrement de Vigenère** :  
     La fonction `vigenere(message, key, direction)` prend un message, une clé et une direction (`1` pour chiffrement, `-1` pour déchiffrement). La fonction `encrypt_vigenere()` chiffre et `decrypt_vigenere()` déchiffre le message.

---

## 🙌 Contribution

Si vous avez des suggestions d'amélioration ou si vous avez rencontré des problèmes, n'hésitez pas à ouvrir une issue ou une pull request. Toute contribution est la bienvenue !

---
