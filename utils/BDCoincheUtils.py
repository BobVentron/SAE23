import datetime
from utils.loadConfig import execute
from utils.Request import _requetesSelectDatabase
from utils.mkRequest import (mkSelect, mkDelete, mkInsertAnnonceRequest, mkInsertDonneRequest, mkInsertEncheresRequest,
                              mkInsertEquipeRequest, mkInsertJoueurRequest, mkInsertPartieRequest, mkselectAnnonceJoueur, 
                              mkselectAnnoncePartie, mkupdate, mkselectDonnePartie, mkselectPartieID, mkselectCompoDonne)

def joueurToString(joueur: tuple) -> str: return f"Joueur n°{joueur[0]}, qui s'appelle {joueur[2]} {joueur[1]} et qui est née le {convert_date(joueur[3])}" #Fonction qui prend un entrée un tuple de joueur et qui renvoie les element du tuple sous forme d'une jolie phrase

def equipeToString(equipe: tuple) -> str: return f"Equipe n°{equipe[0]}, qui a pour nom {equipe[1]} et pour description: {equipe[2]}, cette équipe est composé des joueurs d'id {equipe[3]} et {equipe[4]}"#Fonction qui prend un entrée un tuple d'equipe et qui renvoie les element du tuple sous forme d'une jolie phrase

def compoToString(compo: tuple) -> str: return f"Equipe n°{compo[0]}, qui a pour nom {compo[1]} est composé du joueur {compo[2]} et du joueur {compo[3]}"#Fonction qui prend un entrée un tuple de la composition des equipes et qui renvoie les element du tuple sous forme d'une jolie phrase

def partieToString(partie: tuple) -> str: return f"Partie n°{partie[0]}, a eu lieu le {convert_date(partie[1])} au {partie[3]} et a commencer à {str(convertirTimeToSTR(partie[2]))}"#Fonction qui prend un entrée un tuple des parties et qui renvoie les element du tuple sous forme d'une jolie phrase

def getListe(requete) -> list: return[t for t in execute(_requetesSelectDatabase[requete])] #fooction qui prend en entrée le nom d'une requete et qui renvoie le contenu de l'execution de cette requete sous la forme d'une liste

def getmkliste(table) -> list: return[t for t in execute(mkSelect(table))] #fonction qui prend en entrée le nom d'une table et qui renvoei sous la fomre d'une liste les elements de cette table

def nbPartiegagner(nbPartie : tuple) -> str : return f"Le joueur {nbPartie[0]} a gagné {nbPartie[1]} partie.<br>" #fonction qui prend en entrer un tuple et qui renvoie une jolie phrase sur le nombre de partie gagner par un joueur
   
def AnnonceJoueur(idJoueur: int) -> str : 
    """
    Cette fonction prend en parametre l'id d'un joueur sous former d'un int.
    et renvoie un texte sous fourme d'un str,
    Cette fonction permet de créer un texte qui résume les anonces que a eu un certain joueur
    """
    text = "Ce joueur a eu comme annonce :"
    try:
        for annonce in execute(mkselectAnnonceJoueur(idJoueur)) : #Recuperation de tout les annonces du joueur grâce a son id 
            #Creation des phrase par rapport au annonce que le joueur a eu
            if annonce[6] == 1 : text = text + f"<br> Une belote durant la partie n°{annonce[15]} (pendant la donne d'id : {annonce[8]})"
            if annonce[5] != "0" : text = text + f"<br> {annonce[5]} tierce(s) durant la partie n°{annonce[15]} (pendant la donne d'id : {annonce[8]})"
            if annonce[4] == "1" : text = text + f"<br> {annonce[4]} cinquante durant la partie n°{annonce[15]} (pendant la donne d'id : {annonce[8]})"
            if annonce[3] == 1 : text = text + f"<br> Un 100 durant la partie n°{annonce[15]} (pendant la donne d'id : {annonce[8]})"
            if annonce[2] != "" and annonce[2] != "null" : text = text + f"<br> un carré de {annonce[2]} durant la partie n°{annonce[15]} (pendant la donne d'id : {annonce[8]})"
            if annonce[1] != "" and annonce[1] != "null": text = text + f"<br> un carré de {annonce[1]} durant la partie n°{annonce[15]} (pendant la donne d'id : {annonce[8]})"
        if text == "<br> Ce joueur a eu comme annonce :": text = "<br>Ce joueur n'a jamais eu d'annonce." #Si le joueur n'a pas eu d'annonce on renvoie cette phrase
        return text
    except TypeError as e :
        print("\033[91m Erreur: vous avez saisi une mauvaise valeur \033[0m")


