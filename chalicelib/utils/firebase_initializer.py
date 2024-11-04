import json
import pyrebase

from chalicelib.utils.ssm import get_credential

def firebase_initializer():
    cred = get_credential(parameter="firebase-client")
    firebase = pyrebase.initialize_app(json.loads(cred)).auth()
    return firebase