from flask import render_template

from flask_login import login_required

from app.main import bp
import app.main.models


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('main/index.html')


@bp.route('/forum/<topic_id>')
def topic(topic_id):
    pass


@bp.route('/thread/<thread_id>')
def thread(thread_id):
    pass


@login_required
@bp.route('/new_thread')
def new_thread():
    pass


@login_required
@bp.route('/new_comment')
def new_comment():
    pass
