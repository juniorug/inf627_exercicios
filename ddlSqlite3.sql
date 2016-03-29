-- -----------------------------------------------------
-- Table `mydb`.`sensor_family`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sensor_family` (
  `id` INTEGER PRIMARY KEY NOT NULL,
  `family_name` VARCHAR(45) NULL,
  `default_measure_unit` VARCHAR(45) NULL
);

-- -----------------------------------------------------
-- Table `mydb`.`place`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `place` (
  `id` INTEGER PRIMARY KEY NOT NULL,
  `description` VARCHAR(45) NULL
);
  
-- -----------------------------------------------------
-- Table `mydb`.`sensor`
-- -----------------------------------------------------  
CREATE TABLE IF NOT EXISTS `sensor` (
  `id` INT NOT NULL,
  `sensor_family_id` INT NOT NULL,
  `place_id` INT NOT NULL, 
  `sensor_type` VARCHAR(45) NULL,
  `pin` INT NOT NULL,
  `sampling_time` INT NOT NULL,  
  `status` VARCHAR(45) NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (`sensor_family_id`) REFERENCES sensor_family (`id`) ,
  FOREIGN KEY (`place_id`)  REFERENCES `place` (`id`)
);
    
-- -----------------------------------------------------
-- Table `mydb`.`sensor_measurement`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sensor_measurement` (
  `id` INTEGER PRIMARY KEY NOT NULL,
  `sensor_id` INT NULL,
  `datetime_measurement` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `value` VARCHAR(45) NULL,
  FOREIGN KEY (`sensor_id`) REFERENCES `sensor` (`id`)
);
-- -----------------------------------------------------
-- drop table sensor_family;
-- drop table sensor;
-- drop table place;
-- drop table sensor_measurement;
-- -----------------------------------------------------
