from funs import get_key_from_phrase, get_hex_from_wif, get_address_from_sk_hex

print(get_key_from_phrase('password', 1))

private_key_wif = 'KwX6bqzDC9T76ZG9t3AgasUzfxKBx2DTEqKE7BHStvfKVj6ecBmy'
private_key_hex = get_hex_from_wif(private_key_wif)
print(get_address_from_sk_hex(private_key_hex))
