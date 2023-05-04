from flask import (
    Blueprint, render_template, request, session)
import json
from cst.db import get_db

bp = Blueprint('search', __name__)

@bp.route('/')
def index():
    return render_template('search/index.html')




@bp.route('/save-corpus', methods=['POST'])
def save_corpus():
    print('Save corpus')
    user = session['user_id']
    # Save information about the current selection (query and document set) to DB
    name = request.form['name']
    description = request.form['description']
    query = request.form['query']
    documents = request.form['documents']
    cursor = get_db().cursor()
    # TODO: exception handling
    cursor.execute(
                "INSERT INTO corpus (user_id, name, description) VALUES (?, ?, ?);",
                (user, name, description),
            )

    corpus_id = cursor.lastrowid
    get_db().commit()

    return f'Saved corpus as {name}'
    #except db.IntegrityError:
    #else:

