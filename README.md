# Projet_App_flask

Ce projet consiste en la création d'une application flask, qui utlise des outils tel que MongoDB, scrapy, et docker compose 

# Descsription 

Aujourd’hui, de nombreux sites existent pour répertorier le données météorologique des différents spots de surf. Or étant moi même surfeur je me suis rendu compte que cela prenait beaucoup de temps d’analyser les nombreuses données pour chaque spots et chaque jours lorsque je recherche un endroit pour aller surfer.
Le but de cette application est de récolter les données des différents spots de surf en France sur le site "https://www.surf-report.com/" à l’aide scrappy, une fois c’est données stockées l’affichage se fait via une application web en utilisant le framework Flask. Mongodb a été utilisé pour créer la base de données et permettre les requêtes.
Afin d’analyser via des graphiques les conditions météorologiques moyennes des différents spots Dash a été utilisé .
Enfin Docker a permis la virtualisation d’un serveur pour la base de donnée mongo.


# Lancement du programme 

1) Lancer dans un premier temps docker :

docker-compose up 


2) Executer le script pyhton :

App_web.py

3) Se rendre à l'adresse indiquée par le terminal 


# Résultat 
![Test Image 5](https://github.com/AntoineMOREAU1/Mosaique-image-python-Projet-2017/blob/main/img_read_me/Affichage_des_spots.png)
![Test Image 6](https://github.com/AntoineMOREAU1/Mosaique-image-python-Projet-2017/blob/main/Photo-Final/aurelie28.jpg)

![Test Image 1](https://github.com/AntoineMOREAU1/Mosaique-image-python-Projet-2017/blob/main/Photo-OG/avengers.jpg)
![Test Image 2](https://github.com/AntoineMOREAU1/Mosaique-image-python-Projet-2017/blob/main/Photo-Final/avangersfinal.jpg)




