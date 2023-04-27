from flask import Flask, render_template
from flask_login import LoginManager
from views.admin_login import AdminLogin
from views.admin_view import admin
from views.views import views
from config import WSGI1_KEY

app = Flask(__name__)
app.secret_key = WSGI1_KEY
app.register_blueprint(views)
app.register_blueprint(admin)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return AdminLogin().get_data(user_id)


@app.errorhandler(404)
def handle404(error):
    """
    error 404 handler
    """
    return render_template("not_found.html")


@app.errorhandler(401)
def handle401(error):
    """
    error 401 handler
    """
    return render_template("unauthorized.html")
