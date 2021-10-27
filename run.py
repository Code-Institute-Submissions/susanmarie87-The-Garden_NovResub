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
DEVELOPMENT = True

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/events")
def events():
    """
    Returns events.html template
    """
    events = list(mongo.db.events.find())
    return render_template("events.html", events=events)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Allows user to register event.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return render_template("login.html")

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(
                request.form.get("password"), 'sha256')
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("login.html")


@app.route("/unregister_event", methods=["POST"])
def unregister_event():
    """
    Allows user to unregister their event.
    """
    if request.method == "POST":
        registration = {
            "username": session["user"],
            "event_id": request.form.get("event_id")
        }
        mongo.db.registration.delete_many(registration)
        flash("You're successfully unregistered!")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/delete_event", methods=["POST"])
def delete_event():
    """
    Allows user to delete an event
    """
    if request.method == "POST":
        event = {
            "username": session["user"],
            "_id": ObjectId(request.form.get("delete_event"))
        }
        mongo.db.events.delete_one(event)
        flash("You have deleted this event!")
    return redirect(url_for(
        "profile", username=session["user"]))


@app.route("/create_event", methods=["POST"])
def create_event():
    """
    Allows user to create an event
    """
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


@app.route("/open_edit_event", methods=["POST"])
def open_edit_event():
    """
    Returns edit event template
    """
    if request.method == "POST":
        event_filter = {
            "username": session["user"],
            "_id": ObjectId(request.form.get("open_edit_event"))
        }

        event = mongo.db.events.find_one(event_filter)

        return render_template(
            "edit_event.html", event=event)


@app.route("/edit_event", methods=["POST"])
def edit_event():
    """
    Allows user to edit their registered event details.
    """
    if request.method == "POST":
        event = {
            "username": session["user"],
            "_id": ObjectId(request.form.get("commit_edit_event")),
            "category_name": request.form.get("category_name"),
            "event_name": request.form.get("event_name"),
            "event_date": request.form.get("event_date"),
            "image": request.form.get("image")
        }

        event_filter = {
            "username": session["user"],
            "_id": ObjectId(request.form.get("commit_edit_event"))
        }
        mongo.db.events.replace_one(event_filter, event)
        flash("You have edited your event!")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Returns login page. Checks for existing username and password.
    """
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
                flash("Incorrect Username or Password")
                # return redirect(url_for("index"))
        else:
            # username doesn't exist
            flash("Incorrect Username or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Grabs the session user's username from db
    """
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
            {"username": session["user"]}))

        return render_template(
            "profile.html", username=username, events=events,
            my_events=my_events)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Logs User Out.
    """
    flash("You are logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/register_events", methods=["GET", "POST"])
def register_events():
    """
    Returns register page. ALlows user to create new account.
    """
    if not session.get("user", None):
        return redirect(url_for("login"))
    if request.method == "POST":
        registration = {
            "username": session["user"],
            "event_id": request.form.get("event_id")
        }
        mongo.db.registration.insert_one(registration)
        flash("You're successfully registered!")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/contact")
def contact():
    """
    Flashes succesful contact message to user
    """
    if request.method == "POST":
        flash("Thank you for contacting us, {}".format(
           request.form.get("name")))
    return render_template("contact.html")


@app.errorhandler(404)
def not_found(e):
    """
    On 400 error user will be oassed to custom error page.
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(err):
    """
    On 500 error user will be oassed to custom error page.
    """
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),)
