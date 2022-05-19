from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

"""Blogly application."""



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "HI"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False 
toolbar = DebugToolbarExtension(app)


connect_db(app)

@app.route('/')
def list():
    """shows pet page"""
   
    return redirect("/user")


@app.route('/user', methods=["GET"])
def list_users():
    """shows pet page"""
    users = User.query.all()
    return render_template('user/showuser.html', users=users)

@app.route('/user/newuser', methods=["GET"])
def open_create_user():
    

    return render_template("user/createnewuser.html")

@app.route('/user/newuser', methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    
    

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url or None)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/user')

@app.route("/user/<int:user_id>", methods=["GET"])
def show_user(user_id):
    """show details about single pet"""
    user = User.query.get_or_404(user_id)
    return render_template("user/userprofile.html", user=user, user_id=user_id)

@app.route("/user/<int:user_id>/edit", methods=["GET"])
def get_edit_user(user_id):

    user = User.query.get_or_404(user_id)

    return render_template('user/edit.html', user=user)



@app.route("/user/<int:user_id>/edit", methods=["POST"])
def post_edit_user(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()
    return redirect("/user")