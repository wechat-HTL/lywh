DROP DATABASE IF EXISTS `lywh`;
CREATE DATABASE `lywh` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `lywh`;
SET NAMES utf8;
SET SESSION storage_engine = "InnoDB";
SET SESSION time_zone = "+8:00";
ALTER DATABASE CHARACTER SET "utf8";

# lywh user表
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nickname` VARCHAR(128) NOT NULL UNIQUE,
    `avatar` VARCHAR(128),
    `role` VARCHAR(32),
    `status` VARCHAR(32),
    `password` VARCHAR (128),
    `email` VARCHAR(128),
    `desp` VARCHAR(256),
    `created_at` DATETIME NOT NULL,
    `updated_at` DATETIME,
	  KEY (`created_at`),
    KEY (`status`),
    KEY (`updated_at`),
    KEY (`nickname`)
)DEFAULT CHARSET = UTF8;