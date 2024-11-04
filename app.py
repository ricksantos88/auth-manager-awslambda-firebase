from chalice import Chalice

app = Chalice(app_name='auth-ms-serverless-lambda-python')


@app.route('/')
def index():
    return {'hello': 'world'}
