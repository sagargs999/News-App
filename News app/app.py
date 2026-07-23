import os
import requests
from flask import Flask, render_template, request
from models import db, Bookmark, User
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask import request, redirect, url_for
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = "your_super_secret_key_123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///news.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))
    
API_KEY = os.getenv("NEWS_API_KEY")
print("API KEY FROM ENV:", repr(API_KEY))

@app.route("/")
def home():

    search = request.args.get("search")
    country = request.args.get("country", "us")
    print("Country:", country)
    category = request.args.get("category")

    if search:

        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={search}&apiKey={API_KEY}"
        )
    else:

      url = (
         f"https://newsapi.org/v2/top-headlines?"
         f"country={country}"
      )

    if category:
        url += f"&category={category}"

    url += f"&apiKey={API_KEY}"
    response = requests.get(url)
    print(url)
    data = response.json()
    
    print(data)

    articles = data.get("articles", [])

    return render_template(
        "index.html",
        articles=articles,
        country=country
    )

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")

        email = request.form.get("email")

        password = generate_password_hash(
            request.form.get("password")
        )

        user = User(
            username=username,
            email=email,
            password=password
        )

        db.session.add(user)

        db.session.commit()

        return redirect(url_for("home"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            login_user(user)

            return redirect(url_for("home"))
        return "Invalid email or password"
        

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("home"))

 

@app.route("/bookmarks")
@login_required
def bookmarks():

    articles = Bookmark.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "bookmarks.html",
        articles=articles
    )


@app.route("/bookmark", methods=["POST"])
@login_required
def bookmark():

    title = request.form.get("title")
    description = request.form.get("description")
    image = request.form.get("image")
    url = request.form.get("url")

    # Check if this article is already bookmarked by this user
    existing = Bookmark.query.filter_by(
        user_id=current_user.id,
        url=url
    ).first()

    if existing:
        return redirect(url_for("bookmarks"))

    bookmark = Bookmark(
        title=title,
        description=description,
        image=image,
        url=url,
        user_id=current_user.id
    )

    db.session.add(bookmark)
    db.session.commit()

    return redirect(url_for("bookmarks"))

@app.route("/delete_bookmark/<int:id>", methods=["POST"])
@login_required
def delete_bookmark(id):

    bookmark = Bookmark.query.get_or_404(id)

    # Make sure users can only delete their own bookmarks
    if bookmark.user_id != current_user.id:
        return "Unauthorized", 403

    db.session.delete(bookmark)
    db.session.commit()

    return redirect(url_for("bookmarks"))

if __name__ == "__main__":

    with app.app_context():
      db.create_all()

    app.run(debug=True)