import pymysql
import csv
import time
from utils.Request import _requetesCreateDatabase
from utils.mkRequest import mkDropRequest, mkCreateBaseRequest, mkUseRequest, mkCountAttributsRequest
from utils.loadConfig import _dbConfig, majParamsConnexion, execute, progress_bar
from utils.BDCoincheUtils import doInsertAnnonce, doInsertDonne, doInsertEncheres, doInsertEquipe, doInsertJoueur, doInsertPartie

def initBase() -> None :
    "Procédure gérant la créaation de la base de données"
    majParamsConnexion() #Mise a jour des paramètre depuis le fichier config.txt
    match _dbConfig['driver'].upper() :
        case "MYSQL" :
            createBaseMYSQL() #creation de la base de données
            loadFromCSVFile(_dbConfig['path']) #importation de la base de donées
        case _ :
            print (f"SGBDR {_dbConfig['driver'].upper()} non géré")

def createBaseMYSQL() -> None:
    "Cette procédure permet la création de la base de donées"
    progres = 1
    db = pymysql.connect(host=_dbConfig['host'], user=_dbConfig['user'], passwd=_dbConfig['passwd'], port=int(_dbConfig['port']))#Connection au serveur de base de donées
    cursor = db.cursor() 
    
    total_tables = len([key for key in _requetesCreateDatabase.keys() if key.startswith("createTable")]) #Nessésaire pour le barre de chargement
    
    #execution des requetes de création de la base de donées 
    for requete in _requetesCreateDatabase.keys():
        if requete == "drop": cursor.execute(mkDropRequest(_dbConfig['db'])) #execution de la requete drop
        elif requete == "createBase": 
            cursor.execute(mkCreateBaseRequest(_dbConfig['db'])) #execution de la requete pour créer la base
            progress_bar(progres, total_tables+2, " La base de données a été créée avec succès.") #update de la barre de chargement
            progres += 1
        elif requete == "use": cursor.execute(mkUseRequest(_dbConfig['db'])) #execution de la requête pour ce servir de la base nouvelement créer
        elif requete =="countAttributs" or requete =="show" or requete=="delete" or requete=="update": pass #on echape ces requete car elle ne doivent par être executer ici
        else:
            #Execution des requetes de créatio ndes tables
            cursor.execute(_requetesCreateDatabase[requete])
            if requete.startswith("createTable"):
                table_name = requete[11:]
                progress_bar(progres, total_tables+2, f" La table {table_name} a été créée avec succès.") #update de la barre de chargement
                progres += 1
        time.sleep(0.25)

    
def loadFromCSVFile(path : str) -> None:
    """
    Procédure qui prend un parametre le chemin vers le fichier csv ou ce situe des les données à entrer dans la base.
    Cette procédure permet d'injecter un jeu de donées
    """
    with open(path, newline='\n',encoding='utf-8') as csvFile : #Ouverture du fichier csv
        lignes = csv.reader(csvFile,delimiter=',')
        TableAModif = ""
        nbAttributsTable = 0
        for elem in lignes : #Parcours des différentes lignes
            if len(elem) == 0 or elem[0][0] == "#" : continue #Si la ligne ne contien rien ou commence par un # on l'échape
            elif "[" in elem[0] and "]" in elem[0]: # si dans la ligne il y a les element [ et ] on récupere le nom de la table 
                TableAModif = (elem[0][6:-1]).lower() #Récuperation du nom de la table
                nbAttributsTable = (execute(mkCountAttributsRequest(_dbConfig['db'], TableAModif)))[0][0] - 1 #Recuperation du nombre d'attributs de la table
            elif len(elem) == nbAttributsTable : #vérification que la longeur de l'élément est bien égale au nombre d'attribut correspondant à la table
                #Insertion dans la bonne table des éléments 
                match TableAModif: 
                    case "annonce": doInsertAnnonce(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7]); 
                    case "donne": doInsertDonne(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5])
                    case "encheres": doInsertEncheres(elem[0], elem[1], elem[2], elem[3])
                    case "equipe": doInsertEquipe(elem[0], elem[1], elem[2], elem[3])
                    case "joueur" : doInsertJoueur(elem[0], elem[1], elem[2])
                    case "partie": doInsertPartie(elem[0], elem[1], elem[2])
        progress_bar(9, 9, " Les données ont été importer dans la base de données\n "), time.sleep(1.45) #Progression de la barre de chargement
        

if __name__ == '__main__':
    "Execution du script de création de la base lors de l'execution de ce fichier"
    try : 
        print("\033[92m___________________________________________________________________________\n\n██╗      █████╗      ██████╗ ██████╗ ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗\n██║     ██╔══██╗    ██╔════╝██╔═══██╗██║████╗  ██║██╔════╝██║  ██║██╔════╝\n██║     ███████║    ██║     ██║   ██║██║██╔██╗ ██║██║     ███████║█████╗  \n██║     ██╔══██║    ██║     ██║   ██║██║██║╚██╗██║██║     ██╔══██║██╔══╝  \n███████╗██║  ██║    ╚██████╗╚██████╔╝██║██║ ╚████║╚██████╗██║  ██║███████╗\n╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝\n___________________________________________________________________________\n\033[0m")
        initBase() # appelle de la procédure qui permet de créer la base
        print("\033[92m___________________________________________________________________________\033[0m\n")
        print('\033[92m########  ##    ## ########    #### \n##     ##  ##  ##  ##          #### \n##     ##   ####   ##          #### \n########     ##    ######       ##  \n##     ##    ##    ##               \n##     ##    ##    ##          #### \n########     ##    ########    ####\033[0m')
    except pymysql.err.OperationalError as e: #Erreur si il est imposible de ce connecter au serveur de base ce données
        print(f"\033[91mErreur : Imposible de ce connecter a la base de données. Vérifier le fichier de configuration et vérifier que phpmyadmin est bien lancée\033[0m {e}")
        print("\033[92m___________________________________________________________________________\033[0m\n")
        print('\033[92m########  ##    ## ########    #### \n##     ##  ##  ##  ##          #### \n##     ##   ####   ##          #### \n########     ##    ######       ##  \n##     ##    ##    ##               \n##     ##    ##    ##          #### \n########     ##    ########    ####\033[0m')
    except KeyboardInterrupt : #Erreur qui permet une fermeture plus "propre" quand l'utilisateur fait CTRL+C
        print("\n\033[92m___________________________________________________________________________\033[0m\n")
        print('\033[92m########  ##    ## ########    #### \n##     ##  ##  ##  ##          #### \n##     ##   ####   ##          #### \n########     ##    ######       ##  \n##     ##    ##    ##               \n##     ##    ##    ##          #### \n########     ##    ########    ####\033[0m')