from flask import Blueprint, jsonify
from server.models import Episode, Appearance, Guest
from flask_jwt_extended import jwt_required

episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        "id": e.id,
        "date": e.date.isoformat(),
        "number": e.number
    } for e in episodes]), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify({
        "id": episode.id,
        "date": episode.date.isoformat(),
        "number": episode.number,
        "appearances": [{
            "id": a.id,
            "rating": a.rating,
            "guest": {
                "id": a.guest.id,
                "name": a.guest.name,
                "occupation": a.guest.occupation
            }
        } for a in episode.appearances]
    }), 200

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    from server.extensions import db
    episode = Episode.query.get_or_404(id)

    db.session.delete(episode)
    db.session.commit()

    return {"message": f"Episode {id} deleted."}, 200
