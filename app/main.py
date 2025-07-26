
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_socketio import SocketIO
import RPi.GPIO as GPIO

app = Flask(__name__)
app.secret_key = "ChangeMe"
socketio = SocketIO(app)

devices = {}
groups = {}
settings = {
    "ssid": "Cortana",
    "wlan_pw": "ChangeMe",
    "admin_user": "admin",
    "admin_pw": "ChangeMe"
}

@app.route("/")
def index():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("index.html", devices=devices, groups=groups, settings=settings)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == settings["admin_user"] and request.form["password"] == settings["admin_pw"]:
            session["logged_in"] = True
            return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/api/devices", methods=["GET", "POST"])
def api_devices():
    if request.method == "POST":
        data = request.json
        devices[data["name"]] = {
            "type": data["type"],
            "pin": data["pin"],
            "group": data.get("group"),
            "pwm": data.get("pwm", False),
            "state": False
        }
        return jsonify(success=True)
    return jsonify(list(devices.values()))

@app.route("/api/device/<name>", methods=["PATCH"])
def api_device_control(name):
    data = request.json
    device = devices[name]
    device['state'] = data['state']
    socketio.emit('status_update', {name: device})
    return jsonify(success=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=80)
