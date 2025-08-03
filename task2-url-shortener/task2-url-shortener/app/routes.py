from flask import Blueprint, request, jsonify, redirect
from .services import shorten_url, get_redirect, get_stats

shortener_bp = Blueprint("shortener", __name__)

@shortener_bp.route("/api/shorten", methods=["POST"])
def api_shorten():
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    result, error = shorten_url(data["url"])
    if error:
        return jsonify({"error": error}), 400
    return jsonify(result), 201

@shortener_bp.route("/<short_code>", methods=["GET"])
def redirect_url(short_code):
    url = get_redirect(short_code)
    if not url:
        return jsonify({"error": "Short code not found"}), 404
    return redirect(url)

@shortener_bp.route("/api/stats/<short_code>", methods=["GET"])
def stats(short_code):
    data = get_stats(short_code)
    if not data:
        return jsonify({"error": "Short code not found"}), 404
    return jsonify(data)
