from flask import Flask
from .routes import shortener_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(shortener_bp)

    @app.route("/health", methods=["GET"])
    def health_check():
        return {"status": "ok"}, 200

    return app
