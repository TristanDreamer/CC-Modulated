from . import bp
from flask import render_template

@bp.route("/")
def root():
    return render_template("root.html")