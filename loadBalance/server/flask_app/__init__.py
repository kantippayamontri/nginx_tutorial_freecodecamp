from flask import Flask

def create_app(suffix=""):

    app = Flask(__name__)

    @app.route("/")
    def home():
        return f"This is Flask. Server {suffix}"

    return app

