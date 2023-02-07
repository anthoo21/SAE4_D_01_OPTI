
tabsurface = [32,48,60,157,76,90]
tabprix = [69.5,299,146,471.6,66,190]

def algo() :
    compteurX = 0
    compteurY = 0
    sommeAll = 0
    sommeQuadra = 0
    print("Calcul de la moyenne du jeu de données (valeur x) : ")
    for element in tabsurface :
        compteurX = compteurX + 1
    moyenneX = sum(tabsurface)/compteurX
    print(moyenneX)
    print("Calcul de la moyenne du jeu de données (valeur y) : ")
    for element in tabprix :
        compteurY = compteurY + 1
    moyenneY = sum(tabprix)/compteurY
    print(moyenneY)
    produitMoyenne = moyenneX*moyenneY
    print("Moyenne de x * moyenne de y : \n" + str(produitMoyenne))
    print("Moyenne de x*y : ")
    for i in range(len(tabsurface)) :
        sommeAll = sommeAll + tabsurface[i]*tabprix[i]
    moyenneXY = sommeAll/compteurX
    print(moyenneXY)
    print("Covariance de (x,y) : ")
    covarianceXY = moyenneXY-produitMoyenne
    print(covarianceXY)
    print("\n")
    print("Calcul de la moyenne quadratique : ")
    for i in range(len(tabsurface)) :
        sommeQuadra = sommeQuadra + tabsurface[i]**2
    moyenneQuadra = sommeQuadra/compteurX
    print(moyenneQuadra)
    print("Calcul de la moyenne au carré : ")
    moyenneXCarre = moyenneX**2
    print(moyenneXCarre)
    print("Calcul de la variance de x : ")
    varianceX = moyenneQuadra-moyenneXCarre
    print(varianceX)
    print("\n\n")
    print("Calcul de a : ")
    a = covarianceXY/varianceX
    print(a)
    print("Calcul de b : ")
    b = moyenneY-a*moyenneX
    print(b)
    print("\nModèle d'estimation pour calculer le prix d'un appartement : ")
    print("y = {0:.2f}".format(a) + "x + {0:.2f}".format(b))

algo()