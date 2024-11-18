from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Configuration settings from .env file
app.config['SECRET_KEY'] = os.getenv('FLASK_APP_SECRET_KEY')  # Flask secret key
app.config['JWT_SECRET_KEY'] = os.getenv('FLASK_JWT_SECRET_KEY')  # JWT secret key
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable unnecessary signal tracking

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# User model with the updated fields
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_email_confirmed = db.Column(db.Boolean, default=False)  # Email confirmation status
    is_operation_user = db.Column(db.Boolean, default=False)   # Future role-based field

    def __repr__(self):
        return f"<User {self.username}>"

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Check if required parameters are provided
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({"msg": "Missing required parameters: username, email, and password are required."}), 400


    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check if username or email already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "Email already exists"}), 400

    # Hash the password before saving
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password=hashed_password)
    
    # Add the user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201

# Route to login and get a JWT token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Check if required parameters are provided
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"msg": "Missing required parameters: username and password are required."}), 400


    username = data.get('username')
    password = data.get('password')

    # Look for the user by username
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        # Create and return the JWT token
        access_token = create_access_token(identity=user.id)
        return jsonify({"msg": "Login successful", "access_token": access_token}), 200

    return jsonify({"msg": "Invalid username or password"}), 401


# Protected dashboard route (requires JWT token)
@app.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify({"msg": f"Welcome, {user.username}!"}), 200

# Run the Flask app
if __name__ == "__main__":
    # Create the database and tables (if they don't exist)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
