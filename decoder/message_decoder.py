import base64

#function
def decode_4th(message):
    x = base64.b16decode(message)
    return x

def decode_3rd(message):
    x = base64.b32decode(message)
    return decode_4th(x)

def decode_2nd(message):
    x = base64.b64decode(message)
    return decode_3rd(x)

def decode_1st(message):
    x = base64.b85decode(message)
    return decode_2nd(x)

def decode(message):
    m = decode_1st(message.encode())
    return m

