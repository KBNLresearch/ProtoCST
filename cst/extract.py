from flask import (
    Blueprint, render_template, request, session, jsonify)
from cst.auth import  login_required
from cst.db import get_db
import pandas as pd


bp = Blueprint('extract', __name__)

@bp.route('/mycorpora', methods=('GET', 'POST'))
@login_required
def overview():
    user_id = session['user_id']
    query = """SELECT corpus.id, corpus.name, corpus.description, corpus.created, COUNT(DISTINCT document_in_corpus.document_id) AS nDocuments
                FROM corpus 
                LEFT JOIN document_in_corpus ON corpus.id = document_in_corpus.corpus_id 
                WHERE user_id = ?
                GROUP BY corpus.id"""
    db = get_db()
    corpora = db.execute(query,(user_id,)).fetchall()
    return render_template('extract/overview.html', corpora = corpora)

@bp.route('/extract-corpus', methods=('GET', 'POST'))
@login_required
def extract_corpus():
    corpus_id = request.args.get('corpus_id')
    query = """SELECT corpus.*, COUNT(DISTINCT document_in_corpus.document_id) AS nDocuments
                FROM corpus 
                LEFT JOIN document_in_corpus ON corpus.id = document_in_corpus.corpus_id 
                WHERE corpus.id = ?"""
    db = get_db()
    corpus = db.execute(query,(corpus_id,)).fetchone()
    return render_template('extract/export_options.html', corpus = corpus)
