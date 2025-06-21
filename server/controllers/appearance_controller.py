from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models import Appearance, Guest, Episode
from server.extensions import db

appearance_bp = Blueprint('appearance', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()

    rating = data.get("rating")
    guest_id = data.get("guest_id")
    episode_id = data.get("episode_id")

    if not (1 <= rating <= 5):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    guest = Guest.query.get(guest_id)
    episode = Episode.query.get(episode_id)

    if not guest or not episode:
        return jsonify({"error": "Guest or Episode not found"}), 404

    appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    db.session.add(appearance)
    db.session.commit()

    return jsonify({
        "id": appearance.id,
        "rating": appearance.rating,
        "guest": {
            "id": guest.id,
            "name": guest.name
        },
        "episode": {
            "id": episode.id,
            "number": episode.number
        }
    }), 201
