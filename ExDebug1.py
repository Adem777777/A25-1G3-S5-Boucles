def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température en °C (int ou float)
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : taux d’humidité en % (int ou float)

    Retour :
    - "Tout est sous contrôle!" si toutes les conditions sont respectées
    - "Environnement non optimal" sinon (après avoir affiché les problèmes détectés)
    """

    alerte = False

    # Vérification température
    if temp <= 18:
        print("Température trop basse")
        alerte = True
    elif temp >= 27:
        print("Température trop élevée")
        alerte = True

    # Vérification humidité
    if humidite <= 30:
        print("Humidité trop basse")
        alerte = True
    elif humidite >= 50:
        print("Humidité trop élevée")
        alerte = True

    # Vérification poussière
    if poussiere != "faible":
        print("Trop de poussière")
        alerte = True

    # Retour final
    if not alerte:
        return "Tout est sous contrôle!"
    else:
        return "Environnement non optimal"

while True:
    if __name__ == "__main__":

    #  print(environnement_optimal(25, "faible", 40))
        #temp = int(input("Entrez la température désirée:"))
        #poussiere = input("Entrez le niveau de poussiere:")
        #humidite = float(input("Entrez le niveau d'humidité:"))
        ordi1 = input("Entrez la température, niveau de poussière et niveau d'humidité séparé avec des espaces.")
        liste_ordi1 = ordi1.split(" ")
        ordi2 = input("Entrez la température, niveau de poussière et niveau d'humidité séparé avec des espaces pour le deuxième ordi.")
        liste_ordi2 = ordi2.split(" ")
        ordi3 = input("Entrez la température, niveau de poussière et niveau d'humidité séparé avec des espaces pour le troisième ordi.")
        liste_ordi3 = ordi3.split(" ")



        #print(environnement_optimal(temp, poussiere, humidite))
        print(environnement_optimal(float(liste_ordi1[0]), liste_ordi1[1], float(liste_ordi1[2])))

        print(environnement_optimal(float(liste_ordi2[0]), liste_ordi2[1], float(liste_ordi2[2])))

        print(environnement_optimal(float(liste_ordi3[0]), liste_ordi3[1], float(liste_ordi3[2])))
