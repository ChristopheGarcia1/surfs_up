import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

import app

print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")

app = Flask(__name__)
@app.route('/')
def welcome():
   return(
   '''
   Welcome to the Climate Analysis API! \n
   Available Routes: \n
   /api/v1.0/precipitation \n
   /api/v1.0/stations \n
   /api/v1.0/tobs \n
   /api/v1.0/temp/start/end \n
   ''')
