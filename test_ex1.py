import pytest # importe module pytest pour test unitaire
from ExDebug1 import environnement_optimal # importe fonction d'un autre fichier

def test_environnement_optimal():
    #Arrange
    temp = 25
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Tout est sous contrôle!"

    #Act = appeler fonction a tester
    resultat_obtenu = environnement_optimal(temp, poussiere, humidite)

    #Assert : verifiation
    assert resultat_attendu == resultat_obtenu

def test_environnement_optimal_2():
    #Arrange
    temp = 30
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Environnement non optimal"

    #Act = appeler fonction a tester
    resultat_obtenu = environnement_optimal(temp, poussiere, humidite)

    #Assert : verifiation
    assert resultat_attendu == resultat_obtenu

def test_environnement_optimal_3():
    #Arrange
    temp = 25
    poussiere = "faible"
    humidite = 20
    resultat_attendu = "Environnement non optimal"

    #Act = appeler fonction a tester
    resultat_obtenu = environnement_optimal(temp, poussiere, humidite)

    #Assert : verifiation
    assert resultat_attendu == resultat_obtenu

def test_environnement_optimal_2():
    #Arrange
    temp = 30
    poussiere = "moyen"
    humidite = 25
    resultat_attendu = "Environnement non optimal"

    #Act = appeler fonction a tester
    resultat_obtenu = environnement_optimal(temp, poussiere, humidite)

    #Assert : verifiation
    assert resultat_attendu == resultat_obtenu


