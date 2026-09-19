import os
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from backend.models import db, Analysis
from backend.services.model import predict_image   # NEW: ML service

upload_bp = Blueprint("upload", __name__, url_prefix="/api/upload")

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_bp.route("/image", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        # Run ML prediction
        prediction, confidence = predict_image(filepath)

        # Create new Analysis record
        user_id = request.form.get("user_id")  # pass user_id in form-data
        analysis = Analysis(
            user_id=user_id,
            image_path=filepath,
            predicted_class=prediction,
            confidence=confidence,
            status="completed"
        )
        db.session.add(analysis)
        db.session.commit()

        return jsonify({
            "message": "Image uploaded successfully",
            "analysis_id": analysis.id,
            "prediction": prediction,
            "confidence": confidence
        }), 201

    return jsonify({"error": "Invalid file type"}), 400
