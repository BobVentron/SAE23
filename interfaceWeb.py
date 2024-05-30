import cherrypy, os, os.path

from mako.template import Template
from mako.lookup import TemplateLookup
from utils.BDCoincheUtils import (getmkliste, joueurToString, getListe, equipeToString, compoToString, partieToString,
                                  nbPartiegagner, donne162, AnnonceJoueur, AnnoncePartie, doInsertAnnonce,
                                  doInsertDonne, doInsertEncheres, doInsertJoueur, doInsertEquipe, doInsertPartie,
                                  afichTable, suprID, doUpdate, doselectDonnePartie, doselectPartieID,
                                  doselectCompoDonne)

from utils.loadConfig import dbConnect

# Configuration du moteur de templates Mako
mylookup = TemplateLookup(directories=['res/templates'], input_encoding='utf-8', module_directory='res/tmp/mako_modules')

class InterfaceWeb(object):    
#######################################################################################
#                        Page d'accueil                                               #
####################################################################################### 
    @cherrypy.expose
    def index(self):
        """Page d'accueil."""
        mytemplate = mylookup.get_template("index.html")
        return mytemplate.render()

    @cherrypy.expose
    def affJoueur(self):
        """Afficher la liste des joueurs."""
        mytemplate = mylookup.get_template("aff_liste.html")
        return mytemplate.render(liste=[joueurToString(e) for e in getmkliste("joueur")], elem="joueurs")

    @cherrypy.expose
    def affJoueuralpha(self):
        """Afficher la liste des joueurs triés par ordre alphabétique."""
        mytemplate = mylookup.get_template("aff_liste.html")
        return mytemplate.render(liste=[joueurToString(e) for e in getListe("selectJoueurOrdre")], elem="joueurs trier par ordre alphabétique")
    
    @cherrypy.expose
    def affEquipe(self):
        """Afficher la liste des équipes."""
        mytemplate = mylookup.get_template("aff_liste.html")
        return mytemplate.render(liste=[equipeToString(e) for e in getmkliste("equipe")], elem="équipes")
    
    @cherrypy.expose
    def affCompo(self):
        """Afficher la liste des membres de chaque équipe."""
        mytemplate = mylookup.get_template("aff_liste.html")
        return mytemplate.render(liste=[compoToString(e) for e in getListe("selectCompo")], elem="membres de chaque équipe")
    
    @cherrypy.expose
    def affpartie(self):
        """Afficher la liste des parties."""
        mytemplate = mylookup.get_template("aff_liste.html")
        return mytemplate.render(liste= [partieToString(e) for e in getListe("selectPartie")], elem=" parties")
    
    @cherrypy.expose
    def affpartieGagner(self):
        """Afficher le nombre de parties gagnées par chaque joueur."""
        mytemplate = mylookup.get_template("aff_texte.html")
        text= ""
        for e in getListe("selectNbPartieWin"): 
            text = text + f'<div class="list-group-item rounded">{nbPartiegagner(e)}</div>' #Création d'un affiche spécial pour chauqe ligne 
        for e in getmkliste("joueur"): 
            if e[1] not in text or e[2] not in text: 
                text = text+ f'<div class="list-group-item rounded">Le joueur {e[2]} {e[1]} a gagné 0 partie.</div>' #Création d'un affiche spécial pour chauqe ligne 
        return mytemplate.render(texte=text, elem="nombre de partie gagner par chaque joueur")
    
    @cherrypy.expose
    def affDonne162(self):
        """Afficher les parties où il y a une donne supérieure à 162."""
        mytemplate = mylookup.get_template("aff_liste.html")
        return mytemplate.render(liste= [donne162(e) for e in getListe("selectAnnonce162")], elem=" partie où il y a une donne supérieure à 162")

    @cherrypy.expose
    def affAnnonceJoueur(self):
        """Afficher les annonces d'un joueur."""
        mytemplate = mylookup.get_template("aff_AnnonceJoueur.html")
        return mytemplate.render(texte="", message="")
    
    @cherrypy.expose
    def affAnnonceJoueur_affJoueur(self):
        """Afficher la liste des joueurs pour les annonces."""
        mytemplate = mylookup.get_template("aff_AnnonceJoueur.html")
        text = "Voici la liste des joueurs : "
        for e in getmkliste("joueur"):
            text = text + f'<div class="list-group-item rounded">{joueurToString(e)}</div>'# Création d'un affiche spécial pour chauqe ligne 
        return mytemplate.render(texte=text, message="")

    @cherrypy.expose
    def affAnnonceJoueur_Do(self, id=None):
        """Afficher les annonces d'un joueur spécifique.
        id (int): L'identifiant du joueur pour laquelle les annonces doivent être affichées."""
        text = AnnonceJoueur(id)
        mytemplate = mylookup.get_template("aff_AnnonceJoueur.html")
        return mytemplate.render(texte="", message=text)
    
    @cherrypy.expose
    def affAnnoncePartie(self):
        """Afficher les annonces d'une partie."""
        mytemplate = mylookup.get_template("aff_AnnoncePartie.html")
        return mytemplate.render(texte="", message="")
    
    @cherrypy.expose
    def affAnnoncePartie_affPartie(self):
        """Afficher la liste des parties pour les annonces."""
        mytemplate = mylookup.get_template("aff_AnnoncePartie.html")
        text = "Voici la liste des parties : "
        for e in getListe("selectPartie"):
            text = text + f'<div class="list-group-item rounded">{partieToString(e)}</div>' #Création d'un affiche spécial pour chauqe ligne 
        return mytemplate.render(texte=text, message="")

    @cherrypy.expose
    def affAnnoncePartie_Do(self, id=None):
        """Afficher les annonces d'une partie spécifique.
        id (int): L'identifiant de la partie pour laquelle les annonces doivent être affichées."""
        text = AnnoncePartie(id)
        mytemplate = mylookup.get_template("aff_AnnoncePartie.html")
        return mytemplate.render(texte="", message=text)

