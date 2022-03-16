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
        self.channel = ""
        self.volume = ""
        self.isMute = False
        self.app = ""
        try:
            self.webos_client = connection('192.168.1.108').connect()
        except:
            print("Failed")

    #Converting into app id
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
            self.webos_client.launch_app(self.appid("hdmi1"))

        elif "hdmi1" in self.webos_client.get_input():
            self.webos_client.launch_app(self.appid("hdmi2"))

        elif "hdmi2" in self.webos_client.get_input():
            self.webos_client.launch_app(self.appid("hdmi3"))

        else:
            self.webos_client.launch_app(self.appid("tv"))

    
    def power_clicked(self):
        return self.webos_client.power_off()


    def pause_clicked(self):
        return self.webos_client.pause()


    def play_clicked(self):
        return self.webos_client.play()


    def rewind_clicked(self):
        return self.webos_client.rewind()


    def forward_clicked(self):
        return self.webos_client.fast_forward()

