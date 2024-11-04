from chalice import Blueprint
from chalicelib.utils.firebase_initializer import firebase_initializer

extra_routes_login = Blueprint(__name__)
firebase = firebase_initializer()

@extra_routes_login.route("/login", methods=["POST"])
def login_routes():
    
    try:
        body = extra_routes_login.current_request.json_body
        user = firebase.sign_in_with_email_and_password(
            email=body.get("email"), 
            password=body.get("password")
        )
        return user
    except Exception as e:
        return { "error": str(e) }