#######################################################################################
#                        INSERTION                                                    #
#######################################################################################        
    @cherrypy.expose
    def insert_Annonce(self):
        """Affiche la page pour insérer une nouvelle annonce."""        
        mytemplate = mylookup.get_template("Insert_Annonces.html")        
        return mytemplate.render(message="Veuillez remplir tous les champs",type="info")
    
    @cherrypy.expose
    def doInsertAnnonce(self, carre1=None, carre2=None, _100=None, nb50=None, nbTierce=None, belote=None, id_joueur=None, id_donne=None):
        """Insère une nouvelle annonce dans la base de données."""
        try:
            doInsertAnnonce(carre1, carre2, _100, nb50, nbTierce, belote, id_joueur, id_donne)
            message = "Insertion réussie !"
            typ = "success"
        except Exception as e:
            message = str(e)
            typ = "danger"

        mytemplate = mylookup.get_template("Insert_Annonces.html")        
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def insert_Donne(self):    
        """Affiche la page pour insérer une nouvelle Donne."""            
        mytemplate = mylookup.get_template("Insert_Donne.html")        
        return mytemplate.render(message="Veuillez remplir tous les champs", type="info")
    
    @cherrypy.expose
    def doInsertDonne(self, point_equipe1=None, point_equipe2=None, win_enchere=None, id_equipe1=None, id_equipe2=None, id_partie=None):
        """Insère une nouvelle donne dans la base de données."""
        try:
            doInsertDonne(point_equipe1, point_equipe2, win_enchere, id_equipe1, id_equipe2, id_partie)
            message = "Insertion réussie !"
            typ = "success"
        except Exception as e:
            message = str(e)
            typ = "danger"

        mytemplate = mylookup.get_template("Insert_Donne.html")        
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def insert_Encheres(self):     
        """Affiche la page pour insérer une nouvelle Encheres."""           
        mytemplate = mylookup.get_template("Insert_Encheres.html")        
        return mytemplate.render(message="Veuillez remplir tous les champs", type="info")
    
    @cherrypy.expose
    def doInsertEncheres(self, couleur=None, montant=None, id_joueur=None, id_donne=None):
        """Insère une nouvelle encheres dans la base de données."""
        try:
            doInsertEncheres(couleur, montant, id_joueur, id_donne)
            message = "Insertion réussie !"
            typ = "success"
        except Exception as e:
            message = str(e)
            typ = "danger"
        mytemplate = mylookup.get_template("Insert_Encheres.html")        
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def insert_Joueurs(self):     
        """Affiche la page pour insérer une nouveau joueur."""           
        mytemplate = mylookup.get_template("Insert_Joueurs.html")        
        return mytemplate.render(message="Veuillez remplir tous les champs", type="info")

    @cherrypy.expose
    def doInsertJoueurs(self, nom=None, prenom=None, date_naissance=None):
        """Insère un nouveau joueur dans la base de données."""
        try:
            doInsertJoueur(nom, prenom, date_naissance)
            message = "Insertion réussie !"
            typ = "success"
        except Exception as e:
            message = str(e)
            typ = "danger"

        mytemplate = mylookup.get_template("Insert_Joueurs.html")        
        return mytemplate.render(message=message, type=typ)
    
    @cherrypy.expose
    def insert_Equipe(self):      
        """Affiche la page pour insérer une nouvelle équipe."""          
        mytemplate = mylookup.get_template("Insert_Equipe.html")        
        return mytemplate.render(message="Veuillez remplir tous les champs", type="info")
    
    @cherrypy.expose
    def doInsertEquipe(self, nom_equipe=None, description_equipe=None, id_joueur1=None, id_joueur2=None):
        """Insère une nouvelle equipe dans la base de données."""
        try:
            doInsertEquipe(nom_equipe, description_equipe, id_joueur1, id_joueur2)
            message = "Insertion réussie !"
            typ = "success"
        except Exception as e:
            message = str(e)
            typ = "danger"

        mytemplate = mylookup.get_template("Insert_Equipe.html")        
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def insert_Partie(self):       
        """Affiche la page pour insérer une nouvelle partie."""         
        mytemplate = mylookup.get_template("Insert_Partie.html")        
        return mytemplate.render(message="Veuillez remplir tous les champs", type="info")
    
    @cherrypy.expose
    def doInsertPartie(self, date_partie=None, heure_debut=None, lieu_partie=None):
        """Insère une nouvelle partie dans la base de données."""
        try:
            doInsertPartie(date_partie, heure_debut, lieu_partie)
            message = "Insertion réussie !"
            typ = "success"
        except Exception as e:
            message = str(e)
            typ = "danger"

        mytemplate = mylookup.get_template("Insert_Partie.html")        
        return mytemplate.render(message=message, type=typ)
    
