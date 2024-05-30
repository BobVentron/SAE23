-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : ven. 12 avr. 2024 à 14:20
-- Version du serveur : 8.2.0
-- Version de PHP : 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `soleilhac-sae`
--
CREATE DATABASE IF NOT EXISTS `soleilhac-sae` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `soleilhac-sae`;

-- --------------------------------------------------------q

DROP TABLE IF EXISTS `annonce`;
CREATE TABLE IF NOT EXISTS `annonce` (
  `IdAnnonce` int NOT NULL AUTO_INCREMENT,
  `carre1` enum('roi','dame','valets','as','dix','neuf','huit','sept','null') COLLATE utf8mb4_general_ci DEFAULT NULL,
  `carre2` enum('roi','dame','valets','as','dix','neuf','huit','sept','null') COLLATE utf8mb4_general_ci DEFAULT NULL,
  `100` tinyint(1) NOT NULL DEFAULT '0',
  `nb50` enum('0','1','2','') COLLATE utf8mb4_general_ci NOT NULL,
  `nbTierce` enum('0','1','2','') COLLATE utf8mb4_general_ci NOT NULL,
  `belote` tinyint(1) DEFAULT NULL,
  `IdJoueur` int DEFAULT NULL,
  `IdDonne` int NOT NULL,
  PRIMARY KEY (`IdAnnonce`),
  KEY `IdJoueur` (`IdJoueur`,`IdDonne`),
  KEY `IdDonne` (`IdDonne`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `annonce` (`IdAnnonce`, `carre1`, `carre2`, `100`, `nb50`, `nbTierce`, `belote`, `IdJoueur`, `IdDonne`) VALUES
(1, 'null', 'null', 0, '0', '1', 0, 3, 1),
(2, 'null', 'null', 0, '1', '0', 0, 9, 2),
(3, 'null', 'null', 0, '0', '1', 0, 3, 3),
(4, 'null', 'null', 1, '0', '0', 1, 4, 4),
(5, 'neuf', 'null', 0, '0', '0', 0, 4, 5),
(6, 'null', 'null', 0, '1', '0', 1, 3, 6),
(7, 'null', 'null', 0, '1', '0', 0, 10, 7),
(8, 'null', 'null', 0, '0', '0', 1, 9, 8),
(9, 'null', 'null', 0, '1', '0', 0, 10, 9),
(10, 'null', 'null', 0, '1', '0', 1, 9, 10),
(11, 'null', 'null', 0, '1', '0', 1, 9, 10),
(12, 'null', 'null', 0, '1', '0', 0, 10, 11),
(13, 'null', 'null', 1, '0', '0', 0, 9, 11),
(14, 'null', 'null', 0, '0', '1', 1, 9, 12),
(15, 'valets', 'null', 0, '0', '0', 1, 6, 14);

DROP TABLE IF EXISTS `donne`;
CREATE TABLE IF NOT EXISTS `donne` (
  `IdDonne` int NOT NULL AUTO_INCREMENT,
  `pointEquipe1` int DEFAULT NULL,
  `pointEquipe2` int DEFAULT NULL,
  `winEnchere` enum('equipe1','equipe2','') COLLATE utf8mb4_general_ci NOT NULL,
  `idEquipe1` int DEFAULT NULL,
  `idEquipe2` int DEFAULT NULL,
  `idPartie` int NOT NULL,
  PRIMARY KEY (`IdDonne`),
  KEY `idEquipe1` (`idEquipe1`,`idEquipe2`,`idPartie`),
  KEY `idPartie` (`idPartie`),
  KEY `idEquipe2` (`idEquipe2`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `donne` (`IdDonne`, `pointEquipe1`, `pointEquipe2`, `winEnchere`, `idEquipe1`, `idEquipe2`, `idPartie`) VALUES
(1, 180, 70, 'equipe1', 1, 4, 1),
(2, 30, 295, 'equipe2', 1, 4, 1),
(3, 50, 245, 'equipe2', 1, 4, 1),
(4, 430, 0, 'equipe1', 1, 4, 1),
(5, 530, 30, 'equipe1', 1, 4, 1),
(6, 305, 40, 'equipe1', 1, 4, 1),
(7, 30, 350, 'equipe2', 1, 4, 1),
(8, 395, 20, 'equipe1', 1, 4, 1),
(9, 295, 45, 'equipe1', 1, 4, 1),
(10, 420, 30, 'equipe1', 1, 4, 1),
(11, 230, 60, 'equipe1', 1, 4, 1),
(12, 50, 205, 'equipe2', 1, 4, 1),
(13, 190, 70, 'equipe1', 1, 4, 1),
(14, 10, 720, 'equipe2', 2, 3, 2);

DROP TABLE IF EXISTS `encheres`;
CREATE TABLE IF NOT EXISTS `encheres` (
  `IdEncheres` int NOT NULL AUTO_INCREMENT,
  `couleur` enum('pique','careau','trefle','coeur') COLLATE utf8mb4_general_ci NOT NULL,
  `hauteur` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `numero` int NOT NULL,
  `idDonne` int NOT NULL,
  PRIMARY KEY (`IdEncheres`),
  KEY `idDonne` (`idDonne`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `encheres` (`IdEncheres`, `couleur`, `hauteur`, `numero`, `idDonne`) VALUES
(1, 'pique', '85', 1, 2),
(2, 'careau', '90', 2, 2),
(3, 'pique', '95', 3, 2),
(4, 'careau', '105', 4, 2),
(5, 'pique', '110', 5, 2),
(6, 'careau', '115', 6, 2),
(7, 'trefle', '100', 1, 3),
(8, 'coeur', '105', 2, 3),
(9, 'trefle', '115', 3, 3),
(10, 'coeur', '150', 1, 4),
(11, 'coeur', '250', 1, 5),
(12, 'trefle', '90', 1, 6),
(13, 'pique', '115', 2, 6),
(14, 'careau', '85', 1, 7),
(15, 'coeur', '150', 2, 7),
(16, 'pique', '135', 1, 8),
(17, 'careau', '110', 1, 9),
(18, 'pique', '90', 1, 10),
(19, 'trefle', '95', 2, 10),
(20, 'pique', '140', 3, 10),
(21, 'coeur', '90', 1, 11),
(22, 'pique', '85', 1, 12),
(23, 'pique', '90', 1, 13),
(24, 'careau', '350', 1, 14);

DROP TABLE IF EXISTS `equipe`;
CREATE TABLE IF NOT EXISTS `equipe` (
  `idEquipe` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `description` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `idJoueur1` int DEFAULT NULL,
  `idJoueur2` int DEFAULT NULL,
  PRIMARY KEY (`idEquipe`),
  KEY `idJoueur1` (`idJoueur1`,`idJoueur2`),
  KEY `idJoueur2` (`idJoueur2`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `equipe` (`idEquipe`, `nom`, `description`, `idJoueur1`, `idJoueur2`) VALUES
(1, 'Les Maîtres du Jeu', 'Les pros du jeu', 3, 4),
(2, 'Les Invincibles', 'Les gagnants', 5, 6),
(3, 'Les Titans', 'Les champions', 7, 8),
(4, 'Les Experts', 'Les experts', 9, 10),
(5, 'Les Stratèges', 'Les stratèges', 1, 3),
(6, 'Les Dominators', 'Les invincibles', 2, 4),
(7, 'Les Rois du Jeu', 'Équipe royale', 5, 7),
(8, 'Les Requins', 'Les requins', 6, 1);

DROP TABLE IF EXISTS `joueur`;
CREATE TABLE IF NOT EXISTS `joueur` (
  `idJoueur` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Prenom` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `DateNaissance` date NOT NULL,
  PRIMARY KEY (`idJoueur`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `joueur` (`idJoueur`, `Nom`, `Prenom`, `DateNaissance`) VALUES
(1, 'Doe', 'John', '1990-05-15'),
(2, 'Smith', 'Emma', '1985-10-28'),
(3, 'Johnson', 'Michael', '1978-03-20'),
(4, 'Williams', 'Sophia', '1992-07-12'),
(5, 'Brown', 'James', '1983-09-05'),
(6, 'Miller', 'Olivia', '1975-12-18'),
(7, 'Davis', 'William', '1988-02-25'),
(8, 'Garcia', 'Isabella', '1995-04-30'),
(9, 'Rodriguez', 'Alexander', '1980-06-22'),
(10, 'Martinez', 'Emily', '1970-08-14');

DROP TABLE IF EXISTS `partie`;
CREATE TABLE IF NOT EXISTS `partie` (
  `IdPartie` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `heureDebut` time NOT NULL,
  `Adresse` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`IdPartie`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `partie` (`IdPartie`, `date`, `heureDebut`, `Adresse`) VALUES
(1, '2024-04-01', '14:00:00', '123 Rue de la Paix 75001 Paris'),
(2, '2024-04-05', '15:30:00', '456 Avenue des Champs-Élysées 75008 Paris'),
(3, '2024-04-10', '19:00:00', '789 Boulevard Saint-Germain 75006 Paris');


ALTER TABLE `annonce`
  ADD CONSTRAINT `annonce_ibfk_1` FOREIGN KEY (`IdJoueur`) REFERENCES `joueur` (`idJoueur`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `annonce_ibfk_2` FOREIGN KEY (`IdDonne`) REFERENCES `donne` (`IdDonne`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `donne`
  ADD CONSTRAINT `donne_ibfk_1` FOREIGN KEY (`idPartie`) REFERENCES `partie` (`IdPartie`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `donne_ibfk_2` FOREIGN KEY (`idEquipe1`) REFERENCES `equipe` (`idEquipe`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `donne_ibfk_3` FOREIGN KEY (`idEquipe2`) REFERENCES `equipe` (`idEquipe`) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE `encheres`
  ADD CONSTRAINT `encheres_ibfk_1` FOREIGN KEY (`idDonne`) REFERENCES `donne` (`IdDonne`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `equipe`
  ADD CONSTRAINT `equipe_ibfk_1` FOREIGN KEY (`idJoueur1`) REFERENCES `joueur` (`idJoueur`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `equipe_ibfk_2` FOREIGN KEY (`idJoueur2`) REFERENCES `joueur` (`idJoueur`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;