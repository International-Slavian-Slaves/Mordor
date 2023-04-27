from flask import Blueprint
from flask import render_template, url_for, request, redirect, flash
from flask_login import login_user, login_required
from controllers.controllers import get_hours, check_admin
from views.admin_login import AdminLogin
from views.forms import RF_IDForm, AdminForm

admin = Blueprint('admin', __name__, template_folder='..templates')


@admin.route("/login", methods=['GET', 'POST'])
def login_admin():
    """
    func for login as admin with the help of a post form
    """
    if request.method == "POST":
        user = check_admin(request.form['rf_id'])
        if user and user[0] == "11:11:11:11":
            userlogin = AdminLogin().create(user)
            login_user(userlogin)
            flash("Вы успешно авторизовались")
            return redirect(url_for("views.index"))
        else:
            flash("Попытка входа не удалась, попробуйте снова")
    return render_template("login.html", form=AdminForm())


@admin.route("/hours", methods=['GET', 'POST'])
@login_required
def get_month_time():
    """
    view for /hours route, returns month hours html
    """
    response = ""
    if request.method == 'POST':
        dict = request.form.to_dict()
        response = get_hours(dict['rf_id'])
    return render_template("month_times.html", form=RF_IDForm(), response=response)
