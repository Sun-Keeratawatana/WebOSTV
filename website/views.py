from flask import Blueprint, render_template
import sys
sys.path.append('/Users/sun/Desktop/WebOSTV/')
from tvapi import webostv

views = Blueprint('views', __name__)

tv = webostv()

@views.route('/')
def home():
  currentVol = webostv().get_audio_vol()
  current_ch = webostv().get_app()
  return render_template("home.html", current_volume=currentVol, current_input=current_ch)

@views.route('/vol-down/')
def vol_down_clicked():
  webostv().vol_down_clicked()
  currentVol = webostv().get_audio_vol()
  return render_template("home.html", current_volume=currentVol, Muted='')

@views.route('/vol-up/')
def vol_up_clicked():
  webostv().vol_up_clicked()
  currentVol = webostv().get_audio_vol()
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
  current_ch = tv.get_app()
  return render_template("home.html", current_input = current_ch)

@views.route('/youtube/')
def youtube_clicked():
  tv.youtube_clicked()
  current_ch = tv.get_app()
  return render_template("home.html", current_input = current_ch)

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

@views.route('/ch3/')
def ch3_clicked():
  tv.toCable()
  tv.channel_num_clicked(3)
  current_ch = webostv().channel
  return render_template("home.html", current_input=current_ch)


@views.route('/ch4/')
def ch4_clicked():
  tv.toCable()
  tv.channel_num_clicked(4)
  current_input = webostv().channel
  return render_template("home.html", current_input=current_input)

@views.route('/ch5/')
def ch5_clicked():
  tv.toCable()
  tv.channel_num_clicked(5)
  current_ch = webostv().channel
  return render_template("home.html", current_input=current_ch)


@views.route('/ch6/')
def ch6_clicked():
  tv.toCable()
  tv.channel_num_clicked(6)
  current_input = webostv().channel
  return render_template("home.html", current_input=current_input)

@views.route('/ch7/')
def ch7_clicked():
  tv.toCable()
  tv.channel_num_clicked(7)
  current_ch = webostv().channel
  return render_template("home.html", current_input=current_ch)


@views.route('/ch8/')
def ch8_clicked():
  tv.toCable()
  tv.channel_num_clicked(8)
  current_input = webostv().channel
  return render_template("home.html", current_input=current_input)


@views.route('/ch9/')
def ch9_clicked():
  tv.toCable()
  tv.channel_num_clicked(9)
  current_ch = webostv().channel
  return render_template("home.html", current_input=current_ch)


@views.route('/ch0/')
def ch0_clicked():
  tv.toCable()
  tv.channel_num_clicked(0)
  current_input = webostv().channel
  return render_template("home.html", current_input=current_input)