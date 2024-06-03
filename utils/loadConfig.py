import pymysql
import sys

_dbConfig = { #configuration de base 
    'driver' : "MySQL",
    'host' : "localhost",
    'user' : "admin",
    'passwd' : "admin",
    'port' : 3306,     # port MySQL standard (par défaut)
    'db' : "soleilhac_sae",
    'path' : "./utils/donneeCoinche.csv"
}

def majParamsConnexion() -> None:
    "Procédure qui permet de mettre a jour les élément de connection grâce au fichier config.txt"
    try :
        with open("config.txt") as f : #Ouvre le fichier config.txt
            for ligne in f : #Parcours du fichier 
                if ligne[0] == '#' or ligne[0] == '[' or len(ligne)<3 : continue #On echape les elements qui commence par # ou [ 
                champs = ligne.split(':')
                _dbConfig[champs[0].strip()] = champs[1].strip().strip('"')#Mise a jour de la configuration 
    except FileNotFoundError as e : print("'config.txt' absent, utilisation des valeurs par défaut")#renvoie une erreur si il y a un probleme avec l'ouvertur du fichier txt

def dbConnect() -> tuple:
    """
    Fonction qui renvoie un tuple 
    Cette fonction permet de ce connecter a la base de données 
    et renvoie les élément utils a l'éxécution des requetes
    """
    majParamsConnexion()
    db = pymysql.connect(host = _dbConfig['host'], user=_dbConfig['user'], passwd=_dbConfig['passwd'], port=int(_dbConfig['port']), db = _dbConfig['db'])
    return (db,db.cursor())

def execute(req : str) :
    """
    Fonction qui prend en parametre un requete sous la forme d'une string. 
    Cette fonction permet d'executer des requetes sql. 
    Elle renvoie le resultat des requetes SELECT
    ou elle renvoie le resultat des autres requetes sans oublier de les commits 
    """
    try : 
        _dbEtudiant, _cursorEtudiant = dbConnect()
        res = _cursorEtudiant.execute(req)
        if "select" in req or "SELECT" in req: res = _cursorEtudiant.fetchall()
        else : _dbEtudiant.commit()
        return res
    except Exception as e : 
        if "1064" in str(e) : 
            print("\033[91m Erreur: vous avez saisi une mauvaise valeur \033[0m")

def progress_bar(iteration, total, text, bar_length=50):
    """
    Fonction qui permet la creation de barre de chargemant personaliser.
    """
    percent = int((iteration / total) * 100)
    arrow = '=' * int((percent / 100.0) * bar_length - 1)
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write('\rProgress: [%s%s] %d%%' % (arrow, spaces, percent) +text)
    sys.stdout.flush()