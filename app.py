from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
import os

#init app

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
     return jsonify({'msg':'hello World'})

if __name__ == '__main__':

  app.run(debug=True)