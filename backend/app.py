from flask import Flask
from backend.config import Config
from backend.models import db
from backend.routes import admin_bp
from backend.routes.auth import auth_bp 
from backend.routes.upload import upload_bp 
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Register blueprints
app.register_blueprint(admin_bp)
app.register_blueprint(auth_bp) 
app.register_blueprint(upload_bp)
@app.route("/")
def home():
    return "DermaAgent Backend Running"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