def AnnoncePartie(idPartie: int) -> str : 
    """
    Cette fonction prend en parametre l'id d'une partie sous former d'un int.
    et renvoie un texte sous fourme d'un str,
    Cette fonction permet de créer un texte qui résume les anonces qu'il y a eu pendant une certain partie
    """
    text = "Durant cette partie il y a eu comme annonce : "
    try :
        for annonce in execute(mkselectAnnoncePartie(idPartie)): #Recuperation de tout les annonces du partie grace a l'id de cette dernier
            #Creation des phrase par rapport au annonce que de la partie
            if annonce[6] == 1 : text = text + f'<div class="list-group-item rounded">une belote (pendant la donne d\'id : {annonce[8]})</div>'
            if annonce[5] != "0" : text = text + f'<div class="list-group-item rounded">{annonce[5]} tierce(s) durant la partie (pendant la donne d\'id : {annonce[8]})</div>'
            if annonce[4] == "1" : text = text + f'<div class="list-group-item rounded">{annonce[4]} cinquante durant la partie  (pendant la donne d\'id : {annonce[8]})</div>'
            if annonce[3] == 1 : text = text +f'<div class="list-group-item rounded">Un 100 durant la partie  (pendant la donne d\'id : {annonce[8]})</div>'
            if annonce[2] != "" and annonce[2] != "null": text = text + f'<div class="list-group-item rounded">un carré de {annonce[2]} durant la partie (pendant la donne d\'id : {annonce[8]})</div>'
            if annonce[1] != "" and annonce[1] != "null": text = text + f'<div class="list-group-item rounded">un carré de {annonce[1]} durant la partie (pendant la donne d\'id : {annonce[8]})</div>'
        if text == "Durant cette partie il y a eu comme annonce : ": text = f'<div class="list-group-item rounded">il n\'y a jamais eu d\'annonce dans cette partie.</div>'#Si dans une partie il y a pas d'annonce on renvoie cette phrase
        return text
    except TypeError as e :
        print("\033[91m Erreur: vous avez saisi une mauvaise valeur \033[0m")

def donne162(elem: tuple)->str : return f"L'équipe {elem[0]} a dit une annonce supérieur a 162 durant la partie n°{elem[2]} (pandant la donne d'id : {elem[1]})"#Fonction qui prend en entrée un tuple et qui renvoie un phrase phrase sous forme d'une str 

def convertirTimeToSTR(delta: datetime.timedelta) -> str: return f"{delta.seconds // 3600}h{(delta.seconds % 3600) // 60}min{delta.seconds % 60}s" #Fonction qui prend en entrée une heure au format datetime.timedelta et qui renvoie en str cette heure formater de la maniere suivante 17h18min4s

def convertirDate(date: str)->str:
    """
    Fonction qui prend en entrée une date en str de la forme jour/mois/annee
    et qui renvoie cette même date sous la forme annee-mois-jour
    """
    if "-" in str(date) : text = date
    else :
        jour, mois, annee = (str(date)).split('/')
        if len(mois) == 1: mois = '0' + mois
        if len(jour) == 1: jour = '0' + jour
        text = f"{annee}-{mois}-{jour}"
    return text

def convert_date(date):
    """
    Fonction qui prend en entrée une date en str de la forme annee-mois-jour
    et qui renvoie cette même date sous la forme jour/mois/annee
    """
    if "/" in str(date) : text = date
    else :
        year, month, day = (str(date)).split('-')
        text = f"{day}/{month}/{year}"
    return text

