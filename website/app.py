from flask import Flask, render_template
from pylgtv import WebOsClient

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/vol-down/')
def vol_down_clicked():
    webos_client = WebOsClient('192.168.1.106')
    webos_client.volume_down()
    return render_template("home.html")

@app.route('/vol-up/')
def vol_up_clicked():
    webos_client = WebOsClient('192.168.1.106')
    webos_client.volume_up()
    return render_template("home.html")

@app.route('/netflix/')
def netflix_clicked():
    webos_client = WebOsClient('192.168.1.106')
    webos_client.launch_app("netflix")
    return render_template("home.html")

@app.route('/youtube/')
def youtube_clicked():
    webos_client = WebOsClient('192.168.1.106')
    webos_client.launch_app("youtube.leanback.v4")
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)