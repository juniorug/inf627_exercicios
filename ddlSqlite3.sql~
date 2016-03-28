-- -----------------------------------------------------
-- Table `mydb`.`sensor_family`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sensor_family` (
  `id` INT NOT NULL,
  `family_name` VARCHAR(45) NULL,
  `default_measure_unit` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
  
-- -----------------------------------------------------
-- Table `mydb`.`sensor`
-- -----------------------------------------------------  
CREATE TABLE IF NOT EXISTS `sensor` (
  `id` INT NOT NULL,
  `sensor_family_id` INT NOT NULL,
  `sensor_type` VARCHAR(45) NULL,
  `status` VARCHAR(45) NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (`sensor_family_id`) REFERENCES sensor_family (`id`) 
);
  
-- -----------------------------------------------------
-- Table `mydb`.`place`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `place` (
  `id` INT NOT NULL,
  `description` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
  
-- -----------------------------------------------------
-- Table `mydb`.`sensor_measurement`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sensor_measurement` (
  `id` INTEGER PRIMARY KEY NOT NULL,
  `sensor_id` INT NULL,
  `datetime_measurement` TIMESTAMP(6) NULL,
  `value` VARCHAR(45) NULL,
  `place_id` INT NULL,
  FOREIGN KEY (`sensor_id`) REFERENCES `sensor` (`id`),
  FOREIGN KEY (`place_id`)  REFERENCES `place` (`id`));
