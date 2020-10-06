import os
#nous devrions vérifier si le fichier existe ou non avant de le supprimer.
if os.path.exists('spots.csv'):
    os.remove('spots.csv')
   