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


### Utilisation :

Pour utiliser l'application il faut suivre différentes étapes:
Etape 1 : Démarer votre serveur de base de donées (phphmyadmin par exemple)
Etape 2 : Modifier le fichier config.txt avec les bonne information (notament le host, le user et le mot de passe de la base de donées)
Etape 3 : Ouvrir un terminal et ce placer dans le fichier 'Soleilhac_Bastien_SAE23_liv1'
```bash
    cd Soleilhac_Bastien_SAE23_liv1
```
Etape 4 (Facultatif) : Executer le fichier python de création de la base 
```bash
    python3 createBase.py
``` 
Etape 5 : Lancer l'appplication 
```bash
    python3 interfaceCLI.py
```


### Les fonctionnalités : 

L'application propose les fonctionnalités suivantes :
    -Afficher les joueurs
    -Afficher les joueurs dans l'ordre alphabétique
    -Afficher les équipes
    -Afficher la composition des équipes
    -Afficher la liste des parties
    -Afficher le nombre de parties gagnées par chaque joueur
    -Afficher toutes les annonces pour un certain joueur
    -Afficher toutes les annonces pour une certaine partie
    -Afficher les parties avec des annonces supérieures à 162   
    -Exécuter une commande SQL
    -Supprimer un élément d'une table
    -Insérer un élément dans une table
    -Modifier un élément d'une table



bleme avec carreau et careau