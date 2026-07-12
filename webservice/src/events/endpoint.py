import json
from ..main import sock
from .endpoint_command_list import COMMAND_LIST
from typing import Tuple

@sock.route('/endpoint')
def endpoint_main(ws):
    while ws.connected:
        # Packet format should look something like:
        #   {
        #       command --> int
        #       data -->
        #   }
        packet = ws.receive()


def decode_packet(packet) -> Tuple[int, str]:
    try:
        json_pack = json.loads(packet)

        command = json_pack["command"]
        data = json_pack["data"]

        if command in COMMAND_LIST:
            return COMMAND_LIST[command]
        else:
            return(-2, "Unknown Command")

    except Exception as E:
        return (-1, str(E))