# luhn_algorithm.py

def verify_card_number(card_number):
    """
    Vérifie si un numéro de carte est valide en utilisant l'algorithme de Luhn.
    
    :param card_number: Numéro de carte sous forme de chaîne de caractères
    :return: True si le numéro est valide, False sinon
    """
    # Supprimer les espaces et les tirets
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Vérification de la longueur du numéro
    if len(card_number) < 13 or len(card_number) > 19:
        return False
    
    # Inverser le numéro pour itérer du dernier chiffre
    card_number = card_number[::-1]
    
    total = 0
    
    # Itérer sur chaque chiffre du numéro
    for i, digit in enumerate(card_number):
        # Convertir le caractère en entier
        digit = int(digit)
        
        # Si l'indice est impair (les chiffres à partir du 2e chiffre depuis la fin)
        if i % 2 != 0:
            # Doubler le chiffre
            digit *= 2
            # Si le résultat est plus grand que 9, ajouter les chiffres séparés
            if digit > 9:
                digit = digit - 9
        
        # Ajouter le chiffre ou le chiffre transformé à la somme totale
        total += digit
    
    # Si la somme totale est divisible par 10, le numéro est valide
    return total % 10 == 0

def main():
    """
    Fonction principale pour tester l'algorithme de Luhn.
    """
    card_number = input("Entrez un numéro de carte : ")
    if verify_card_number(card_number):
        print("VALID!")
    else:
        print("INVALID!")

if __name__ == "__main__":
    main()
