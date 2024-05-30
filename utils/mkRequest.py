"""
Dans ce ficher tout ces fonction prennent plusieurs parametres
Et renvoie un string
Tout ces fonction permet d'inserer dans des requete sql des valeurs specifique.
"""

from utils.Request import _requetesCreateDatabase, _requetesInsertDatabase, _requetesSelectDatabase

def mkDropRequest(baseName) -> str: return _requetesCreateDatabase["drop"].format(baseName)

def mkCreateBaseRequest(baseName) -> str: return _requetesCreateDatabase["createBase"].format(baseName)

def mkUseRequest(baseName) -> str: return _requetesCreateDatabase["use"].format(baseName)

def mkCountAttributsRequest(baseName, tableName) -> str: return _requetesCreateDatabase["countAttributs"].format(baseName, tableName)

def mkInsertJoueurRequest(nom, prenom, date_naissance) -> str: return _requetesInsertDatabase["insertJoueur"].format(nom, prenom, date_naissance)

def mkInsertPartieRequest(date, heure_debut, adresse) -> str: return _requetesInsertDatabase["insertPartie"].format(date, heure_debut, adresse)

def mkInsertEquipeRequest(nom, description, id_joueur1, id_joueur2) -> str: return _requetesInsertDatabase["insertEquipe"].format(nom, description, id_joueur1, id_joueur2)

def mkInsertDonneRequest(point_equipe1, point_equipe2, win_enchere, id_equipe1, id_equipe2, id_partie) -> str: return _requetesInsertDatabase["insertDonne"].format(point_equipe1, point_equipe2, win_enchere, id_equipe1, id_equipe2, id_partie)

def mkInsertAnnonceRequest(carre1, carre2, _100 , nb50, nbTierce, belote, id_joueur, id_donne) -> str: return _requetesInsertDatabase["insertAnnonce"].format(carre1, carre2, _100, nb50, nbTierce, belote, id_joueur, id_donne)

def mkInsertEncheresRequest(couleur, hauteur, numero, id_donne) -> str: return _requetesInsertDatabase["insertEncheres"].format(couleur, hauteur, numero, id_donne)

def mkSelect(table) -> str: return _requetesSelectDatabase["select"].format(table)

def mkDelete(table, idSupr) -> str: return _requetesCreateDatabase["delete"].format(table.lower(), table, idSupr)

def mkselectAnnonceJoueur(idjoueur: int) -> str: return _requetesSelectDatabase["selectAnnonceJoueur"].format(idjoueur)

def mkselectAnnoncePartie(idPartie: int) -> str: return _requetesSelectDatabase["selectAnnoncePartie"].format(idPartie)

def mkupdate(table, attribut, valeur, idModif) -> str: return _requetesCreateDatabase["update"].format(table, attribut, valeur, table.capitalize(), idModif)

def mkselectDonnePartie(id) -> str: return _requetesSelectDatabase["selectDonnePartie"].format(id)

def mkselectPartieID(date, heureDebut, Adresse) -> str : return _requetesSelectDatabase["selectPartieID"].format(date, heureDebut, Adresse)

def mkselectCompoDonne(idDonne) -> str : return _requetesSelectDatabase["selectCompoDonne"].format(idDonne)