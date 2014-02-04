__author__ = 'Claudio'


from Crypto.Cipher import AES
import base64

def encryption(privateInfo, bitKey):
    BLOCK_SIZE = 32
    PADDING = '{'
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    secret = bitKey
    cipher = AES.new(secret)
    encoded = EncodeAES(cipher, privateInfo)
    return encoded, secret

def decryption(encryptedString, key):
    PADDING = '{'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    encryption = encryptedString
    key = key
    cipher = AES.new(key)
    decoded = DecodeAES(cipher, encryption)
    return decoded

