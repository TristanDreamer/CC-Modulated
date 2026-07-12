import json
from ..main import sock
from .endpoint_command_list import COMMAND_LIST

@sock.route('/endpoint')
def endpoint_main(ws):
    while ws.connected:
        # Packet format should look something like:
        #   {
        #       command --> int
        #       data -->
        #   }
        packet = ws.receive()


def decode_packet(packet) -> tuple[int, str]:
    try:
        json_pack = json.dumps(packet)


    except Exception as E:
        return (-1, str(E))