import os
import json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/events")
def events():
    events = list(mongo.db.events.find())
        
    return render_template("events.html", events=events)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/unregister_event", methods=["POST"])
def unregister_event():
    if request.method == "POST":
        registration = {
            "username": session["user"],                                                                        
            "event_id": request.form.get("event_id")
        }
        mongo.db.registration.delete_many(registration)
        flash("You're successfully unregistered!")
    return redirect(url_for("profile", username=session ["user"]))


@app.route("/create_event", methods=["POST"])
def create_event():
    
    if request.method == "POST":
        event = {
            "username": session["user"],                                                                        

            "category_name": request.form.get("category_name"),
            "event_name": request.form.get("event_name"),
            "event_date": request.form.get("event_date"),
            "image": request.form.get("image")

        }
        mongo.db.events.insert_one(event)
        flash("You have Created a New Event!")
    return redirect(url_for("events"))



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check for existing username
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password 
                print("wrong password")
                flash("Incorrect Username or Password") 
                # return redirect(url_for("index"))
        else:
            # username doesn't exist
            flash("Incorrect Username or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        registrations = list(mongo.db.registration.find(
            {"username": session["user"]}, 
            {"event_id": 1}).distinct("event_id"))
        registrations = [ObjectId(event_id) for event_id in registrations]
        events = list(mongo.db.events.find(
            {"_id": {"$in": registrations}}))
        my_events = list(mongo.db.events.find(
            {"username": session["user"]})
            
        return render_template("profile.html", username=username, events=events)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():

    flash("You are logged out")
    session.pop("user")
    return redirect(url_for("login"))

"""
@app.route("/add_events", methods=["GET", "POST"])
def add_events():
    if request.method == "POST":
        "event"
"""

@app.route("/register_events", methods=["GET", "POST"]) 
def register_events(): 

    if request.method == "POST":
        registration = {
            "username": session["user"],                                                                        
            "event_id": request.form.get("event_id")
        }
        mongo.db.registration.insert_one(registration)
        flash("You're successfully registered!")
    return redirect(url_for("profile", username=session ["user"]))


@app.route("/contact")
def contact():
    if request.method == "POST":
       flash("Thank you for contacting us, {}".format(
           request.form.get("name")))
    return render_template("contact.html")
    

"""""
 @app.errorhandler(404)
 def page_not_found(e):
     404 error brings user to error page

     return render_template('pages/404.html'), 404

# @app.errohandler(500)
# def internal_error(err):
    # 500 error brings user to error page

    # return render_template('pages/500.html'), 500
"""    


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True) 
        