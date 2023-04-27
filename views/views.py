from flask import Blueprint, render_template, request
from flask_login import login_required
from views.forms import RegistrationForm, LimitForm
from controllers.controllers import register_user, get_recent_passes, get_fun, get_locations

views = Blueprint('views', __name__, template_folder='..templates')



@views.route("/", methods=['GET', 'POST'])
@views.route("/index", methods=['GET', 'POST'])
@login_required
def index():
    """
    handler for routes / and /index
    returns index page with last passes
    """
    limit = 10
    if request.method == 'POST':
        limit = int(request.form['amount'])
    passes_data = get_recent_passes(limit)
    return render_template('index.html', passes_data=passes_data, form=LimitForm())


@views.route("/registration", methods=['GET', 'POST'])
@login_required
def registration():
    """
    view for registration, returns registration html
    adds user registration functional
    """
    if request.method == 'POST':
        request_data = request.form
        register_user(request_data)
    return render_template('registration.html', form=RegistrationForm())


@views.route("/fun")
@login_required
def kill_yourself():
    """
    fun for dropping db
    """
    msg, result = get_fun()
    return render_template("easter_result.html", msg=msg, result=result)


@views.route("/locations")
@login_required
def locate_users():
    """
    view mapped to /locations that returns all users locations html
    """
    location_data = get_locations()
    return render_template("locations.html", location_data=location_data)



