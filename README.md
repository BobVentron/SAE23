____________________________________________________________________________

> ██╗      █████╗      ██████╗ ██████╗ ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗
> ██║     ██╔══██╗    ██╔════╝██╔═══██╗██║████╗  ██║██╔════╝██║  ██║██╔════╝
> ██║     ███████║    ██║     ██║   ██║██║██╔██╗ ██║██║     ███████║█████╗  
> ██║     ██╔══██║    ██║     ██║   ██║██║██║╚██╗██║██║     ██╔══██║██╔══╝  
> ███████╗██║  ██║    ╚██████╗╚██████╔╝██║██║ ╚████║╚██████╗██║  ██║███████╗
> ╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝
____________________________________________________________________________


# Application pour un amateur de coinche stéphanoise pour conserver ses diverses parties de coinche.

> [!IMPORTANT]
> Pour le fichier .csv :
>   l'orde des tables dans ce fichier est important.
>   l'orde des tables est le suivant : 
>   TableJoueur; TablePartie; TableEquipe; TableDonne; TableAnnonce; TableEncheres


### Procédure de lancement de l'aplication WEB

Pour utiliser l'application il faut suivre différentes étapes:
Etape 1 : Démarer votre serveur de base de donées (phphmyadmin par exemple)
Etape 2 : Modifier le fichier config.txt avec les bonne information (notament le host, le user et le mot de passe de la base de donées)
Etape 3 : Ouvrir un terminal et ce placer dans le fichier 'Soleilhac_Bastien_SAE23_final'
```bash
    cd Soleilhac_Bastien_SAE23_final
```
Etape 4 (Facultatif) : Executer le fichier python de création de la base 
```bash
    python3 createBase.py
``` 
Etape 5 : Lancer l'appplication 
```bash
    python3 interfaceWeb.py
```

### L'état de l'aplication
## Partie administrateur 

Affichages de la liste des Joueurs
Affichages de la liste des Joueurs par orde alphabétique
Affichages des équipes
Affichages de la composition des équipes
Affichages des partie
Affichages du nombre de partie gagner par chaque joueur
Affichages des annonce que a eu un certaine joueur
Affichages des annonce qui ont eu lieu durant une certaine partie
Affichages de la liste des partie ou les joueur on annoncer faire plus de 162 points

Insertion posible dans chacune des 6 table (joueurs, partie, equipe, donne, encheres, annonces) contenue dans la base de données
Posibiliter de supprimer n'importe qu'elle élément de n'importe qu'elle table
Posibiliter de modifier tout les élément (sauf les id) de tout les tables

## Partie public

Cette page contient une liste de toutes les parties jouées, triées de la 
partie la plus récente (les parties qui sont en cours de jeu en premier) à la moins 
récente. Pour chaque partie, on peut lire le nom des deux équipes qui ont joué 
et qui a gagné (si la partie est finie). En cliquant sur une partie, nous pouvons 
avoir la composition des équipes. Et les informations sur chaque donne de la 
partie avec l’évolution des points suivant ces donnes. Les donnes sont rangées 
de la manière suivante : la première donne jouée sera en première et la dernière 
en dernier. Les informations correspondantes à chaque donne sont les 
suivantes : qui est partie et à quelle couleur , nous avons le résultat de la donne 
et le nombre de points qu'on gagner chaqu'une des équipes, 
mais aussi nous avons les annonces éventuelles de la donne. Il est aussi 
possible de créer une partie et de rajouter des donnes en direct. 
Pour créer une partie, il sufit juste de définir les deux équipes qui disputent
cette dernière et le lieu de la partie et la premier donne de cette dernier. Et
pour rajouter une donne, il va juste être nécessaire de rentrer les scores obtenus 
par chaque équipe .


# Il n'y a pas eu de modifications de la base depuis l’étape 2

### Les fonctionnalités prévues non réalisées
Tout les fonctionnalités ont été réalisées, il y a eu juste quelque petit 
modifications. Par exemple, pour inserer une donne dans la partie dynamique 
ont devait aussi ajouter le contrat correspondantes à la donne, finalement il
n'est pas nessesaire d'ajouter le contrat. Pour ajouter une partie pour la partie
dynamique il ne devait pas être nessesaire d'ajouter la premier donne alors que 
actuellement si. 

Il a été réalisées en plus l'Affichages des joueur par orde alphabétique

