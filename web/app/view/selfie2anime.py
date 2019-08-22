# encoding: utf-8

from flask import Blueprint

bp = Blueprint('selfie2anime', __name__, url_prefix='/selfie2anime')


@bp.route('/')
def index():
    return 'Hello'
