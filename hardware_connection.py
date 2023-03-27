from flask import Flask, request
from controllers.hw_controllers import is_registered, insert_data

app = Flask(__name__)
app.secret_key = "34565465465465"


@app.route("/")
def on_request():
    rf_id = request.args.get("rfid")
    response = is_registered(rf_id=rf_id)
    if response:
        insert_data(rf_id=rf_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
