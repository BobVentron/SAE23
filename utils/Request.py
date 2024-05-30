"""
Ce fichier contient sous forme de 3  dictionnaire  les requetes nessesaire a l'appliquation pour:
    -créer la base, 
    -inserer des elements
    -selection des elements
"""

_requetesCreateDatabase = {
    "drop" : "DROP DATABASE IF EXISTS {}",
    "createBase" : "CREATE DATABASE IF NOT EXISTS `{}` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;",
    "use" : "USE `{}`;",
    "createTableAnnonce" : "CREATE TABLE IF NOT EXISTS `annonce` (\
        `IdAnnonce` int NOT NULL AUTO_INCREMENT,\
        `carre1` enum('roi','dame','valets','as','dix','neuf','huit','sept', 'null') DEFAULT NULL,\
        `carre2` enum('roi','dame','valets','as','dix','neuf','huit','sept', 'null') DEFAULT NULL,\
        `100` tinyint(1) NOT NULL DEFAULT '0',\
        `nb50` enum('0','1','2','') NOT NULL,\
        `nbTierce` enum('0','1','2','') NOT NULL,\
        `belote` tinyint(1) DEFAULT NULL,\
        `IdJoueur` int DEFAULT NULL,\
        `IdDonne` int NOT NULL,\
        PRIMARY KEY (`IdAnnonce`),\
        KEY `IdJoueur` (`IdJoueur`,`IdDonne`),\
        KEY `IdDonne` (`IdDonne`)\
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;",
    "createTableDonne" : "CREATE TABLE IF NOT EXISTS `donne` (\
        `IdDonne` int NOT NULL AUTO_INCREMENT,\
        `pointEquipe1` int DEFAULT NULL,\
        `pointEquipe2` int DEFAULT NULL,\
        `winEnchere` enum('equipe1','equipe2','') NOT NULL,\
        `idEquipe1` int DEFAULT NULL,\
        `idEquipe2` int DEFAULT NULL,\
        `idPartie` int NOT NULL,\
        PRIMARY KEY (`IdDonne`),\
        KEY `idEquipe1` (`idEquipe1`,`idEquipe2`,`idPartie`),\
        KEY `idPartie` (`idPartie`),\
        KEY `idEquipe2` (`idEquipe2`)\
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;", 
    "createTableEncheres" : "CREATE TABLE IF NOT EXISTS `encheres` (\
        `IdEncheres` int NOT NULL AUTO_INCREMENT,\
        `couleur` enum('pique','careau','trefle','coeur') NOT NULL,\
        `hauteur` varchar(10) NOT NULL,\
        `numero` int NOT NULL,\
        `idDonne` int NOT NULL,\
        PRIMARY KEY (`IdEncheres`),\
        KEY `idDonne` (`idDonne`)\
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;", 
    "createTableEquipe" : "CREATE TABLE IF NOT EXISTS `equipe` (\
        `idEquipe` int NOT NULL AUTO_INCREMENT,\
        `nom` varchar(30) NOT NULL,\
        `description` varchar(50) NOT NULL,\
        `idJoueur1` int DEFAULT NULL,\
        `idJoueur2` int DEFAULT NULL,\
        PRIMARY KEY (`idEquipe`),\
        KEY `idJoueur1` (`idJoueur1`,`idJoueur2`),\
        KEY `idJoueur2` (`idJoueur2`)\
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;", 
    "createTableJoueur" : "CREATE TABLE IF NOT EXISTS `joueur` (\
        `idJoueur` int NOT NULL AUTO_INCREMENT,\
        `Nom` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,\
        `Prenom` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,\
        `DateNaissance` date NOT NULL,\
        PRIMARY KEY (`idJoueur`)\
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;", 
    "createTablePartie" : "CREATE TABLE IF NOT EXISTS `partie` (\
        `IdPartie` int NOT NULL AUTO_INCREMENT,\
        `date` date NOT NULL,\
        `heureDebut` time NOT NULL,\
        `Adresse` varchar(50) NOT NULL,\
        PRIMARY KEY (`IdPartie`)\
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;", 
    "alterTableAnnonce" : "ALTER TABLE `annonce`\
        ADD CONSTRAINT `annonce_ibfk_1` FOREIGN KEY (`IdJoueur`) REFERENCES `joueur` (`idJoueur`) ON DELETE SET NULL ON UPDATE CASCADE,\
        ADD CONSTRAINT `annonce_ibfk_2` FOREIGN KEY (`IdDonne`) REFERENCES `donne` (`IdDonne`) ON DELETE CASCADE ON UPDATE CASCADE;", 
    "alterTableDonne" : "ALTER TABLE `donne`\
        ADD CONSTRAINT `donne_ibfk_1` FOREIGN KEY (`idPartie`) REFERENCES `partie` (`IdPartie`) ON DELETE CASCADE ON UPDATE CASCADE,\
        ADD CONSTRAINT `donne_ibfk_2` FOREIGN KEY (`idEquipe1`) REFERENCES `equipe` (`idEquipe`) ON DELETE SET NULL ON UPDATE CASCADE,\
        ADD CONSTRAINT `donne_ibfk_3` FOREIGN KEY (`idEquipe2`) REFERENCES `equipe` (`idEquipe`) ON DELETE SET NULL ON UPDATE CASCADE;", 
    "alterTableEncheres" : "ALTER TABLE `encheres`\
        ADD CONSTRAINT `encheres_ibfk_1` FOREIGN KEY (`idDonne`) REFERENCES `donne` (`IdDonne`) ON DELETE CASCADE ON UPDATE CASCADE;", 
    "alterTableEquipe" : "ALTER TABLE `equipe`\
        ADD CONSTRAINT `equipe_ibfk_1` FOREIGN KEY (`idJoueur1`) REFERENCES `joueur` (`idJoueur`) ON DELETE SET NULL ON UPDATE CASCADE,\
        ADD CONSTRAINT `equipe_ibfk_2` FOREIGN KEY (`idJoueur2`) REFERENCES `joueur` (`idJoueur`) ON DELETE SET NULL ON UPDATE CASCADE;", 
    "countAttributs" : "SELECT COUNT(*)\
        FROM information_schema.columns\
        WHERE table_schema = '{}' AND table_name = '{}';",
    "show" : "SHOW DATABASES",
    "delete" : "DELETE FROM {} where id{} = {};",
    "update" : "UPDATE {} SET {} = '{}' WHERE id{} = {}"
}

