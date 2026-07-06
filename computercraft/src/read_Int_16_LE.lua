local function readInt16LE(b1, b2)
    local val = b1 + b2 * 256
    if val >= 32768 then
        val = val - 65536
    end
    return val
end