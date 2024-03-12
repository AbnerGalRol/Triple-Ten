-- Encuentra la cantidad de viajes en taxi para cada compañía de taxis para el 15 y 16 de noviembre de 2017, asigna al campo resultante el nombre trips_amount e imprímelo también. 
-- Ordena los resultados por el campo trips_amount en orden descendente.
SELECT 
    cabs.company_name,
    COUNT(trips.trip_id) AS trips_amount 
FROM cabs
    INNER JOIN trips ON trips.cab_id = cabs.cab_id
WHERE
    trips.start_ts::date BETWEEN '2017-11-15' AND '2017-11-16'
GROUP BY
    cabs.company_name
ORDER BY
    trips_amount DESC;

-- Encuentra la cantidad de viajes para cada empresa de taxis cuyo nombre contenga las palabras "Yellow" o "Blue" del 1 al 7 de noviembre de 2017. 
SELECT 
    cabs.company_name,
    COUNT(trips.trip_id) AS trips_amount 
FROM cabs
    INNER JOIN trips ON trips.cab_id = cabs.cab_id
WHERE
    cabs.company_name LIKE '%Yellow%'
    AND
    trips.start_ts::date BETWEEN '2017-11-01' AND '2017-11-07'
GROUP BY
    cabs.company_name

UNION

SELECT 
    cabs.company_name,
    COUNT(trips.trip_id) AS trips_amount 
FROM cabs
    INNER JOIN trips ON trips.cab_id = cabs.cab_id
WHERE
    cabs.company_name LIKE '%Blue%'
    AND
    trips.start_ts::date BETWEEN '2017-11-01' AND '2017-11-07'
GROUP BY
    cabs.company_name;
-- Encuentra el número de viajes de Flash Cab y Taxi Affiliation Services
-- Encuentra el número de viajes de estas dos empresas y asigna a la variable resultante el nombre trips_amount. 
-- Junta los viajes de todas las demás empresas en el grupo "Other"
SELECT
    CASE
        WHEN cabs.company_name IN ('Flash Cab','Taxi Affiliation Services')
        THEN cabs.company_name
        ELSE 'Other'
        END AS Company,
    COUNT(trips.trip_id) AS trip_amaunt
FROM
    cabs 
    INNER JOIN trips ON trips.cab_id = cabs.cab_id
WHERE
   trips.start_ts::date BETWEEN '2017-11-01' AND '2017-11-07'
GROUP BY 
    company
ORDER BY 
    trip_amaunt DESC;

-- Recupera los identificadores de los barrios de O'Hare y Loop de la tabla neighborhoods.
SELECT
    neighborhood_id,
    name
FROM
    neighborhoods
WHERE
    name LIKE '%Hare' OR name LIKE 'Loop';

/*
Para cada hora recupera los registros de condiciones meteorológicas de la tabla weather_records. 
Usando el operador CASE, divide todas las horas en dos grupos: Bad si el campo description contiene las palabras rain o storm, y Good para los demás. 
Nombra el campo resultante weather_conditions. La tabla final debe incluir dos campos: fecha y hora (ts) y weather_conditions.
*/
SELECT
    ts,
    CASE
        WHEN description LIKE '%rain%' THEN 'Bad'
        WHEN description LIKE '%storm%' THEN 'Bad'
        ELSE 'Good'
        END AS weather_conditions
FROM
    weather_records;

/*
Recupera de la tabla de trips todos los viajes que comenzaron en el Loop (pickup_location_id: 50) el sábado y terminaron en O'Hare (dropoff_location_id: 63). 
Obtén las condiciones climáticas para cada viaje. 
Utiliza el método que aplicaste en la tarea anterior. Recupera también la duración de cada viaje. 
Ignora los viajes para los que no hay datos disponibles sobre las condiciones climáticas.
*/

SELECT
    trips.start_ts,
    CASE
        WHEN weather_records.description LIKE '%rain%' THEN 'Bad'
        WHEN weather_records.description LIKE '%storm%' THEN 'Bad'
        ELSE 'Good'
        END AS weather_conditions,
    trips.duration_seconds
FROM
    trips
    INNER JOIN weather_records ON weather_records.ts = trips.start_ts
WHERE
    trips.pickup_location_id = 50
    AND trips.dropoff_location_id = 63
    AND EXTRACT (DOW FROM trips.start_ts) = 6
ORDER BY
    trips.trip_id;

