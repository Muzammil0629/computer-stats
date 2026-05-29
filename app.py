from flask import Flask
import socket
import datetime
import shutil

app = Flask(__name__)

@app.route("/")
def dashboard():
    total, used, free = shutil.disk_usage("/")

    return f"""
    <html>
    <head>
        <title>Computer Stats Dashboard</title>
    </head>
    <body>
        <h1>Computer Stats Dashboard</h1>

        <p><b>Version:</b> 2.0</p>
        <p><b>Hostname:</b> {socket.gethostname()}</p>
        <p><b>Current Time:</b> {datetime.datetime.now()}</p>

        <p><b>Disk Total:</b> {total // (2**30)} GB</p>
        <p><b>Disk Used:</b> {used // (2**30)} GB</p>
        <p><b>Disk Free:</b> {free // (2**30)} GB</p>

        <p><b>Status:</b> Healthy</p>
        <p><b>Deployment:</b> Automated via GitHub Actions</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
