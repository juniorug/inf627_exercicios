INSERT INTO sensor_family (id, family_name, default_measure_unit)
VALUES (1, 'Temperature', '°C'),
       (2, 'Humidity', '%'),
       (3, 'Luminosity', 'lx');

INSERT INTO place (id, description)
VALUES (1, 'center inside');

INSERT INTO sensor (id, sensor_family_id,place_id, sensor_type,pin,sampling_time, status)
VALUES (1, 1, 1, 'DHT11Temperture', 4, 5, 1),
       (2, 2, 1, 'DHT11Humidity', 4, 5, 1),
       (3, 3, 1, 'LDR', 18, 5, 1);

-- -----------------------------------------------------
-- select * from sensor_family;
-- select * from sensor;
-- select * from place;
-- select * from sensor_measurement;
-- -----------------------------------------------------
