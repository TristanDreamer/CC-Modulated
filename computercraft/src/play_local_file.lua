
local socket = peripheral.find("simpleradio:insulator")
if not socket then
    error("No simpleradio speaker/socket peripheral found")
end

local CHUNK_SAMPLES = 960 * 16 -- must be a multiple of 960'
local BYTES_PER_SAMPLE = 2
local CHUNK_DURATION_MS = (CHUNK_SAMPLES / 48000) * 1000

local file = fs.open("test/output.pcm", "rb")

local data = file.readAll()

local total = #data

local function readInt16LE(b1, b2)
    local val = b1 + b2 * 256
    if val >= 32768 then
        val = val - 65536
    end
    return val
end



local pos = 1
local nextTime = os.epoch("utc")


while pos < total do
    local buffer = {}
    local n = 0
    
    local endPos = math.min(pos + CHUNK_SAMPLES * BYTES_PER_SAMPLE - 1, total - 1)
    
    
    for i = pos, endPos, 2 do
        n = n + 1
        buffer[n] = readInt16LE(data:byte(i), data:byte(i + 1))
    end
    
    if n > 0 then
        local remainder = n % 960
        if remainder ~= 0 then
            for i = n + 1, n + (960 - remainder) do
                buffer[i] = 0
            end
        end

        socket.route(buffer, 1) -- volume 0-1
    end
    
    nextTime = nextTime + CHUNK_DURATION_MS
    local now = os.epoch("utc")
    local waitMs = nextTime - now
    if waitMs > 0 then
        sleep(waitMs / 1000)
    end
    
    pos = pos + CHUNK_SAMPLES * BYTES_PER_SAMPLE
    
end

