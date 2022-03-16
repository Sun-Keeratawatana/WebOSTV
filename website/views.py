from flask import Blueprint, render_template
from pylgtv import WebOsClient
from tvapi import *

views = Blueprint('views', __name__)

@views.route('/')
def home():
  webos_client = WebOsClient('192.168.1.108')
  currentVol = webos_client.get_audio_status().get("volumeStatus")["volume"]
  return render_template("home.html", current_volume=currentVol)

@views.route('/vol-down/')
def vol_down_clicked():
  webos_client = WebOsClient('192.168.1.108')
  webos_client.volume_down()
  currentVol = webos_client.get_audio_status().get("volumeStatus")["volume"]
  return render_template("home.html", current_volume=currentVol)

@views.route('/vol-up/')
def vol_up_clicked():
  webos_client = WebOsClient('192.168.1.108')
  webos_client.volume_up()
  currentVol = webos_client.get_audio_status().get("volumeStatus")["volume"]
  return render_template("home.html", current_volume=currentVol)

@views.route('/netflix/')
def netflix_clicked():
  webos_client = WebOsClient('192.168.1.108')
  webos_client.launch_app("netflix")
  return render_template("home.html")

@views.route('/youtube/')
def youtube_clicked():
  webos_client = WebOsClient('192.168.1.108')
  webos_client.launch_app("youtube.leanback.v4")
  return render_template("home.html")

@views.route('/power/')
def power_clicked():
  webos_client = WebOsClient('192.168.1.108')
  webos_client.power_off()
  return render_template("home.html")

@views.route('/play/')
def play_clicked():
  webostv().play_clicked()
  return render_template("home.html")

@views.route('/pause/')
def pause_clicked():
  webostv().pause_clicked()
  return render_template("home.html")

@views.route('/rewind/')
def rewind_clicked():
  webostv().rewind_clicked()
  return render_template("home.html")

@views.route('/fast-forward/')
def fastforward_clicked():
  webostv().forward_clicked()
  return render_template("home.html")
