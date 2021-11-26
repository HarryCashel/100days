import sqlalchemy.sql.sqltypes
from werkzeug import exceptions
from flask import Flask, jsonify, render_template, request, json
from flask_sqlalchemy import SQLAlchemy
from random import choice, randint
import secrets

app = Flask(__name__)
secret_secret = secrets.token_hex()
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
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


## HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def add_cafe():
    try:
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
    except sqlalchemy.exc.IntegrityError:
        return jsonify(error={"Duplicate": "There is a cafe with that name already."}), 409


## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:coffee_id>", methods=["PATCH", "PUT", "POST"])
def update_price(coffee_id):
    try:
        coffee_to_update = Cafe.query.get(coffee_id)
        new_price = request.args.get("new-price")
        coffee_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"Success": "Successfully updated the price"}), 200
    except AttributeError:
        return jsonify(error={"Cafe not found": "Cannot update something that does not exist."}), 404


## HTTP DELETE - Delete Record


@app.route("/delete/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    auth = request.args.get("api-key")
    if auth == secret_secret:
        cafe_to_delete = Cafe.query.get(cafe_id)
        if cafe_to_delete:

            try:

                db.session.delete(cafe_to_delete)
                db.session.commit()
                return jsonify(response={"Success": "Successfully deleted cafe"}), 200
            # except AttributeError:
            #     return jsonify(error={"Cafe not found": "Cannot delete something that does not exist."}), 404
            except sqlalchemy.orm.exc.UnmappedInstanceError:
                return jsonify(error={"error": "Cannot delete something that does not exist."}), 404
        else:
            return jsonify(error={"error": "Cannot delete something that does not exist."}), 404
    else:
        return jsonify(error={"error": "Sorry you don't have permission. Make sure you have the correct api_key."}), 403


print(secret_secret)

if __name__ == '__main__':
    app.run(debug=True)
