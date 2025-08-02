from flask import Flask
from .routes import user_bp
from .database import init_db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    init_db(app)
    app.register_blueprint(user_bp)

    @app.route("/", methods=["GET"])
    def home():
        return {"status": "User API running"}, 200

    return app