_requetesInsertDatabase = {
    "insertJoueur" : "INSERT INTO joueur (Nom, Prenom, DateNaissance) VALUES ('{}', '{}', '{}');",
    "insertPartie" : "INSERT INTO partie (date, heureDebut, Adresse) VALUES ('{}', '{}', '{}');",
    "insertEquipe" : "INSERT INTO equipe (nom, description, idJoueur1, idJoueur2) VALUES ('{}', '{}', {}, {});",
    "insertDonne" : "INSERT INTO donne (pointEquipe1, pointEquipe2, winEnchere, idEquipe1, idEquipe2, idPartie) VALUES ({}, {}, '{}', {}, {}, {});",
    "insertAnnonce" : "INSERT INTO annonce (carre1, carre2, `100`, nb50, nbTierce, belote, IdJoueur, IdDonne) VALUES ('{}', '{}', {}, '{}', '{}', {}, {}, {});",
    "insertEncheres" : "INSERT INTO encheres (couleur, hauteur, numero, idDonne) VALUES ('{}', {}, {}, {});",
}

_requetesSelectDatabase = {
    "select" : "SELECT * FROM {}",
    "selectJoueurOrdre" : "SELECT * FROM joueur ORDER BY Nom, Prenom;",
    "selectCompo" : "SELECT idEquipe, equipe.nom, CONCAT(j1.Prenom, ' ', j1.Nom) AS joueur1, CONCAT(j2.Prenom, ' ', j2.Nom) AS joueur2 FROM equipe LEFT JOIN joueur j1 ON equipe.idJoueur1 = j1.idJoueur LEFT JOIN joueur j2 ON equipe.idJoueur2 = j2.idJoueur;",
    "selectPartie" :" SELECT * from partie ORDER BY date",
    "selectAnnonceJoueur": "SELECT * FROM annonce join donne on annonce.IdDonne = donne.IdDonne WHERE IdJoueur = {}",
    "selectAnnoncePartie":"SELECT * FROM annonce join donne on annonce.IdDonne = donne.IdDonne WHERE donne.idPartie = {}",
    "selectNbPartieWin" : "SELECT \
            CONCAT(j.Nom, ' ', j.Prenom) AS NomComplet,\
            COUNT(*) AS PartiesRemportees\
        FROM \
            equipe e\
        JOIN \
            joueur j ON e.idJoueur1 = j.idJoueur\
        JOIN \
            (SELECT \
                idPartie,\
                CASE\
                    WHEN SUM(pointEquipe1) > SUM(pointEquipe2) THEN idEquipe1\
                    ELSE idEquipe2\
                END AS idEquipeGagnante\
            FROM \
                donne\
            GROUP BY \
                idPartie) AS gagnants ON e.idEquipe = gagnants.idEquipeGagnante\
        GROUP BY \
            e.idJoueur1, j.Nom, j.Prenom\
        UNION\
        SELECT \
            CONCAT(j.Nom, ' ', j.Prenom) AS NomComplet,\
            COUNT(*) AS PartiesRemportees\
        FROM \
            equipe e\
        JOIN \
            joueur j ON e.idJoueur2 = j.idJoueur\
        JOIN \
            (SELECT \
                idPartie,\
                CASE\
                    WHEN SUM(pointEquipe1) > SUM(pointEquipe2) THEN idEquipe1\
                    ELSE idEquipe2\
                END AS idEquipeGagnante\
            FROM \
                donne\
            GROUP BY \
                idPartie) AS gagnants ON e.idEquipe = gagnants.idEquipeGagnante\
        GROUP BY \
            e.idJoueur2, j.Nom, j.Prenom\
        ORDER BY\
            PartiesRemportees DESC;",
    "selectAnnonce162" : "SELECT\
            e.nom AS NomEquipe,\
            d.IdDonne,\
            d.idPartie,\
            p.Adresse AS LieuPartie,\
            p.date AS DatePartie\
        FROM \
            donne d\
        JOIN \
            (\
                SELECT \
                    IdDonne,\
                    CASE \
                        WHEN winEnchere = 'equipe1' THEN idEquipe1\
                        ELSE idEquipe2\
                    END AS IdEquipe\
                FROM \
                    donne\
            ) AS equipe_gagnante ON d.IdDonne = equipe_gagnante.IdDonne\
        JOIN \
            equipe e ON equipe_gagnante.IdEquipe = e.idEquipe \
        JOIN \
            partie p ON d.idPartie = p.IdPartie\
        JOIN \
            encheres en ON d.IdDonne = en.idDonne\
        WHERE \
            en.hauteur > 162;",
    "selectPartieDirect" : "SELECT SUM(pointEquipe1), sum(pointEquipe2), equipe1.nom, equipe2.nom , idPartie, equipe1.idEquipe, equipe2.idEquipe FROM `donne` JOIN equipe AS equipe1 ON donne.idEquipe1 = equipe1.idEquipe JOIN equipe AS equipe2 ON donne.idEquipe2 = equipe2.idEquipe GROUP BY idPartie ",
    "selectDonnePartie" : "SELECT * FROM `donne` LEFT JOIN annonce ON donne.IdDonne = annonce.IdDonne LEFT JOIN  joueur on annonce.IdJoueur = joueur.idJoueur LEFT JOIN (SELECT e.* FROM encheres e INNER JOIN (SELECT MAX(IdEncheres) AS MaxIdEncheres FROM encheres GROUP BY IdDonne) derniere_enchere ON e.IdEncheres = derniere_enchere.MaxIdEncheres) AS dernier_enchere ON donne.IdDonne = dernier_enchere.IdDonne   WHERE donne.idPartie = {} ORDER BY donne.IdDonne",
    "selectPartieID" : "SELECT `IdPartie` FROM `partie` WHERE `date` = '{}' AND `heureDebut` = '{}' AND `Adresse` = '{}';",
    "selectCompoDonne" : """SELECT donne.*, 
            joueur1.Nom AS NomJoueur1Equipe1, 
            joueur1.Prenom AS PrenomJoueur1Equipe1, 
            joueur2.Nom AS NomJoueur2Equipe1, 
            joueur2.Prenom AS PrenomJoueur2Equipe1,
            joueur3.Nom AS NomJoueur3Equipe2, 
            joueur3.Prenom AS PrenomJoueur3Equipe2, 
            joueur4.Nom AS NomJoueur4Equipe2, 
            joueur4.Prenom AS PrenomJoueur4Equipe2
        FROM donne 
        JOIN equipe AS equipe1 ON donne.idEquipe1 = equipe1.idEquipe 
        JOIN joueur AS joueur1 ON equipe1.idJoueur1 = joueur1.idJoueur 
        JOIN joueur AS joueur2 ON equipe1.idJoueur2 = joueur2.idJoueur 
        JOIN equipe AS equipe2 ON donne.idEquipe2 = equipe2.idEquipe 
        JOIN joueur AS joueur3 ON equipe2.idJoueur1 = joueur3.idJoueur 
        JOIN joueur AS joueur4 ON equipe2.idJoueur2 = joueur4.idJoueur
        WHERE donne.idPartie = {}
        LIMIT 1"""
}