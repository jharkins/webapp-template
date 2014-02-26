from webapp import app, lm, login_required, login_user, current_user, \
    logout_user

import logging

from flask import render_template, url_for, redirect, flash, \
    request, g, session

from lib.db import db, User

# Flash levels - send a meessage to the user with:
#   success, info, warning, danger

log = logging.getLogger(__name__)

lm.login_view = "log_in"
lm.login_message_category = "danger"


@lm.user_loader
def load_user(userid):
    return User.query.get(userid)


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    # If the user is logged in, don't let them register
    if 'user' in g and g.user.is_authenticated():
        return redirect(url_for('secured_area'))

    from lib.forms.registration_form import RegistrationForm
    form = RegistrationForm()

    if form.validate_on_submit():
        log.debug("valid form, registering user")

        # Create a new user
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash("Logged in successfully.", 'success')
        return redirect(request.args.get("next") or url_for("secured_area"))

    return render_template('register.html', form=form)


@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    from lib.forms.login_form import LoginForm
    log.debug("log_in route")

    # If the user is logged in, don't relog them in.
    if 'user' in g and g.user.is_authenticated():
        return redirect(url_for('secured_area'))

    form = LoginForm()

    if form.validate_on_submit():
        log.debug("valid form, logging in")
        user = User.query.filter(User.email == form.email.data).first()

        remember_me = False

        if 'remember_me' in session:
            remember_me = session['remember_me']
            session.pop('remember_me', None)

        login_user(user, remember=remember_me)
        flash("Logged in successfully.", 'success')
        return redirect(request.args.get("next") or url_for("secured_area"))

    return render_template('log_in.html', form=form)


@app.route('/secure')
@login_required
def secured_area():
    return render_template('secured.html')


@app.route('/log_out')
@login_required
def log_out():
    logout_user()
    flash('Log out complete.', 'success')
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e), 404
