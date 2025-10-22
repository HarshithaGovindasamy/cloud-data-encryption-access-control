from werkzeug.security import generate_password_hash, check_password_hash

# simple access control using an in-memory user list
users = {
    "admin": generate_password_hash("admin123"),
    "harsha": generate_password_hash("securelove")
}

def authenticate(username, password):
    """Check if the provided credentials are valid"""
    if username in users and check_password_hash(users[username], password):
        return True
    return False