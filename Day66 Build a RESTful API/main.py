import sqlalchemy.sql.sqltypes
from werkzeug import exceptions
from flask import Flask, jsonify, render_template, request, json
from flask_sqlalchemy import SQLAlchemy
from random import choice, randint

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        """Creates a dictionary object of a record"""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    all_cafe = db.session.query(Cafe).all()
    random_cafe = choice(all_cafe)

    # Faster query
    # row_count = Cafe.query.count()
    # random_offset = randint(0, row_count - 1)
    # random_cafe = Cafe.query.offset(random_offset).first()
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafes():
    all_cafe = db.session.query(Cafe).all()
    return jsonify([cafe.to_dict() for cafe in all_cafe])


@app.route("/search")
def search_for_cafe():
    query_location = request.args.get("location")
    searched_cafes = db.session.query(Cafe).filter_by(location=query_location).all()
    if searched_cafes:
        if len(searched_cafes) < 1:
            # print(searched_cafes)
            return jsonify(searched_cafes.to_dict())
    # print(searched_cafes)
        return jsonify([cafe.to_dict() for cafe in searched_cafes])
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def add_cafe():

    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Added the new cafe!"})

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
