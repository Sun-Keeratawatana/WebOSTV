from pylgtv import WebOsClient

import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

try:
    webos_client = WebOsClient('192.168.1.110')
    #webos_client.launch_app('youtube.leanback.v4')
    webos_client.volume_up()
    
except:
    print("Error connecting to TV")