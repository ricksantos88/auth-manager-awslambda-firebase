from chalice import Chalice

from chalicelib.views.login import extra_routes_login
from chalicelib.views.signup import extra_routes_signup

app = Chalice(app_name='auth-ms-serverless-lambda-python')

app.register_blueprint(extra_routes_signup)
app.register_blueprint(extra_routes_login)


@app.route('/')
def index():
    return {'app': 'running'}