def afichTable(table: int ) -> list: 
    """
    Fonction qui prend en entrée le numéro du table sous le forme d'un entier 
    et qui renvoie cette table (avec un formatage spécial si possible) sous la former d'un str
    """
    if table == 4: 
        text = []
        for e in getmkliste("equipe"):
            nombre = ""
            chaine = str((equipeToString(e))[:20])
            inverse = reversed(chaine)
            for caractere in reversed("".join(inverse)):
                if caractere.isdigit(): nombre = str(caractere) + str(nombre)
                elif caractere == ',': break
            text.append([nombre, equipeToString(e)])
    elif table == 5 : 
        text = []
        for e in getmkliste("joueur"):
            nombre = ""
            chaine = str((joueurToString(e))[:20])
            inverse = reversed(chaine)
            for caractere in reversed("".join(inverse)):
                if caractere.isdigit(): nombre = str(caractere) + str(nombre)
                elif caractere == ',': break
            text.append([nombre, joueurToString(e)])
    elif table == 6 :
        text = []
        for e in getListe("selectPartie"):
            nombre = ""
            chaine = str((partieToString(e))[:20])
            inverse = reversed(chaine)
            for caractere in reversed("".join(inverse)):
                if caractere.isdigit(): nombre = str(caractere) + str(nombre)
                elif caractere == ',': break
            text.append([nombre, partieToString(e)])
    else : 
        donnee = execute(mkSelect(['Annonce', 'Donne', 'Encheres', 'Equipe', 'Joueur', 'Partie'][table-1]))
        text = []
        for e in donnee:
            text.append([e[0], e])

    return text

def suprID(table: int, id : int) -> None : execute(mkDelete(['Annonce', 'Donne', 'Encheres', 'Equipe', 'Joueur', 'Partie'][table-1], id)) #Procedure  qui prend en entrée l'id d'une table et l'id de la ligne a supprimer et qui le supprime

def doInsertJoueur(nom, prenom, date_naissance)-> None : execute(mkInsertJoueurRequest(nom, prenom, convertirDate(date_naissance)))#Procedure qui permet d'inserer un joueur dans la table joueur

def doInsertPartie(date, heure_debut, adresse)-> None : execute(mkInsertPartieRequest(convertirDate(date), heure_debut, adresse))#Procedure qui permet d'inserer une partie dans la table partie

def doInsertEquipe(nom, description, id_joueur1, id_joueur2)-> None : execute(mkInsertEquipeRequest(nom, description, id_joueur1, id_joueur2))#Procedure qui permet d'inserer une equipe dans la table equipe

def doInsertDonne(point_equipe1, point_equipe2, win_enchere, id_equipe1, id_equipe2, id_partie)-> None : execute(mkInsertDonneRequest(point_equipe1, point_equipe2, win_enchere, id_equipe1, id_equipe2, id_partie))#Procedure qui permet d'inserer une donne dans la table donne

def doInsertAnnonce(carre1, carre2, _100 , nb50, nbTierce, belote, id_joueur, id_donne)-> None : execute(mkInsertAnnonceRequest(carre1, carre2, _100 , nb50, nbTierce, belote, id_joueur, id_donne))#Procedure qui permet d'inserer une annonce dans la table annonce

def doInsertEncheres(couleur, hauteur, numero, id_donne)-> None : execute(mkInsertEncheresRequest(couleur, hauteur, numero, id_donne))#Procedure qui permet d'inserer une enchere dans la table encheres

def doUpdate(table, attribut, valeur, idModif)-> None : execute(mkupdate(table, attribut, valeur, idModif))#procedure qui permet de modifier un valeur dans une certain table

def doselectDonnePartie(id): return execute(mkselectDonnePartie(id))#Procedure qui permet de récuper tout les donne d'une certain partie

def doselectPartieID(date, heureDebut, Adresse): return execute(mkselectPartieID(date, heureDebut, Adresse))#Procedure qui permet de récupérer l'id d'une partie grace a la date de cette  dernier, a l'heur du début et à sont adderese

def doselectCompoDonne(idDonne) : return execute(mkselectCompoDonne(idDonne))#Procedure qui permet de récuperer les composition des équipe s'affrontant dans une certaine partie