#######################################################################################
#                        SUPRESSION                                                   #
#######################################################################################   
    @cherrypy.expose
    def Supprimer(self, table=None):
        """Affiche la page pour supprimer un element d'une table.
        table (int): contient le numéro de la table ou l'utilisateur veut supprimer des données  
        """ 
        mytemplate = mylookup.get_template("Supp_elem.html")        
        return mytemplate.render(liste=[t for t in afichTable(int(table))], table=table, message="Ici vous pouvez supprimer un élément d'une table", type="info", tablesupr=['Annonce', 'Donne', 'Encheres', 'Equipe', 'Joueur', 'Partie'][int(table)-1])

    @cherrypy.expose
    def supprimer_joueur(self, id=None, table=None):
        """Affiche la page pour supprimer un element d'une table.
        table (int): contient le numéro de la table ou l'utilisateur veut supprimer des données  
        id (int) : contient l'id de l'élément a supprimer
        """ 
        try : suprID(int(table), int(id))
        except Exception as e : message = ("Erreur : ",e, e.__traceback__.tb_lineno); typ = "danger"
        else : message = "Votre élément a été suprimer avec succés!"; typ = "success"
        mytemplate = mylookup.get_template("Supp_elem.html")        
        return mytemplate.render(liste=[t for t in afichTable(int(table))], table=table, message=message, type=typ, tablesupr=['Annonce', 'Donne', 'Encheres', 'Equipe', 'Joueur', 'Partie'][int(table)-1])

