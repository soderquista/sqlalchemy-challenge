# sqlalchemy-challenge
Performed cllimate analysis about weather measurement data from weather stations located in Honolulu, Hawaii. Then, data hosted as a Flask API based on queries to relational database.
## API Routes: 

/api/v1.0/precipitation - JSON of dictionary from precipitation analysis.

/api/v1.0/stations - JSON list of stations from dataset.

/api/v1.0/tobs - JSON list of temperature observations (tobs) of most-active station from previous year.

/api/v1.0/<start> - dynamic route, JSON list of minimum, average, and maximum temperatures from start date, inclusive (format: YYYY-mm-dd)

/api/v1.0/<start>/<end> - dynamic route, JSON list of minimum, average, and maximum temperatures from start date to end date, inclusive (format: YYYY-mm-dd)