Soleilhac_Bastien_SAE23_final  
├── res  
│   ├── css  
│   │   ├── bootstrap.css                   # fichier de style pour bootstrap        
│   │   ├── index.css                       # Style pour le fichier index.html  
│   │   ├── insert_style.css                # Style pour les fichiers html d'insertion  
│   │   ├── partie_direct_style.css         # Style pour les fichier Partie_Direct.html  
│   │   └── style.css                       # Style general pour tout les Templates  
│   ├── font                                # Dossier contenant tout les policess  
│   │   ├── BroncoPersonalUse.ttf  
│   │   ├── Chunkfive Ex.ttf  
│   │   └── dejav-serif.ttf  
│   ├── images                              # Dossier contenant toutes les images  
│   │   ├── as.png  
│   │   ├── carreau.png       
│   │   ├── coeur.png  
│   │   ├── favicon.ico  
│   │   ├── main_carte.jpg  
│   │   ├── main_carte2.jpg  
│   │   ├── trefle.png  
│   │   └── trefle2.png  
│   ├── js                                  # Dossier contenant les fichier js pour le site  
│   │   ├── bootstrap.bundle.min.js         # fichier bootstrap pour l'accordéon pour la partie publiv  
│   │   ├── bootstrap.min.js                # fichier bootstrap pour le style de l'app  
│   │   ├── jquery-3.5.0.min.js             # Obligatoire avec bootstrap  
│   │   └── script.js                       # Différents script utiilser pas l'app Web  
│   ├── templates  
│   │   ├── aff_AnnonceJoueur.html          # Templates qui permet d'affichier les annonces d'un joueur sélectionner   
│   │   ├── aff_AnnoncePartie.html          # Templates qui permet d'affichier les annonces d'une partie sélectionner  
│   │   ├── aff_liste.html                  # Templates qui permet d'affichier différents Liste, contenue de certaine table  
│   │   ├── aff_texte.html                  # Templates qui permet différents texte  
│   │   ├── index.html                      # Templates de la page d'acceuil du site Web  
│   │   ├── Insert_Annonces.html            # Templates de la page qui permet d'insérer une annonce dans la base de donée  
│   │   ├── Insert_Donne.html               # Templates de la page qui permet d'insérer une donne dans la base de donées  
│   │   ├── Insert_Encheres.html            # Templates de la page qui permet d'insérer une encheres dans la base de donées  
│   │   ├── Insert_Equipe.html              # Templates de la page qui permet d'insérer une équipe dans la base de donées  
│   │   ├── Insert_Joueurs.html             # Templates de la page qui permet d'insérer un joueur dans la base de donées  
│   │   ├── Insert_Partie.html              # Templates de la page qui permet d'insérer une partie dans la base de donées  
│   │   ├── Modif_elem.html                 # Templates de la page qui permet de modifier un élément d'une table dans la base de donées  
│   │   ├── Partie_Direct.html              # Templates de la partie dynamique/public du site  
│   │   ├── Supp_elem.html                  # Templates de la page qui permet de supprimer un élément d'une table dans la base de donées  
│   │   └── template.html                   # Templates qui contient la base d'une page html, la navbar et le footer  
├── utils  
│   ├── BDcoincheUtils.py                   # Fichier contenant tout les fonction utile pour le site web  
│   ├── donneeCoinche.csv                   # fichier contenant des données permetant d'initialiser la base de donées   
│   ├── loadConfig.py                       # fichier qui contient des fonction critique pour l'aplication tel que le chargment de la config, l'execution des requetes  sql, la connection a la base de donées  
│   ├── mkRequest.py                        # Dans ce ficher tout ces fonction prennent plusieurs parametres, Et renvoie un string, Tout ces fonction permet d'inserer dans des requete sql des valeurs specifique.  
│   ├── Request.py                          # Ce fichier contient sous forme de 3  dictionnaire  les requetes nessesaire a l'appliquation pour : créer la base, inserer des elements, selection des elements  
├── config.txt                              # fichier contenant la configuration de l'aplication WEB  
├── createBase.py                           # Fichier permetant de créer la base de données et d'importer des valeurs dedans   
├── Dump.sql                                # fichier permetant de recréer la base de données, avec les données  
├── interfaceWeb.py                         # fichier principal qui permet l'execution de l'appliquation WEB  
└── README.txt
