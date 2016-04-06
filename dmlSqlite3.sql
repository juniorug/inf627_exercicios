INSERT INTO dashboard_sensorfamily (id, family_name, default_measure_unit)
VALUES (1, 'Temperature', '°C'),
       (2, 'Humidity', '%'),
       (3, 'Luminosity', 'lx');

INSERT INTO dashboard_place (id, description)
VALUES (1, 'center inside');

INSERT INTO dashboard_sensor (id, sensor_family_id,place_id, sensor_type,pin,sampling_time, status)
VALUES (1, 1, 1, 'DHT11Temperture', 4, 5, 'ON'),
       (2, 2, 1, 'DHT11Humidity', 4, 5, 'ON'),
       (3, 3, 1, 'LDR', 18, 5, 'ON');

-- -----------------------------------------------------
-- select * from dashboard_sensorfamily;
-- select * from dashboard_sensor;
-- select * from dashboard_place;
-- select * from dashboard_sensormeasurement;
-- select * from dashboard_sensormeasurement order by id asc;
-- 
-- update dashboard_sensormeasurement set date_measurement = date('now') where id > 0
-- update dashboard_sensormeasurement set date_measurement = date('now' , '-1 day') where id > 0
-- -----------------------------------------------------
