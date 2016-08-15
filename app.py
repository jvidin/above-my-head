from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/radar'
db = SQLAlchemy(app)


class Radar(db.Model):
    __tablename__ = 'radar'
    id = db.Column(db.Integer, primary_key=True)
    squawk = db.Column(db.String(10))
    flight = db.Column(db.String(10))
    altitude = db.Column(db.String(10))
    lat = db.Column(db.String(10))
    lon = db.Column(db.String(10))


header = ['ID', 'FLIGHT', 'ALTITUDE', 'SQUAWK', 'LAT', 'LON']


@app.route('/')
def hello_world():
    return render_template('layout.html')

@app.route('/flight/')
def id_search():
    flight=request.args.get("flight")
    query = Radar.query.filter_by(flight=flight)
    return render_template('flight.html', query=query, header=header)

@app.route('/squawk/')
def squawk_search():
    squawk=request.args.get("squawk")
    query = Radar.query.filter_by(squawk=squawk)
    return render_template('squawk.html', query=query, header=header)

if __name__ == '__main__':
    app.run(debug=True)