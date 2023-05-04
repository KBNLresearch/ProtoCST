from flask import (
    Blueprint, render_template, request, session, jsonify)
from cst.auth import  login_required
from cst.db import get_db
import pandas as pd


bp = Blueprint('extract', __name__)

@bp.route('/mycorpora', methods=('GET', 'POST'))
@login_required
def overview():
    user = session['user_id']
    query = """SELECT corpus.id, corpus.name, corpus.description, corpus.created, COUNT(DISTINCT document_in_corpus.document_id) AS nDocuments
                FROM corpus 
                LEFT JOIN document_in_corpus ON corpus.id = document_in_corpus.corpus_id 
                WHERE user_id = ?
                GROUP BY corpus.id"""
    db = get_db()
    corpora = db.execute(query,(user,)).fetchall()
    return render_template('extract/overview.html', corpora = corpora)

