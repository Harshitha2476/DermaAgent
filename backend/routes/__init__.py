from flask import Blueprint, jsonify, request
from backend.models import db, User, Analysis, ModelInfo

# Blueprint with prefix
admin_bp = Blueprint("admin", __name__, url_prefix="/api/admin")

# Dashboard summary
@admin_bp.route("/dashboard", methods=["GET"])
def dashboard():
    return jsonify({
        "total_users": User.query.count(),
        "total_analyses": Analysis.query.count(),
        "total_models": ModelInfo.query.count()
    })

# Users
@admin_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{
        "id": u.id,
        "name": u.name,
        "email": u.email,
        "role": u.role,
        "created_at": u.created_at
    } for u in users])

@admin_bp.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    new_user = User(
        name=data.get("name"),
        email=data.get("email"),
        password_hash=data.get("password_hash"),
        role=data.get("role", "user")
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

# Analyses
@admin_bp.route("/analyses", methods=["GET"])
def get_analyses():
    analyses = Analysis.query.all()
    return jsonify([{
        "id": a.id,
        "user_id": a.user_id,
        "image_path": a.image_path,
        "predicted_class": a.predicted_class,
        "confidence": a.confidence,
        "status": a.status,
        "created_at": a.created_at
    } for a in analyses])

# Models
@admin_bp.route("/models", methods=["GET"])
def get_models():
    models = ModelInfo.query.all()
    return jsonify([{
        "id": m.id,
        "model_name": m.model_name,
        "model_version": m.model_version,
        "dataset_type": m.dataset_type,
        "accuracy": m.accuracy,
        "precision": m.precision,
        "recall": m.recall,
        "f1_score": m.f1_score,
        "created_at": m.created_at
    } for m in models])
