# Project Description

You are working as an analyst for Zuber, a new ridesharing company launching in Chicago. Your task is to find patterns in the available information. You aim to understand passenger preferences and the impact of external factors on trips.

Working with a database, you will analyze competitor data and test a hypothesis about the impact of weather on trip frequency.

## Data Description

A database containing information about taxi trips in Chicago:

Neighborhoods table: Data about city neighborhoods

name: neighborhood name
neighborhood_id: neighborhood code
Cabs table: Data about taxis

cab_id: vehicle code
vehicle_id: technical ID of the vehicle
company_name: owning company of the vehicle
Trips table: Data about trips

trip_id: trip code
cab_id: vehicle code operating the trip
start_ts: date and time of trip start (time rounded to the hour)
end_ts: date and time of trip end (time rounded to the hour)
duration_seconds: trip duration in seconds
distance_miles: trip distance in miles
pickup_location_id: pickup neighborhood code
dropoff_location_id: dropoff neighborhood code
Weather Records table: Data about weather

record_id: weather record code
ts: date and time of record (time rounded to the hour)
temperature: temperature when the record was taken
description: brief description of weather conditions, e.g., "light rain" or "scattered clouds"
