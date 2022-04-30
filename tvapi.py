from pylgtv import WebOsClient
import sys

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


class webostv():
    def __init__(self):
        try:
            self.webos_client = connection('192.168.1.108').connect()
            #self.volume = self.webos_client.get_audio_status().get("volumeStatus")["volume"]
            self.volume = self.webos_client.get_audio_status().get("volume")
        except:
            sys.exit("Cannot connect to the tv")


        self.channel = ""
        self.displaychannel = ""
        self.isMute = self.webos_client.get_muted()
        
        self.app = ""
        
            
    def get_audio_vol(self):
        return self.volume

    def get_mute(self):
        return self.isMute

    def get_app(self):
        self.app = self.webos_client.get_current_app()
        return self.app

    def update_channel(self, ch):
        self.channel += ch
        return self.channel

# id:com.webos.app.livetv, netflix, doonung, lgtv-hbogoasia1, amazon, com.viu.tv, com.webos.app.notificationcenter, 
# com.webos.app.remoteservice, com.webos.app.accessibility, com.webos.app.livemenu, com.webos.app.miracast
# com.webos.app.scheduler, com.webos.app.recordings, com.webos.app.photovideo, com.webos.app.music, com.webos.app.btspeakerapp
# com.webos.app.connectionwizard, com.webos.app.tvuserguide, com.webos.app.browser, com.xstars.app.aquarelax, com.webos.app.hdmi2
# com.webos.app.hdmi3, spotify-beehive, youtube.leanback.v4, airplay, com.webos.app.discover, tv.twitch.tv.starshot.lg
# com.apple.appletv

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
    

    def findChId(self, number):
        for channel in self.webos_client.get_channels():
            if(channel["channelNumber"] == number):
                return channel["channelId"]


    def detectInput(self):
        if "livetv" in self.webos_client.get_input():
            return "livetv"

        elif "hdmi1" in self.webos_client.get_input():
            return "hdmi1"

        elif "hdmi2" in self.webos_client.get_input():
            return "hdmi2"

        else:
            return "hdmi3"


    def toCable(self):
        return self.webos_client.launch_app(self.appid("tv"))


    def inputs_clicked(self):
        print("input clicked")
        if self.detectInput() == "livetv":
            return self.webos_client.launch_app(self.appid("hdmi1"))
        elif self.detectInput() == "hdmi1":
            return self.webos_client.launch_app(self.appid("hdmi2"))
        elif self.detectInput() == "hdmi2":
            return self.webos_client.launch_app(self.appid("hdmi3"))
        else:
            return self.toCable()
            

    def channel_num_clicked(self, num):
        self.channel += num
        print(self.channel)
        if len(self.channel) >= 2:
            if(self.channel.startswith('0')):
                self.channel = self.channel[1]
            self.webos_client.set_channel(self.findChId(self.channel))
            self.displaychannel = self.channel
            self.channel = ""
        return

    
        
    def power_clicked(self):
        print("power clicked")
        return self.webos_client.power_off()


    def pause_clicked(self):
        print("pause clicked")
        return self.webos_client.pause()


    def play_clicked(self):
        print("play clicked")
        return self.webos_client.play()


    def rewind_clicked(self):
        print("rewind clicked")
        return self.webos_client.rewind()


    def forward_clicked(self):
        print("forward clicked")
        return self.webos_client.fast_forward()


    def youtube_clicked(self):
        print("youtube clicked")
        return self.webos_client.launch_app(self.appid("youtube"))


    def netflix_clicked(self):
        print("netflix clicked")
        return self.webos_client.launch_app(self.appid("netflix"))


    def vol_up_clicked(self):
        print("vol_up clicked")
        self.volume += 1
        if self.volume >= 100:
            self.volume = 100
        return self.webos_client.volume_up()


    def vol_down_clicked(self):
        print("vol_down clicked")
        self.volume -= 1
        if self.volume <= 0:
            self.volume = 0
        return self.webos_client.volume_down()


    def mute_clicked(self):
        print("mute clicked")
        if self.isMute:
            return self.webos_client.set_mute(False)
        else:
            return self.webos_client.set_mute(True)

    def channel_up(self):
        print("ch_up clicked")
        self.webos_client.launch_app(self.appid("tv"))
        return self.webos_client.channel_up()

    def channel_down(self):
        print("ch_down clicked")
        self.webos_client.launch_app(self.appid("tv"))
        return self.webos_client.channel_down()
