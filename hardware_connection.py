from flask import Flask, request
from controllers.hw_controllers import is_registered, insert_data
from config import WSGI2_KEY

app = Flask(__name__)
app.secret_key = WSGI2_KEY


@app.route("/")
def on_request():
    rf_id = request.args.get("rfid")
    response = is_registered(rf_id=rf_id)
    if response:
        insert_data(rf_id=rf_id)
    print(app.secret_key)
    return response
