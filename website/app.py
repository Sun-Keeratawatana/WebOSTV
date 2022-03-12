from flask import Flask, render_template
from pylgtv import WebOsClient
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/my-link/')
def my_link():
    print("I got clicked!")
    webos_client = WebOsClient('192.168.1.106')
    #webos_client.launch_app('youtube.leanback.v4')
    webos_client.volume_down()
    return "Click."

if __name__ == "__main__":
    app.run(debug=True)