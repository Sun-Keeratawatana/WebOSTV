from pylgtv import WebOsClient

import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

try:
    webos_client = WebOsClient('192.168.4.136')
    #webos_client.launch_app('youtube.leanback.v4')
    #webos_client.volume_down()
    #webos_client.volume_up()
    #print(webos_client.get_apps())
    #print(webos_client.get_inputs())
    #print(webos_client.get_audio_status().get("volumeStatus")["volume"])
    #print(webos_client.get_audio_status())
    #print(webos_client.get_audio_status().get("volume"))
    #print(webos_client.get_channels())
    #print(webos_client.get_input())
    #webos_client.power_off()
    #print(webos_client.get_input())
    print(webos_client.get_services())
except:
    print("Error connecting to TV")
