from ecdsa import SigningKey, SECP256k1
from mbedtls.hashlib import ripemd160
from hashlib import sha256
from base58 import b58encode, b58decode


def sha256n(text_str, n=1):
    text_str = text_str.encode()
    for i in range(n):
        text_str = sha256(text_str).digest()
    return text_str.hex()


def get_checksum(hex_str):
    return sha256(sha256(bytes.fromhex(hex_str)).digest()).hexdigest()[0:8]


def get_wif(hex_str):
    str2 = '80' + hex_str + '01'
    str2 += get_checksum(str2)
    return b58encode(bytes.fromhex(str2)).decode()


def get_hex_from_wif(wif_str):
    str2 = b58decode(wif_str.encode()).hex()
    return str2[2:-10]


def get_address_from_sk_hex(sk_hex):
    sk_bytes = bytes.fromhex(sk_hex)
    sk = SigningKey.from_string(sk_bytes, curve=SECP256k1)
    vk = sk.verifying_key
    vk_hex = vk.to_string().hex()
    vk_decimal = int(vk_hex, 16)
    if vk_decimal % 2 == 0:
        prefix = '02'
    else:
        prefix = '03'
    vk_hex_comp = prefix + vk_hex[0:64]
    vk_hash160 = ripemd160(sha256(bytes.fromhex(vk_hex_comp)).digest()).hexdigest()
    address = '00' + vk_hash160 + get_checksum('00' + vk_hash160)
    address_b58 = b58encode(bytes.fromhex(address)).decode()
    return address_b58


def get_key_from_phrase(phrase, num_of_hashes=1):
    sk_hex = sha256n(phrase, num_of_hashes)
    sk_wif = get_wif(sk_hex)
    address_b58 = get_address_from_sk_hex(sk_hex)
    return {'private_key': sk_wif, 'address': address_b58}