#######################################################################################
#                        MODIFICATION                                                 #
#######################################################################################  

    @cherrypy.expose
    def Modifier(self, table=None):
        """Affiche la page pour modifier un element d'une table.
        table (int): contient le numéro de la table ou l'utilisateur veut modifier des données  
        """ 
        mytemplate = mylookup.get_template("Modif_elem.html")        
        return mytemplate.render(liste=[t for t in afichTable(int(table))], table=int(table), message="Ici vous pouvez modifier un élément d'une table", type="info", tablesupr=['Annonce', 'Donne', 'Encheres', 'Equipe', 'Joueur', 'Partie'][int(table)-1])

    @cherrypy.expose
    def DoModifier(self, table=None, id=None, date_partie=None, heure_debut=None, adresse=None, nom=None, prenom=None, date_naissance=None, nom_equipe=None, description_equipe=None, id_joueur1=None, id_joueur2=None, points_equipe1=None, points_equipe2=None, equipe_gagnante=None, id_equipe1=None, id_equipe2=None, id_partie=None, couleur=None, montant_enchere=None, id_joueur=None, id_donne=None, carre_1=None, carre_2=None, cent=None, nombre_50=None, tierces=None, belote=None, id_joueur_A=None, id_donne_A=None):
        """Affiche la page pour modifier un element d'une table.
        table (int): contient le numéro de la table ou l'utilisateur veut modifier des données  
        id (int) : contient l'id de l'élément a modifier
        les autre variable sont les élément que l'utilisateur peut modifer : 
            Si l'élement est pas vide/contient un truc 
            on l'insert grâce a la focntion doUpdate qui utilise 
            le numero de la table et l'id de l'élément a modifier
        """ 
        try:
            table_names = ['annonce', 'donne', 'encheres', 'equipe', 'joueur', 'partie']
            table_name = table_names[int(table)-1]
            if date_partie is not None and date_partie != "None" and date_partie != '':
                doUpdate(table_name, 'date', date_partie, id)
            if heure_debut is not None and heure_debut != "None" and heure_debut != "":
                doUpdate(table_name, 'heureDebut', heure_debut, id)
            if adresse is not None and adresse != "None" and adresse != "":
                doUpdate(table_name, 'Adresse', adresse, id)
            if nom is not None and nom != "None" and nom != "":
                doUpdate(table_name, 'Nom', nom, id)
            if prenom is not None and prenom != "None" and prenom != "":
                doUpdate(table_name, 'Prenom', prenom, id)
            if date_naissance is not None and date_naissance != "None" and date_naissance != "":
                doUpdate(table_name, 'DateNaissance', date_naissance, id)
            if nom_equipe is not None and nom_equipe != "None" and nom_equipe != "":
                doUpdate(table_name, 'nom', nom_equipe, id)
            if description_equipe is not None and description_equipe != "None" and description_equipe != "":
                doUpdate(table_name, 'description', description_equipe, id)
            if id_joueur1 is not None and id_joueur1 != "None" and id_joueur1 != "":
                doUpdate(table_name, 'IdJoueur1', id_joueur1,  id)
            if id_joueur2 is not None and id_joueur2 != "None" and id_joueur2 != "":
                doUpdate(table_name, 'IdJoueur2', id_joueur2, id)
            if points_equipe1 is not None and points_equipe1 != "None" and points_equipe1 != "":
                doUpdate(table_name, 'pointEequipe1', points_equipe1, id)
            if points_equipe2 is not None and points_equipe2 != "None" and points_equipe2 != "":
                doUpdate(table_name, 'pointEquipe2', points_equipe2, id)
            if equipe_gagnante is not None and equipe_gagnante != "None" and equipe_gagnante != "":
                doUpdate(table_name, 'winEnchere', equipe_gagnante, id)
            if id_equipe1 is not None and id_equipe1 != "None" and id_equipe1 != "":
                doUpdate(table_name, 'idEquipe1', id_equipe1, id)
            if id_equipe2 is not None and id_equipe2 != "None" and id_equipe2 != "":
                doUpdate(table_name, 'idEquipe2', id_equipe2, id)
            if id_partie is not None and id_partie != "None" and id_partie != "":
                doUpdate(table_name, 'idPartie', id_partie, id)
            if couleur is not None and couleur != "None" and couleur != "":
                doUpdate(table_name, 'couleur', couleur, id)
            if montant_enchere is not None and montant_enchere != "None" and montant_enchere != "":
                doUpdate(table_name, 'hauteur', montant_enchere, id)
            if id_joueur is not None and id_joueur != "None" and id_joueur != "":
                doUpdate(table_name, 'numero', id_joueur, id) 
            if id_donne is not None and id_donne != "None" and id_donne != "":
                doUpdate(table_name, 'id_donne', id_donne, id)
            if carre_1 is not None and carre_1 != "None" and carre_1 != "":
                doUpdate(table_name, 'carre_1', carre_1, id)
            if carre_2 is not None and carre_2 != "None" and carre_2 != "":
                doUpdate(table_name, 'carre_2', carre_2, id)
            if cent is not None and cent != "None" and cent != "":
                doUpdate(table_name, 'cent', cent, id)
            if nombre_50 is not None and nombre_50 != "None" and nombre_50 != "":
                doUpdate(table_name, 'nombre_50', nombre_50, id)
            if tierces is not None and tierces != "None" and tierces != "":
                doUpdate(table_name, 'tierces', tierces, id)
            if belote is not None and belote != "None" and belote != "":
                doUpdate(table_name, 'belote', belote, id)
            if id_donne_A is not None and id_donne_A != "None" and id_donne_A != "":
                doUpdate(table_name, 'IdDonne', id_donne_A, id)
            if id_joueur_A is not None and id_joueur_A != "None" and id_joueur_A != "":
                doUpdate(table_name, 'IdJoueur', id_joueur_A, id)
            message = "Modification réussie !"
            typ = "success"
        except Exception as e:
            message = str(e)
            typ = "danger"
        mytemplate = mylookup.get_template("Modif_elem.html")     
        return mytemplate.render(liste=[t for t in afichTable(int(table))], table=int(table), message=message, type=typ, tablesupr=['Annonce', 'Donne', 'Encheres', 'Equipe', 'Joueur', 'Partie'][int(table)-1])

