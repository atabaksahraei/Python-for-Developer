from app import api
from flask import Flask, escape, request, render_template

app = Flask(__name__, static_folder = "app/static/", template_folder='app/templates/')
app.register_blueprint(api.flurfunk.bp, url_prefix='/api/flurfunk')

@app.route("/")
def hello():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)}!"

@app.errorhandler(404)
@app.errorhandler(401)
def handle_all_error(err):
    return render_template("error.html", code=err.code, name=err.name, description=err.description)