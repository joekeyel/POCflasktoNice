from flask import Flask ,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_19_6")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://TMIMS:Tm1m5u5R@127.0.0.1:1527/BQMDEV'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)

class Location(db.Model):
	__tablename__ = 'DC_LOCATION'
	id = db.Column('LOCN_ID', db.Integer, primary_key=True)
	name = db.Column('LOCN_NAME', db.Unicode)



class LocationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Location 
       


@app.route('/')
def index():
    result = Location.query.all()
    location_schema = LocationSchema(many=True)
    output = location_schema.dump(result)
    return jsonify({'location' : output})

if __name__ == '__main__':

  app.run(debug=True)