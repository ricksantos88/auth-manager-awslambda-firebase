from chalice import Chalice

from chalicelib.views.login import extra_routes_login
from chalicelib.views.signup import extra_routes_signup
from chalicelib.views.refresh_token import extra_routes_refresh_token

app = Chalice(app_name='auth-ms-serverless-lambda-python')

app.register_blueprint(extra_routes_signup)
app.register_blueprint(extra_routes_login)
app.register_blueprint(extra_routes_refresh_token)


@app.route('/')
def index():
    return {'app': 'running'}