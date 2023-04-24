from flask import (
    Blueprint, render_template, request)
from cst.auth import  login_required


bp = Blueprint('search', __name__)

@bp.route('/')
def index():
    return render_template('search/index.html')

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    # Save information about the current selection to DB
    return render_template('search/create.html')
