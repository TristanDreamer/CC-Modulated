require("route_sound_to_device")

local socket = peripheral.find("simpleradio:insulator")
local file = fs.open("test/output.pcm", "rb")
local data = file.readAll()


route_sound_to_device(data, socket, 1)