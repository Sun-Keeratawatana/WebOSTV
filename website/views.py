from flask import Blueprint, render_template
from website.tvapi import *

views = Blueprint('views', __name__)

@views.route('/')
def home():
  tv = webostv()
  currentVol = tv.get_audio_vol()
  current_input = tv.detectInput()
  return render_template("home.html", current_volume=currentVol, current_input=current_input)

@views.route('/vol-down/')
def vol_down_clicked():
  tv = webostv()
  tv.vol_down_clicked()
  currentVol = tv.get_audio_vol()
  return render_template("home.html", current_volume=currentVol, Muted='')

@views.route('/vol-up/')
def vol_up_clicked():
  tv = webostv()
  tv.vol_up_clicked()
  currentVol = tv.get_audio_vol()
  return render_template("home.html", current_volume=currentVol, Muted='')

@views.route('/mute/')
def mute_clicked():
  tv = webostv()
  tv.mute_clicked()
  currentVol = tv.get_audio_vol()
  checkmute = webostv()
  if checkmute.isMute:
    return render_template("home.html", current_volume=currentVol, Muted="Muted")
  else:
    return render_template("home.html", current_volume=currentVol)

@views.route('/netflix/')
def netflix_clicked():
  webostv().netflix_clicked()
  return render_template("home.html")

@views.route('/youtube/')
def youtube_clicked():
  webostv().youtube_clicked()
  return render_template("home.html")

@views.route('/power/')
def power_clicked():
  webostv().power_clicked()
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

@views.route('/inputs/')
def inputs_clicked():
  webostv().inputs_clicked()
  current_input = webostv().detectInput()
  return render_template("home.html", current_input=current_input)

