def lecture_fichier(fichier_path):
    surface_appartements = []
    prix_appartements = []
   
    with open(fichier_path, 'r') as fichier:
   
        for ligne in fichier:
            ligne = ligne.strip()
            chaine = ligne.split('\t')
           
            if len(chaine) != 2:
                raise ValueError("Le fichier ne respecte pas le format")
               
            surface_appartements.append(float(chaine[0]))
            prix_appartements.append(float(chaine[1]))
           
    return surface_appartements, prix_appartements

try:
    surface_appartements, prix_appartements = lecture_fichier('../donnees.txt')
    print(surface_appartements)
    print(prix_appartements)
   
except ValueError as erreur:
    print(erreur)
