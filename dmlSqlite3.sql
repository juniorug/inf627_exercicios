INSERT INTO sensor_family (id, family_name, default_measure_unit)
VALUES (1, 'Temperature', '°C'),
       (2, 'Humidity', '%'),
       (3, 'Luminosity', 'lx');


INSERT INTO sensor (id, sensor_family_id, sensor_type, status)
VALUES (1, 1, 'DHT11Temperture', 1),
       (2, 2, 'DHT11Humidity, 1),
       (3, 3, 'LDR', 1);


INSERT INTO place (id, description)
VALUES (1, 'center inside');

"""INSERT INTO sensor_measurement (sensor_id, datetime_measurement, place_id,value)
VALUES (?, ?, ?, ?);""",())

