#!/usr/bin/env python3

import binascii
import struct

def KSA(key):
    S = list(range(256))
    # Add KSA implementation Here
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
    return S

def PRGA(S):
    K = 0
    # Add PRGA implementation here
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key):
    S = KSA(key)
    return PRGA(S)

if __name__ == '__main__':
    # RC4 algorithm please refer to http://en.wikipedia.org/wiki/RC4

    ## key = a list of integer, each integer 8 bits (0 ~ 255)
    ## ciphertext = a list of integer, each integer 8 bits (0 ~ 255)
    ## binascii.unhexlify() is a useful function to convert from Hex string to integer list
    iv_key = binascii.unhexlify("9ccc471f1f1f1f1f")
    message_ciphertext = binascii.unhexlify("edd4853da5933c8c915e260537b4148d419181a196da5500e21039c16b7b456840a418ce1d5ff72bc91fcf4c4bd8372bd5307e982a5e")

    ## Use RC4 to generate keystream
    keystream = RC4(iv_key)
    #print(keystream)
    
    ## Cracking the ciphertext
    message_plaintext = ""
    for i in message_ciphertext:
        message_plaintext += ('{:02X}'.format(i ^ next(keystream)))
    print("Message plaintext (without CRC) =", message_plaintext)

    #     Several test cases: (to test RC4 implementation only)
    #     1. key = '1A2B3C', cipertext = '00112233' -> plaintext = '0F6D13BC'
    #     2. key = '000000', cipertext = '00112233' -> plaintext = 'DE09AB72'
    #     3. key = '012345', cipertext = '00112233' -> plaintext = '6F914F8F'
    
    
    
    ## Check ICV
    crcle = binascii.crc32(bytes.fromhex(message_plaintext)) & 0xffffffff
    crc = struct.pack('<L', crcle)
    crc_plaintext = binascii.hexlify(crc).decode("utf-8")
    print("CRC plaintext (without message) =", crc_plaintext)

    combined_plaintext = message_plaintext + crc_plaintext
    combined_plaintext = binascii.unhexlify(combined_plaintext)
    keystream2 = RC4(iv_key)
    combined_ciphertext = ""
    for i in combined_plaintext:
        combined_ciphertext += ('{:02X}'.format(i ^ next(keystream2)))
    print("Combined ciphertext =", combined_ciphertext)
    crc_ciphertext = combined_ciphertext[len(message_plaintext):]
    print("Encrypted CRC =", crc_ciphertext)