#######################################################################################
#                        Partie dynamique                                             #
#######################################################################################  

    def Afich_Partie_Direct(self):
        """Affiche l'état des parties en direct, ainsi que leurs informations détaillées."""
        liste = getListe('selectPartieDirect')
        listeEquipe = getmkliste("equipe")
        newListe = []
        newListefin = []
        listeDonne= []
        listeDonnefin=[]
        listeCompo = []
        listeCompofin = []
        for e in liste : 
            if e[0] >= 3000 or e[1] >= 3000 : #Si la partie est fini on traite ces données mais en les mettans en dernier dans les différentes liste
                text = "Partie fini"
                liste = doselectDonnePartie(int(e[4]))[1:]
                Elem1 = doselectDonnePartie(int(e[4]))[0]
                listeCompofin.append(doselectCompoDonne(int(e[4])))
                newlistedonne = []
                boo1 = False
                for d in liste :
                    if d[0] == Elem1[0] : 
                        newlistedonne.append([list(d), list(Elem1)])
                        boo1 = True
                    else :
                        if boo1 == True : boo1 = False
                        else : newlistedonne.append([list(Elem1)])
                        Elem1 = d
                newlistedonne.append([list(doselectDonnePartie(int(e[4]))[-1])])
                listeDonnefin.append(newlistedonne)
                newListefin.append([text, e])
            else : 
                text = "Partie en cours"
                liste = doselectDonnePartie(int(e[4]))[1:]
                Elem1 = doselectDonnePartie(int(e[4]))[0]
                listeCompo.append(doselectCompoDonne(int(e[4])))
                newlistedonne = []
                boo1 = False
                for d in liste :
                    if d[0] == Elem1[0] : 
                        
                        newlistedonne.append([list(d), list(Elem1)])
                        boo1 = True
                    else :
                        if boo1 == True : boo1 = False
                        else : newlistedonne.append([list(Elem1)])
                        Elem1 = d
                newlistedonne.append([list(doselectDonnePartie(int(e[4]))[-1])])
                listeDonne.append(newlistedonne)
                newListe.append([text, e])

        mytemplate = mylookup.get_template("Partie_Direct.html")        
        return mytemplate.render(partie=newListe+newListefin, donne=listeDonne+listeDonnefin, equipe = listeEquipe, compo = listeCompo+listeCompofin)

    @cherrypy.expose
    def Afich_Partie_Direct_Insert1(self, points_equipe1, points_equipe2, equipe2, equipe1, lieu_partie, heure_debut, date_partie):
        """
        Insère une nouvelle partie avec la première donne.

        Parameters:
            points_equipe1 (int): Points de l'équipe 1.
            points_equipe2 (int): Points de l'équipe 2.
            equipe2 (int): ID de l'équipe 2.
            equipe1 (int): ID de l'équipe 1.
            lieu_partie (str): Lieu de la partie.
            heure_debut (str): Heure de début de la partie.
            date_partie (str): Date de la partie.
        """
        try:
            doInsertPartie(date_partie, heure_debut, lieu_partie)
            idPartie = doselectPartieID(date_partie, heure_debut, lieu_partie)[0][0]
            doInsertDonne(points_equipe1, points_equipe2, "null", equipe1, equipe2, idPartie)
        except Exception as e:
            message = str(e)
            typ = "danger"

        # Réutilisation du code pour afficher les parties en direct après insertion
        return self.Afich_Partie_Direct()

    @cherrypy.expose
    def Afich_Partie_Direct_Insert2(self, points_equipe1, points_equipe2, idPartie, id_equipe1, id_equipe2):
        """
        Insère une nouvelle donne pour une partie existante.

        Parameters:
            points_equipe1 (int): Points de l'équipe 1.
            points_equipe2 (int): Points de l'équipe 2.
            idPartie (int): ID de la partie.
            id_equipe1 (int): ID de l'équipe 1.
            id_equipe2 (int): ID de l'équipe 2.
        """
        try:
            doInsertDonne(points_equipe1, points_equipe2, "null", id_equipe1, id_equipe2, idPartie)
        except Exception as e:
            message = str(e)
            typ = "danger"

        # Réutilisation du code pour afficher les parties en direct après insertion
        return self.Afich_Partie_Direct()
    
