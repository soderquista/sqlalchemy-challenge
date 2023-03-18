from flask import Flask, jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.sql import text

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn = engine.connect()
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
# Save reference to the table
measurements = Base.classes.measurement
Stations = Base.classes.station

app = Flask(__name__)

@app.route("/")
def home():
    print("Server received request for 'Home' page")
    return (f"This is the homepage for the query results of precipitation analysis. <br/>"
            f"Available Routes: <br/>"
            f"/api/v1.0/precipitation <br/>"
            f"/api/v1.0/stations <br/>"
            f"/api/v1.0/tobs <br/>"
            f"/api/v1.0/<start> or /api/v1.0/<start>/<end> for date range: Calculate the min, avg, and max temperature for the specified date range (date format: YYYY-mm-dd).")

@app.route("/api/v1.0/precipitation")
def precip():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a dict of dates and relative prcp from SQLite database"""
    # Query
    results = session.query(measurements.date,measurements.prcp).filter(measurements.date >= '2016-08-23')
    session.close()
    prcp_data_dict = {'date':'name'}
    # Create a dictionary from the row data
    for date, prcp in results:
        prcp_data_dict[date] = prcp

    return jsonify(prcp_data_dict)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    
    # Query
    results = session.query(Stations.station).distinct()
    session.close()
    lst = []
    for Row in results:
        lst.append(Row.station)
    return jsonify(lst)

@app.route("/api/v1.0/tobs")
def Tobs():
    session = Session(engine)
    
    # Query
    results = session.query(measurements.tobs).filter_by(station='USC00519397').filter(measurements.date >= '2016-08-23')
    session.close()
    lst = []
    for Row in results:
        lst.append(Row.tobs)
    return jsonify(lst)

@app.route("/api/v1.0/<start>")
def vardate(start):
    session = Session(engine)
    
    # Query
    results = session.query(measurements.tobs).filter(measurements.date >= start)
    session.close()
    lst = []
    for Row in results:
        lst.append(Row.tobs)
    TAVG = sum(lst)/len(lst)
    TMIN = min(lst)
    TMAX = max(lst)
    return jsonify([TMIN, TAVG, TMAX])

@app.route("/api/v1.0/<start>/<end>")
def vardates(start, end):
    session = Session(engine)
    
    # Query
    results = session.query(measurements.tobs).filter(measurements.date >= start).filter(measurements.date <= end)
    session.close()
    lst = []
    for Row in results:
        lst.append(Row.tobs)
    TAVG = sum(lst)/len(lst)
    TMIN = min(lst)
    TMAX = max(lst)
    return jsonify([TMIN, TAVG, TMAX])

if __name__ == '__main__':
    app.run(debug=True)
