from .database import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(data):
    hashed_password = generate_password_hash(data["password"])
    user = User(name=data["name"], email=data["email"], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return user

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def update_user(user_id, data):
    user = User.query.get(user_id)
    if not user:
        return None
    if "name" in data:
        user.name = data["name"]
    if "email" in data:
        user.email = data["email"]
    if "password" in data:
        user.password = generate_password_hash(data["password"])
    db.session.commit()
    return user

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return False
    db.session.delete(user)
    db.session.commit()
    return True

def search_users_by_name(name):
    return User.query.filter(User.name.ilike(f"%{name}%")).all()

def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return user
    return None
