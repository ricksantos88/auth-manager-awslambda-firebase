from chalice import Blueprint
from chalicelib.utils.firebase_initializer import firebase_initializer

extra_routes_signup = Blueprint(__name__)
firebase = firebase_initializer()

@extra_routes_signup.route("/signup", methods=["POST"])
def signup_routes():
    
    try:
        body = extra_routes_signup.current_request.json_body
        user = firebase.create_user_with_email_and_password(
            email=body.get("email"), 
            password=body.get("password")
        )
        return user
    except Exception as e:
        return { "error": str(e) }