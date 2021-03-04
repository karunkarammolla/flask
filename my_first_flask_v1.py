from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy,request
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:aEzES_9wESCUhhJ4@devinstance.cmmaelkfp8je.ap-south-1.rds.amazonaws.com/medidata'
app.debug = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)



class movies(db.Model):
    __tablename__ = 'aggregated_scores'
    patient_visits_id = db.Column(db.Integer(),primary_key =True)
    points = db.Column(db.Integer())


    def __init__(self,patient_visits_id,points):
        self.patient_visits_id = patient_visits_id
        self.points = points




@app.route('/test', methods=['GET'])
def test():
    return 'my first trigger great oh yea!'


@app.route('/webapp_movies',methods = ['GET'])
def gmovies():
    all_movies = movies.query.all()
    output = []
    for movie in all_movies:

        currmovie={}
        currmovie['patient_visits_id'] = movie.patient_visits_id
        currmovie['points'] = movie.points

        output.append(currmovie)
    return jsonify(output)
