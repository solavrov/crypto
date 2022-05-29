from funs import get_address_from_sk_hex
import random as rnd

target = '1NiNja'
n = len(target)
m = 4
total_tries = 10**8
info_step = total_tries / 1000

p = 1
for i in range(total_tries):
    if i / info_step > p:
        print(p, '/ 1000')
        p += 1
    sk_hex = hex(rnd.getrandbits(256))[2:].zfill(64)
    k = get_address_from_sk_hex(sk_hex)
    if k[0:m] == target[0:m]:
        print(sk_hex)
        print(k)
        if k[0:n] == target:
            break
