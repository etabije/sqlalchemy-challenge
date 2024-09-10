# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Precipitation Route <br/>"
        f"Stations Route <br/>"
        f"Tobs Route <br/>"
       )

@app.route('/api/v1.0/precipitation')
def precipitation():
    one_year_ago = datetime.now() - timedelta(days=365)
    results = Measurement.query.filter(Measurement.date >= one_year_ago).all()
    precipitation_data = {result.date.strftime('%Y-%m-%d'): result.prcp for result in results if result.prcp is not None}
    return jsonify(precipitation_data)     


@app.route('/api/v1.0/stations')
def stations():
    results = Station.query.all()
    stations_data = {station.id: station.name for station in results} 
    return jsonify(stations_data)