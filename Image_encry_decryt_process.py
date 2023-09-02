# import DES3 for image encryption and md5 for key
from Crypto.Cipher import DES3
from hashlib import md5



def key_transformation(key):
    key_hash = md5(key.encode('ascii')).digest()
    tdes_key = DES3.adjust_key_parity(key_hash)
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')
    return cipher

def encryption(file_path,key):
    cipher = key_transformation(key)

    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()
        nfile_bytes = cipher.encrypt(file_bytes)

    with open(file_path, 'wb') as output_file:
        output_file.write(nfile_bytes)


def decryption(file_path,key):
    cipher = key_transformation(key)

    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()
        nfile_bytes = cipher.decrypt(file_bytes)

    with open(file_path, 'wb') as output_file:
        output_file.write(nfile_bytes)
        

