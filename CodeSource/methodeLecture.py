def lecture_fichier(fichier_path):
    #Méthode permettant la lecture et l'analyse du fichier de donnes
    surface_appartements = [] #Tableau pour stocker les surfaces en mètres carrés
    prix_appartements = []    #Tableau pour stocker les prix en milliers d'€
   
    with open(fichier_path, 'r') as fichier:
   
        for ligne in fichier:
            ligne = ligne.strip() #Suppression du retour à la ligne
            chaine = ligne.split('\t') #Suppression de la tabulation
           
            if len(chaine) != 2: #Si la chaine contient plus de deux "mots" cela retourne une erreur
                raise ValueError("Le fichier ne respecte pas le format attendu.")
               
            surface_appartements.append(float(chaine[0])) #Ajout de la surface au tableau
            prix_appartements.append(float(chaine[1]))    #Ajout du prix au tableau
           
    return surface_appartements, prix_appartements


