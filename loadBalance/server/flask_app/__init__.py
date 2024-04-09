from flask import Flask

def create_app(servername=""):

    app = Flask(__name__)

    @app.route("/")
    def home():
        return f"This is Flask. Server {servername}"

    return app