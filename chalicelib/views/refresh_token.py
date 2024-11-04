from chalice import Blueprint
from chalicelib.utils.firebase_initializer import firebase_initializer

extra_routes_refresh_token = Blueprint(__name__)
firebase = firebase_initializer()

@extra_routes_refresh_token.route("/refresh-token", methods=["POST"])
def refresh_token_routes():
    
    try:
        body = extra_routes_refresh_token.current_request.json_body
        refreshed_token = firebase.refresh(refresh_token=body.get("refresh_token"))
        return refreshed_token
    except Exception as e:
        return { "error": str(e) }