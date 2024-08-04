import base64

#function
def encoded_4th(message):
    x = base64.b85encode(message)
    print(x)
    return x

def encoded_3rd(message):
    x = base64.b64encode(message)
    print(x)
    return encoded_4th(x)

def encoded_2nd(message):
    x = base64.b32encode(message)
    print(x)
    return encoded_3rd(x)

def encoded_1st(message):
    x = base64.b16encode(message.encode())
    print(x)
    return encoded_2nd(x)

def encode(message):
    m = encoded_1st(message)
    return m

