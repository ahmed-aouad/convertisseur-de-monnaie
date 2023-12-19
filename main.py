import forex_python
from forex_python.converter import CurrencyRates

# Liste pour stocker l'historique des conversions
historique = []

# Créer un objet CurrencyRates pour la conversion de devises
convertisseur = CurrencyRates()

# Boucle principale du programme de conversion de devises
while True:
    try:
        # Demander à l'utilisateur s'il souhaite ajouter une nouvelle devise ou non
        rep = input("Voulez-vous ajouter une devise ? (1=oui/2=non) ")

        if rep == "2":
            # L'utilisateur souhaite effectuer une conversion de devises

            # Saisir les détails de la conversion
            montant_a_convertir = float(input("Montant à convertir : "))
            votre_devise = str(input("Votre devise : "))
            devise_souhaitée = str(input("Devise souhaitée : "))

            # Effectuer la conversion de devises à l'aide de l'objet CurrencyRates
            resultat = convertisseur.convert(votre_devise, devise_souhaitée, montant_a_convertir)

            # Afficher les résultats
            print(f"{montant_a_convertir} {votre_devise} équivaut à {resultat:.2f} {devise_souhaitée}")

            # Ajouter la conversion à l'historique
            historique.append(f"{montant_a_convertir} {votre_devise} équivaut à {resultat:.2f} {devise_souhaitée}")

            # Demander à l'utilisateur s'il souhaite consulter l'historique des conversions
            histo = input("Voulez-vous avoir l'historique ? (1=oui/2=non)")

            if histo == "1":
                # Afficher l'historique des conversions
                for i in historique:
                    print(i)

        elif rep == "1":
            # L'utilisateur souhaite ajouter manuellement une conversion à l'historique

            # Saisir les détails de la conversion manuelle
            montant2 = float(input("Quel est le montant ? : "))
            devise = input("Quelle est la première devise ? : ")
            devise2 = input("Quelle est la deuxième devise ? : ")
            tx = float(input("Quel est le taux de change entre les deux devises ? :"))

            # Calculer le résultat de la conversion manuelle
            result = montant2 * tx

            # Afficher le résultat et l'ajouter à l'historique
            print(f"{montant2} {devise} équivaut à {result:.2f} {devise2} (taux de change : {tx})")
            historique.append(f"{montant2} {devise} équivaut à {result:.2f} {devise2} (taux de change : {tx})")

            # Demander à l'utilisateur s'il souhaite consulter l'historique des conversions
            reponse = input("Voulez-vous avoir l'historique ? (1=oui/2=non)")

            if reponse == "1":
                # Afficher l'historique des conversions
                print("HISTORIQUE :")
                for i in historique:
                    print(i)

    except Exception as e:
        # Gérer les exceptions et afficher un message d'erreur
        print(f"Erreur : {e}")
        break  # Sortir de la boucle en cas d'exception







