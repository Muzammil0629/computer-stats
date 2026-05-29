from flask import Flask
import socket
import datetime
import shutil
import os

app = Flask(__name__)

@app.route("/")
def dashboard():
    total, used, free = shutil.disk_usage("/")
    return f"""
    <h1>Computer Stats Dashboard</h1>
    <p><b>Hostname:</b> {socket.gethostname()}</p>
    <p><b>Current Time:</b> {datetime.datetime.now()}</p>
    <p><b>Disk Total:</b> {total // (2**30)} GB</p>
    <p><b>Disk Used:</b> {used // (2**30)} GB</p>
    <p><b>Disk Free:</b> {free // (2**30)} GB</p>
    <p><b>Status:</b> Running from Docker on AWS EC2</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
