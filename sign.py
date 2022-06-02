from ecdsa import SigningKey, SECP256k1

sk_hex = 'a1b2'.zfill(64)
print(sk_hex)
sk = SigningKey.from_string(bytes.fromhex(sk_hex), curve=SECP256k1)
vk = sk.verifying_key
vk_hex = vk.to_string().hex()
print(vk_hex)
msg = b'hello people'
print(msg)
signature = sk.sign(msg)
try:
    vk.verify(signature, msg)
except:
    print('false')
fake_signature = b'fakefakefakefakefakefakefakefakefakefakefakefakefakefakefakefake'
try:
    print(vk.verify(fake_signature, msg))
except:
    print('false')
