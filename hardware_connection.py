from flask import Flask, request
from controllers.hw_controllers import is_registered

app = Flask(__name__)
app.secret_key = "34565465465465"


@app.route("/")
def on_request():
    return is_registered(rf_id=request.args.get("rfid"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
