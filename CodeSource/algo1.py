from methodeLecture import lecture_fichier

def algo() :
    #Initialisation de sommeAll qui permet de calculer la somme des x et y
    sommeAll = 0
    #Initialisation de sommeQuadra qui sert à faire la somme des x au carré
    sommeQuadra = 0

    #Calcul de la moyenne du jeu de données (valeur x)
    moyenneX = sum(surface_appartements)/len(surface_appartements)

    #Calcul de la moyenne du jeu de données (valeur y)
    moyenneY = sum(prix_appartements)/len(prix_appartements)

    #Calcul de la moyenne de x * la moyenne de y
    produitMoyenne = moyenneX*moyenneY

    #Moyenne de x*y
    for i in range(len(surface_appartements)) :
        sommeAll = sommeAll + surface_appartements[i]*prix_appartements[i]
    moyenneXY = sommeAll/len(surface_appartements)

    #Covariance de (x,y)
    covarianceXY = moyenneXY-produitMoyenne

    #Calcul de la moyenne quadratique
    for i in range(len(surface_appartements)) :
        #Somme des Xi au carré
        sommeQuadra = sommeQuadra + surface_appartements[i]**2
    moyenneQuadra = sommeQuadra/len(surface_appartements)

    #Calcul de la moyenne au carré
    moyenneXCarre = moyenneX**2

    #Calcul de la variance de x
    varianceX = moyenneQuadra-moyenneXCarre

    #Calcul de a
    a = covarianceXY/varianceX

    #Calcul de b
    b = moyenneY-a*moyenneX

    print("\nModèle d'estimation pour calculer le prix d'un appartement : ")
    #{0:.2f} sert à afficher 2 chiffres après la virgule
    print("y = {0:.2f}".format(a) + "x + {0:.2f}".format(b))

try:
    surface_appartements, prix_appartements = lecture_fichier("..\donnees.txt")   
except ValueError as erreur: #Levée de l'exception si mauvais format du fichier
    print(erreur)
algo()