from flask import Blueprint, render_template
import sys
sys.path.append('/Users/sun/Desktop/WebOSTV/')
from tvapi import webostv

views = Blueprint('views', __name__)

tv = webostv()


@views.route('/')
def home():
  currentVol = tv.get_audio_vol()
  current_ch = tv.get_app()
  if "com.webos.app." in current_ch:
    current_ch = current_ch[14:]
  elif "youtube" in current_ch:
    current_ch = "youtube" 
  current_chn = tv.displaychannel
  checkmute = webostv()
  if checkmute.isMute:
    return render_template("home.html", current_volume=currentVol, Muted="Muted", current_input=current_ch, current_channel=current_chn)
  else:
    return render_template("home.html", current_volume=currentVol, current_input=current_ch, current_channel=current_chn)


@views.route('/vol-down/')
def vol_down_clicked():
  tv.vol_down_clicked()
  return home()


@views.route('/vol-up/')
def vol_up_clicked():
  tv.vol_up_clicked()
  return home()


@views.route('/mute/')
def mute_clicked():
  webostv().mute_clicked()
  return home()


@views.route('/netflix/')
def netflix_clicked():
  tv.netflix_clicked()
  return home()


@views.route('/youtube/')
def youtube_clicked():
  tv.youtube_clicked()
  return home()


@views.route('/power/')
def power_clicked():
  tv.power_clicked()
  return home()


@views.route('/play/')
def play_clicked():
  tv.play_clicked()
  return home()


@views.route('/pause/')
def pause_clicked():
  tv.pause_clicked()
  return home()


@views.route('/rewind/')
def rewind_clicked():
  tv.rewind_clicked()
  return home()


@views.route('/fast-forward/')
def fastforward_clicked():
  tv.forward_clicked()
  return home()


@views.route('/inputs/')
def inputs_clicked():
  tv.inputs_clicked()
  return home()


@views.route('/chup/')
def channel_up():
  tv.channel_up()
  return home()


@views.route('/chdown/')
def channel_down():
  tv.channel_down()
  return home()


@views.route('/ch1/')
def ch1_clicked():
  tv.channel_num_clicked("1")
  return home()


@views.route('/ch2/')
def ch2_clicked():
  tv.channel_num_clicked("2")
  return home()


@views.route('/ch3/')
def ch3_clicked():
  tv.channel_num_clicked("3")
  return home()


@views.route('/ch4/')
def ch4_clicked():
  tv.channel_num_clicked("4")
  return home()


@views.route('/ch5/')
def ch5_clicked():
  tv.channel_num_clicked("5")
  return home()


@views.route('/ch6/')
def ch6_clicked():
  tv.channel_num_clicked("6")
  return home()


@views.route('/ch7/')
def ch7_clicked():
  tv.channel_num_clicked("7")
  return home()


@views.route('/ch8/')
def ch8_clicked():
  tv.channel_num_clicked("8")
  return home()


@views.route('/ch9/')
def ch9_clicked():
  tv.channel_num_clicked("9")
  return home()


@views.route('/ch0/')
def ch0_clicked():
  tv.channel_num_clicked("0")
  return home()