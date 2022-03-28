from flask import Blueprint, render_template
from website.tvapi import *

views = Blueprint('views', __name__)


tv = webostv()

@views.route('/')
def home():
  currentVol = tv.get_audio_vol()
  current_ch = tv.channel
  return render_template("home.html", current_volume=currentVol, current_input=current_ch)

@views.route('/vol-down/')
def vol_down_clicked():
  tv.vol_down_clicked()
  currentVol = tv.get_audio_vol()
  return render_template("home.html", current_volume=currentVol, Muted='')

@views.route('/vol-up/')
def vol_up_clicked():
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
  tv.netflix_clicked()
  return render_template("home.html")

@views.route('/youtube/')
def youtube_clicked():
  tv.youtube_clicked()
  return render_template("home.html")

@views.route('/power/')
def power_clicked():
  tv.power_clicked()
  return render_template("home.html")

@views.route('/play/')
def play_clicked():
  tv.play_clicked()
  return render_template("home.html")

@views.route('/pause/')
def pause_clicked():
  tv.pause_clicked()
  return render_template("home.html")

@views.route('/rewind/')
def rewind_clicked():
  tv.rewind_clicked()
  return render_template("home.html")

@views.route('/fast-forward/')
def fastforward_clicked():
  tv.forward_clicked()
  return render_template("home.html")

@views.route('/inputs/')
def inputs_clicked():
  tv.inputs_clicked()
  current_ch = webostv().channel
  return render_template("home.html", current_input=current_ch)


@views.route('/chup/')
def channel_up():
  tv.channel_up()
  current_ch = webostv().channel
  return render_template("home.html", current_input=current_ch)


@views.route('/chdown/')
def channel_down():
  tv.channel_down()
  current_ch = webostv().channel
  return render_template("home.html", current_input=current_ch)


@views.route('/ch1/')
def ch1_clicked():
  tv.toCable()
  tv.channel_num_clicked(1)
  current_ch = webostv().channel
  return render_template("home.html", current_input=current_ch)


@views.route('/ch2/')
def ch2_clicked():
  tv.toCable()
  tv.channel_num_clicked(2)
  current_input = webostv().channel
  return render_template("home.html", current_input=current_input)