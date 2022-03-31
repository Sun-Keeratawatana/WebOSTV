from pylgtv import WebOsClient

import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

try:
    webos_client = WebOsClient('10.66.2.172')
    #webos_client.launch_app('youtube.leanback.v4')
    #webos_client.volume_down()
    #print(webos_client.get_inputs())
    #print(webos_client.get_audio_status().get("volumeStatus")["volume"])
    #print(webos_client.get_input())
    print(webos_client.get_current_app())
    #print(webos_client.get_input())
except:
    print("Error connecting to TV")
