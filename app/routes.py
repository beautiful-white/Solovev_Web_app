from flask import Blueprint, render_template, request, redirect, url_for, make_response
from .database import get_db

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return redirect(url_for("main.login"))


@bp.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            conn = get_db()
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            conn.commit()
            conn.close()
            return redirect(url_for("main.login"))
        except Exception as e:
            error = "Пользователь уже существует"
    return render_template("register.html", error=error)


@bp.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        # SQLi
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        user = conn.execute(query).fetchone()
        conn.close()

        if user:
            response = make_response(redirect(url_for("main.hello")))
            response.set_cookie("username", username)
            return response
        else:
            error = "Неверный логин или пароль"
    return render_template("login.html", error=error)


@bp.route("/hello")
def hello():
    username = request.cookies.get("username")
    if not username:
        return redirect(url_for("main.login"))
    return render_template("hello.html", username=username)
