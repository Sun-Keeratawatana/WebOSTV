from pylgtv import WebOsClient
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class connection(object):
    def __init__(self, ip, port=3000, key=None, timeout = 3):
        self.ip = ip
        self.port = port
        self.key = key
        self.tvClient = None
        self.timeout = timeout

    def connect(self):
        try:
            self.tvClient = WebOsClient(self.ip, timeout_connect=self.timeout)

        except:
            print("Error connecting to tv")
            sys.exit(0)

        return self.tvClient

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.channel = ""
        self.volume = ""
        self.isMute = False
        self.app = ""
        self.initUI()
        try:
            self.webos_client = connection('192.168.1.121').connect()
            self.label.setText("Connected")
        except:
            self.label.setText("Failed")

    def findChId(self, number):
        for channel in self.webos_client.get_channels():
            if(channel["channelNumber"] == number):
                return channel["channelId"]

    def detectInput(self):
        if"livetv" in self.webos_client.get_input():
            self.webos_client.launch_app(self.appid("hdmi1"))
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setText("hdmi1")

        elif "hdmi1" in self.webos_client.get_input():
            self.webos_client.launch_app(self.appid("hdmi2"))
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setText("hdmi2")

        elif "hdmi2" in self.webos_client.get_input():
            self.webos_client.launch_app(self.appid("hdmi3"))
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setText("hdmi3")

        else:
            self.webos_client.launch_app(self.appid("tv"))
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setText("TV")

    def channel_clicked(self):
        self.label.setText(self.channel)
        if((len(self.channel)) == 2):
            if(self.channel.startswith('0')):
                print("0")
                self.channel = self.channel[-1]
            try:
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setText(self.channel)
                self.webos_client.launch_app(self.appid("tv"))
                self.webos_client.set_channel(self.findChId(self.channel))
                print(self.channel)
                self.channel = ""

            except:
                print("Failed to complete the task")
                sys.exit(0)

        elif((len(self.channel)) > 2):
            self.channel = ""
            self.label.setText("")


    def one_clicked(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("1")
        self.channel = self.channel + "1"
        self.channel_clicked()

    def two_clicked(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("2")
        self.channel = self.channel + "2"
        self.channel_clicked()

    def three_clicked(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("3")
        self.channel = self.channel + "3"
        self.channel_clicked()

    def four_clicked(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("4")
        self.channel = self.channel + "4"
        self.channel_clicked()

    def five_clicked(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("5")
        self.channel = self.channel + "5"
        self.channel_clicked()

    def six_clicked(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("6")
        self.channel = self.channel + "6"
        self.channel_clicked()

    def seven_clicked(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("7")
        self.channel = self.channel + "7"
        self.channel_clicked()

    def eight_clicked(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("8")
        self.channel = self.channel + "8"
        self.channel_clicked()

    def nine_clicked(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("9")
        self.channel = self.channel + "9"
        self.channel_clicked()

    def zero_clicked(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("0")
        self.channel = self.channel + "0"
        self.channel_clicked()

    def list_clicked(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("List")
        try:
            self.webos_client.launch_app(self.appid("list"))
        except:
            print("Failed to complete the task")
            sys.exit(0)

    def guide_clicked(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Guide")
        try:
            self.webos_client.launch_app(self.appid("guide"))
        except:
            print("Failed to complete the task")
            sys.exit(0)

    def netflix_clicked(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Netflix")
        try:
            self.webos_client.launch_app(self.appid("netflix"))
        except:
            print("Failed to complete the task")
            sys.exit(0)
    
    def youtube_clicked(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Youtube")
        try:
            self.webos_client.launch_app(self.appid("youtube"))
        except:
            print("Failed to complete the task")
            sys.exit(0)

    def twitch_clicked(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Twitch")
        try:
            self.webos_client.launch_app(self.appid("twitch"))
        except:
            print("Exception on launching twitch")

    def volup_clicked(self):
        #self.label.setText("Volume Up")
        try:
            self.webos_client.volume_up()
            self.vol_label.setAlignment(QtCore.Qt.AlignCenter)
            self.volume = "Audio: " + str(self.webos_client.get_volume())
            self.vol_label.setText(self.volume)
        except:
            print("Failed to complete the task")
            sys.exit(0)
    
    def voldown_clicked(self):
        #self.label.setText("Volume Down")
        try:
            self.webos_client.volume_down()
            self.vol_label.setAlignment(QtCore.Qt.AlignCenter)
            self.vol_label.setText(str(self.webos_client.get_volume()))
            self.volume = "Audio: " + str(self.webos_client.get_volume())
            self.vol_label.setText(self.volume)
        except:
            print("Failed to complete the task")
            sys.exit(0)

    def chup_clicked(self):
        #self.label.setText("Channel Up")
        try:
            self.webos_client.launch_app(self.appid("tv"))
            self.webos_client.channel_up()
            self.channel = self.webos_client.get_current_channel()["channelNumber"]
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setText(self.channel)
        except:
            print("Failed to complete the task")
            sys.exit(0)
    
    def chdown_clicked(self):
        #self.label.setText("Channel Down")
        try:
            self.webos_client.launch_app(self.appid("tv"))
            self.webos_client.channel_down()
            self.channel = self.webos_client.get_current_channel()["channelNumber"]
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setText(self.channel)
        except:
            print("Failed to complete the task")
            sys.exit(0)

    def mute_clicked(self):
        self.isMute = self.webos_client.get_muted()
        if self.isMute:
            self.webos_client.set_mute(False)
        else:
            self.webos_client.set_mute(True)
    
    def power_clicked(self):
        self.webos_client.power_off()

    def pause_clicked(self):
        self.webos_client.pause()
    
    def play_clicked(self):
        self.webos_client.play()

    def rewind_clicked(self):
        self.webos_client.rewind()
    
    def forward_clicked(self):
        self.webos_client.fast_forward()

    def appid(self, x):

        if x == "netflix":
            return "netflix"
        
        elif x == "amazon":
            return "amazon"
        
        elif x == "guide":
            return "com.webos.app.tvuserguide"
        
        elif x == "appletv":
            return "com.apple.appletv"
        
        elif x == "youtube":
            return "youtube.leanback.v4"
        
        elif x == "twitch":
            return "tv.twitch.tv.starshot.lg"

        elif x == "tv":
            return "com.webos.app.livetv"

        elif x == "list":
            return "com.webos.app.livemenu"

        elif x == "hdmi1":
            return "com.webos.app.hdmi1"
        
        elif x == "hdmi2":
            return "com.webos.app.hdmi2"

        elif x == "hdmi3":
            return "com.webos.app.hdmi3"
# id:com.webos.app.livetv, netflix, doonung, lgtv-hbogoasia1, amazon, com.viu.tv, com.webos.app.notificationcenter, 
# com.webos.app.remoteservice, com.webos.app.accessibility, com.webos.app.livemenu, com.webos.app.miracast
# com.webos.app.scheduler, com.webos.app.recordings, com.webos.app.photovideo, com.webos.app.music, com.webos.app.btspeakerapp
# com.webos.app.connectionwizard, com.webos.app.tvuserguide, com.webos.app.browser, com.xstars.app.aquarelax, com.webos.app.hdmi2
# com.webos.app.hdmi3, spotify-beehive, youtube.leanback.v4, airplay, com.webos.app.discover, tv.twitch.tv.starshot.lg
# com.apple.appletv

    def initUI(self):
        
        self.setGeometry(0, 0, 300, 1000)
        self.setWindowTitle("Remote")
        self.setStyleSheet("background-color: white")

        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFont(QFont("Times", 20))
        self.label.setText("Status Label")
        #self.label.setStyleSheet("background-color: black")
        self.label.setGeometry(0,850,300,50)

        self.vol_label = QtWidgets.QLabel(self)
        self.vol_label.setAlignment(QtCore.Qt.AlignCenter)
        self.vol_label.setFont(QFont("Times", 20))
        self.vol_label.setGeometry(0,900,300,50)

        self.bPower = QtWidgets.QPushButton(self)
        self.bPower.setGeometry(20,0,90,90)
        self.bPower.setStyleSheet("border-radius : 10px; background-image : url(images/power.png);")
        self.bPower.clicked.connect(self.power_clicked)

        
        self.bInput = QtWidgets.QPushButton(self)
        self.bInput.setGeometry(180,5,80,80)
        self.bInput.setStyleSheet("border-radius : 10px; background-image : url(images/input.png);")
        self.bInput.clicked.connect(self.detectInput)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setGeometry(0,100,80,80)
        self.b1.setText("1")
        self.b1.setFont(QFont('Ariel', 30))
        self.b1.clicked.connect(self.one_clicked)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setGeometry(100,100,80,80)
        self.b2.setText("2")
        self.b2.setFont(QFont('Ariel', 30))
        self.b2.clicked.connect(self.two_clicked)

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setGeometry(200,100,80,80)
        self.b3.setText("3")
        self.b3.setFont(QFont('Ariel', 30))
        #self.b3.setStyleSheet("background-color: black")
        self.b3.clicked.connect(self.three_clicked)

        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setGeometry(0,200,80,80)
        self.b4.setText("4")
        self.b4.setFont(QFont('Ariel', 30))
        self.b4.clicked.connect(self.four_clicked)

        self.b5 = QtWidgets.QPushButton(self)
        self.b5.setGeometry(100,200,80,80)
        self.b5.setText("5")
        self.b5.setFont(QFont('Ariel', 30))
        self.b5.clicked.connect(self.five_clicked)

        self.b6 = QtWidgets.QPushButton(self)
        self.b6.setGeometry(200,200,80,80)
        self.b6.setText("6")
        self.b6.setFont(QFont('Ariel', 30))
        self.b6.clicked.connect(self.six_clicked)

        self.b7 = QtWidgets.QPushButton(self)
        self.b7.setGeometry(0,300,80,80)
        self.b7.setText("7")
        self.b7.setFont(QFont('Ariel', 30))
        self.b7.clicked.connect(self.seven_clicked)

        self.b8 = QtWidgets.QPushButton(self)
        self.b8.setGeometry(100,300,80,80)
        self.b8.setText("8")
        self.b8.setFont(QFont('Ariel', 30))
        self.b8.clicked.connect(self.eight_clicked)

        self.b9 = QtWidgets.QPushButton(self)
        self.b9.setGeometry(200,300,80,80)
        self.b9.setText("9")
        self.b9.setFont(QFont('Ariel', 30))
        self.b9.clicked.connect(self.nine_clicked)

        self.blist = QtWidgets.QPushButton(self)
        self.blist.setGeometry(0,410,80,60)
        self.blist.setStyleSheet("border-radius : 10px; background-image : url(images/list.png);")
        self.blist.clicked.connect(self.list_clicked)

        self.b0 = QtWidgets.QPushButton(self)
        self.b0.setGeometry(100,400,80,80)
        self.b0.setText("0")
        self.b0.setFont(QFont('Ariel', 30))
        self.b0.clicked.connect(self.zero_clicked)

        self.bguide = QtWidgets.QPushButton(self)
        self.bguide.setGeometry(200,410,80,60)
        self.bguide.setStyleSheet("border-radius : 10px; background-image : url(images/guide.png);")
        self.bguide.clicked.connect(self.guide_clicked)

        self.bnetflix = QtWidgets.QPushButton(self)
        self.bnetflix.setGeometry(0,500,80,80)
        self.bnetflix.setStyleSheet("border-radius : 10px; background-image : url(images/adjnetflix.png);")
        self.bnetflix.clicked.connect(self.netflix_clicked)

        self.byoutube = QtWidgets.QPushButton(self)
        self.byoutube.setGeometry(100,500,80,80)
        self.byoutube.setStyleSheet("border-radius : 10px; background-image : url(images/adjyoutube.jpg);")
        self.byoutube.clicked.connect(self.youtube_clicked)

        self.btwitch = QtWidgets.QPushButton(self)
        self.btwitch.setGeometry(200,500,80,80)
        self.btwitch.setStyleSheet("border-radius : 10px; background-image : url(images/adjtwitch.png);")
        self.btwitch.clicked.connect(self.twitch_clicked)

        self.bvolup = QtWidgets.QPushButton(self)
        self.bvolup.setGeometry(15,600,55,55)
        self.bvolup.setStyleSheet("background-image : url(images/audioUp.jpg);")
        self.bvolup.clicked.connect(self.volup_clicked)

        self.bvoldown = QtWidgets.QPushButton(self)
        self.bvoldown.setGeometry(15,660,55,55)
        self.bvoldown.setStyleSheet("background-image : url(images/audioDown.jpg);")
        self.bvoldown.clicked.connect(self.voldown_clicked)

        self.bchup = QtWidgets.QPushButton(self)
        self.bchup.setGeometry(200,600,80,60)
        self.bchup.setStyleSheet("border-radius : 10px; background-image : url(images/up.png);")
        self.bchup.clicked.connect(self.chup_clicked)

        self.bchdown = QtWidgets.QPushButton(self)
        self.bchdown.setGeometry(200,660,85,60)
        self.bchdown.setStyleSheet("border-radius : 10px; background-image : url(images/down.png);")
        self.bchdown.clicked.connect(self.chdown_clicked)

        self.bMute = QtWidgets.QPushButton(self)
        self.bMute.setGeometry(100,630,55,55)
        self.bMute.setStyleSheet("background-image : url(images/audioMute.jpg);")
        self.bMute.clicked.connect(self.mute_clicked)

        self.brewind = QtWidgets.QPushButton(self)
        self.brewind.setGeometry(20,740,50,50)
        self.brewind.setStyleSheet("border-radius : 10px; background-image : url(images/rewind.png);")
        self.brewind.clicked.connect(self.rewind_clicked)

        self.bplay = QtWidgets.QPushButton(self)
        self.bplay.setGeometry(170,740,50,50)
        self.bplay.setStyleSheet("border-radius : 10px; background-image : url(images/play.png);")
        self.bplay.clicked.connect(self.play_clicked)

        self.bpause = QtWidgets.QPushButton(self)
        self.bpause.setGeometry(90,740,50,50)
        self.bpause.setStyleSheet("border-radius : 10px; background-image : url(images/pause.png);")
        self.bpause.clicked.connect(self.pause_clicked)

        self.bforward = QtWidgets.QPushButton(self)
        self.bforward.setGeometry(240,740,50,50)
        self.bforward.setStyleSheet("border-radius : 10px; background-image : url(images/ff.jpg);")
        self.bforward.clicked.connect(self.forward_clicked)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
