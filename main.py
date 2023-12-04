import forex_python
from forex_python.converter import CurrencyRates

historique = []

convertisseur = CurrencyRates()

while True:   

    try:
        rep=input("voulez vous ajouter une devise ?:(1=oui/2=non) ")
        if rep == ("2"):
        # Exemple d'utilisation
            montant_a_convertir= float(input("Montant à convertir: "))
            votre_devise = str(input("Votre devise: "))
            devise_souhaitée = str(input("devise souhaitée: "))
        

            # taux de change
            resultat = convertisseur.convert(votre_devise, devise_souhaitée, montant_a_convertir)

            

            # Afficher les résultats
            print(f"{montant_a_convertir} {votre_devise} équivaut à {resultat:.2f} {devise_souhaitée}")

            historique.append(f"{montant_a_convertir} {votre_devise} équivaut à {resultat:.2f} {devise_souhaitée}")

            histo=input("voulez vous avoir l'historique ?:(1=oui/2=non)")   
            if histo== "1":
                for i in historique:
                    print (i)

        elif rep=="1":
        
                 
            montant2=float(input("quel est le montant ? : "))
            devise=input("quelle est la premiere devise ? : ")
            devise2=input("quelle est la deuxieme devise ? : ")
            tx=float(input("quelle est le taux de change entre les deux devises ? :"))
            result= montant2 * tx
            print(f"{montant2} {devise} équivaut à {result:.2f} {devise2}(taux de change : {tx})")
            historique.append(f"{montant2} {devise} équivaut à {result:.2f} {devise2}(taux de change : {tx})")
            reponse=input("voulez vous avoir l'historique ?:(1=oui/2=non)")
            if reponse== "1":
                print("HISTORIQUE :")
                for i in historique:
                    print(i)    

    except Exception as e:
        print(f"Erreur : {e}")
        break