if __name__ == '__main__':
    print("\033[92m___________________________________________________________________________\n\n██╗      █████╗      ██████╗ ██████╗ ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗\n██║     ██╔══██╗    ██╔════╝██╔═══██╗██║████╗  ██║██╔════╝██║  ██║██╔════╝\n██║     ███████║    ██║     ██║   ██║██║██╔██╗ ██║██║     ███████║█████╗  \n██║     ██╔══██║    ██║     ██║   ██║██║██║╚██╗██║██║     ██╔══██║██╔══╝  \n███████╗██║  ██║    ╚██████╗╚██████╔╝██║██║ ╚████║╚██████╗██║  ██║███████╗\n╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝\n___________________________________________________________________________\n\033[0m")
    rootPath = os.path.abspath(os.getcwd())
    try : 
        dbConnect() # on teste si on peut ce connecter a la BDD et si c'est pas le cas on renvoie une erreur
        print(f"la racine du site est :\n\t{rootPath}\n\tcontient : {os.listdir()}")
        #initBase()
        cherrypy.quickstart(InterfaceWeb(), '/', 'config.txt')
    except Exception as e : 
        print(f"\033[91mErreur : Imposible de ce connecter a la base de données. Vérifier le fichier de configuration et vérifier que phpmyadmin est bien lancée\033[0m \n{e}")
        print("\033[92m___________________________________________________________________________\033[0m\n")
        print('\033[92m########  ##    ## ########    #### \n##     ##  ##  ##  ##          #### \n##     ##   ####   ##          #### \n########     ##    ######       ##  \n##     ##    ##    ##               \n##     ##    ##    ##          #### \n########     ##    ########    ####\033[0m')
    except KeyboardInterrupt : #Erreur qui permet une fermeture plus "propre" quand l'utilisateur fait CTRL+C
        print("\n\033[92m___________________________________________________________________________\033[0m\n")
        print('\033[92m########  ##    ## ########    #### \n##     ##  ##  ##  ##          #### \n##     ##   ####   ##          #### \n########     ##    ######       ##  \n##     ##    ##    ##               \n##     ##    ##    ##          #### \n########     ##    ########    ####\033[0m')