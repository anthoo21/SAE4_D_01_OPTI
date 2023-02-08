import math
from methodeLecture import lecture_fichier

def calculIndicateurs() : #Méthode utile pour l'affichage des indicateurs et pour l'algo1
    
    #Initialisations des variables
    indicateursX = []  # Moyenne des x, médiane des x, variance de x, écartType de x
    indicateursY = []  # Moyenne des y, médiane des y, variance de y, écartType de y
    indicateursXY = [] # Covariance, 'coefficient de corrélation linéaire'
    sommeAll = 0       # Permet de calculer la somme des x et y
    sommeQuadraX = 0   # Sert à faire la somme des x au carré
    sommeQuadraY = 0   # Sert à faire la somme des y au carré
    #Fin des initialisations

    #Calculs concernant les surfaces(valeur x) du jeu de données
    #Moyenne des x
    moyenneX = sum(surface_appartements)/len(surface_appartements)
    indicateursX.append(moyenneX) #Ajout au tableau

    #Médiane des x
    tailleListe = len(surface_appartements)   #Méthode qui donne la taille de la liste
    listeTriee = sorted(surface_appartements) #Méthode qui trie la liste
    if (tailleListe % 2 == 0) :
        Xmedian = (listeTriee[tailleListe//2-1] + listeTriee[tailleListe//2])/2
    else :
        Xmedian = listeTriee[(tailleListe//2)]
    indicateursX.append(Xmedian) #Ajout au tableau

    #Moyenne quadratique des x
    for i in range(len(surface_appartements)) :
        #Somme des Xi au carré
        sommeQuadraX = sommeQuadraX + surface_appartements[i]**2
    moyenneQuadraX = sommeQuadraX/len(surface_appartements)

    #Moyenne des x au carré
    moyenneXCarre = moyenneX**2

    #Variance de x
    varianceX = moyenneQuadraX-moyenneXCarre
    indicateursX.append(varianceX) #Ajout au tableau

    #Ecart type de x
    ecartTypeX = math.sqrt(varianceX) #math.sqrt permet le calcul de la racine carrée
    indicateursX.append(ecartTypeX) #Ajout au tableau


    #Calculs concernant les prix(valeur y) du jeu de données
    #Moyenne des y
    moyenneY = sum(prix_appartements)/len(prix_appartements)
    indicateursY.append(moyenneY)

    #Médiane des y
    tailleListeY = len(prix_appartements)   #Méthode qui donne la taille de la liste
    listeTrieeY = sorted(prix_appartements) #Méthode qui trie la liste
    if (tailleListeY % 2 == 0) :
        Ymedian = (listeTrieeY[tailleListeY//2-1] + listeTrieeY[tailleListeY//2])/2
    else :
        Ymedian = listeTrieeY[(tailleListeY//2)]
    indicateursY.append(Ymedian) #Ajout au tableau

    #Moyenne quadratique des y
    for i in range(len(prix_appartements)) :
        #Somme des Yi au carré
        sommeQuadraY = sommeQuadraY + prix_appartements[i]**2
    moyenneQuadraY = sommeQuadraY/len(prix_appartements)

    #Moyenne des y au carré
    moyenneYCarre = moyenneY**2

    #Variance de y
    varianceY = moyenneQuadraY-moyenneYCarre
    indicateursY.append(varianceY)

    #Ecart type de y
    ecartTypeY = math.sqrt(varianceY)
    indicateursY.append(ecartTypeY)

    #Autres calculs
    #Calcul de la moyenne de x * la moyenne de y
    produitMoyenne = moyenneX*moyenneY

    #Moyenne de x*y
    for i in range(len(surface_appartements)) :
        sommeAll = sommeAll + surface_appartements[i]*prix_appartements[i]
    moyenneXY = sommeAll/len(surface_appartements)

    #Covariance de (x,y)
    covarianceXY = moyenneXY-produitMoyenne
    indicateursXY.append(covarianceXY)

    return indicateursX, indicateursY, indicateursXY

try:
    surface_appartements, prix_appartements = lecture_fichier("..\donnees.txt")   
except ValueError as erreur: #Levée de l'exception si mauvais format du fichier
    print(erreur)
  
    
def algo1(indiX, indiY, indiXY) :

    #Calcul de a = covarianceXY/varianceX
    a = indiXY[0]/indiX[2]

    #Calcul de b = moyenneY-a*moyenneX
    b = indiY[0]-a*indiX[0]

    return a,b

def algo2(x) : #TODO
    a = 0
    b = 0
    return a,b


def estimationPrix(surface, a, b) :

    calcul = (a*surface+b)*1000
    #On multiplie par mille pour avoir le résultat en milliers

    print("\nPrix d'un appartement pour " + str(surface) + "m² : ")
    return print("{0:.2f}".format(calcul) + "€")


def affichageModele (a,b) :
    
    print("\nModèle d'estimation pour calculer le prix d'un appartement : ")
    #{0:.2f} sert à afficher 2 chiffres après la virgule
    print("y = {0:.2f}".format(a) + "x + {0:.2f}".format(b))


def affichageIndicateurs(indiX, indiY, indiXY) : #Prend en paramètre trois tableaux contenant les indicateurs
    
    print("\n* ---- Différents indicateurs concernant les données ---- *")
    print("Indicateurs concernant les surfaces :")
    print ("Moyenne : " + str(indiX[0]) + " mètres carrés.\nMédiane : " + str(indiX[1]) + " mètres carrés.\nVariance : "
           +  str(indiX[2]) + "\nEcartType : " + str(indiX[3]))
    
    print("\nIndicateurs concernant les prix :")
    print ("Moyenne : " + str(indiY[0]) + "€\nMédiane : "  + str(indiY[1]) + "€\nVariance : "
           + str(indiY[2]) + "\nEcartType : " + str(indiY[3]))
    
    print("\nAutres indicateurs :")
    print ("Covariance : " + str(indiXY[0]) + "\nCoefficient de corrélation linéaire : TODO ")

def entreeMenu() :

    testOK = False
    entree = 0
    
    print("*  -------------------------------------  MENU  --------------------------------------  *")
    print("*  Options disponibles :                                                                *")
    print("*                                                                                       *")
    print("*  1 - Affichage des indicateurs associés au jeu de données                             *")
    print("*  2 - Calcul du modèle par résolution analytique                                       *")
    print("*  3 - Calcul du modèle par descente de gradient                                        *")
    print("*  4 - Estimation du prix d'un appartement à partir d'un modèle                         *")
    print("*  5 - Quitter l'outil                                                                  *")
    print("*  -----------------------------------------------------------------------------------  *")
    
    while (entree == 0) : #Ne s'arrête que lorsqu'une valeur est entrée
        try:
            entree = int(input("\nSélectionnez une option (entre 1 et 5) : "))
            if 1 <= entree <= 5: #Vérifie que l'entrée respecte le format
                testOK = True
            else:
                raise ValueError()
        except ValueError :#Si l'entrée n'est pas un entier
            print("Erreur : vous n'avez pas entré un nombre entier compris entre 1 et 5.")

    return testOK, entree


#Programme principal
#Initialisation des variables
indicateursX = []  # Moyenne des x, 'médiane des x', variance de x, écartType de x
indicateursY = []  # Moyenne des y, 'médiane des y', variance de y, écartType de y
indicateursXY = [] # Covariance, 'coefficient de corrélation linéaire'
a = 0
b = 0
#Fin de l'initialisation

print("*  -----------------------------------------------------------------------------------  *")
print("*  Bienvenue dans l'outil d'aide à la détermination du prix de vente d'un appartement ! *")
print("*  -----------------------------------------------------------------------------------  *")

testOK, entree = entreeMenu()

while (testOK == True) :
    if (entree == 1) :
        indicateursX, indicateursY, indicateursXY = calculIndicateurs()
        affichageIndicateurs(indicateursX, indicateursY, indicateursXY)

        print("\n\n\n\n\n\n\n\n\n\n\n") #Espaces pour aérer l'affichage
        testOK, entree = entreeMenu()   #Permet de revenir au menu
        
    elif (entree == 2) :
        if (indicateursX == []) :
            indicateursX, indicateursY, indicateursXY = calculIndicateurs()
            
        a, b = algo1(indicateursX, indicateursY, indicateursXY)
        affichageModele(a, b)

        print("\n\n\n\n\n\n\n\n\n\n\n") #Espaces pour aérer l'affichage
        testOK, entree = entreeMenu()   #Permet de revenir au menu
        
    elif (entree == 3) :
        affichageModele(a, b)
        print("Méthode en cours d'implémentation, merci de votre compréhension !")

        print("\n\n\n\n\n\n\n\n\n\n\n") #Espaces pour aérer l'affichage
        testOK, entree = entreeMenu()   #Permet de revenir au menu

    elif (entree == 4) :
        if (indicateursX == [] or a == 0) :
            indicateursX, indicateursY, indicateursXY = calculIndicateurs()
            a, b = algo1(indicateursX, indicateursY, indicateursXY)

        entreeSurface = int(input("\nEntrez la surface de votre appartement (nombre entier): "))  
        estimationPrix(entreeSurface, a, b)

        print("\n\n\n\n\n\n\n\n\n\n\n") #Espaces pour aérer l'affichage
        testOK, entree = entreeMenu()   #Permet de revenir au menu
            
    else :
        print("Merci d'avoir utilisé notre outil !")
        testOK = False
