from funs import get_address_from_sk_hex

target = '1XxXxx'
n = len(target)
m = 4
block_size = 10 ** 8
info_step = block_size / 1000

block_number = 1

sk_dec_start = (block_number - 1) * block_size + int(block_number == 1)
p = 1
for sk_dec in range(sk_dec_start, block_size * block_number):
    if (sk_dec - sk_dec_start) / info_step > p:
        print(p, '/ 1000')
        p += 1
    sk_hex = hex(sk_dec)[2:].zfill(64)
    sk_dec += 1
    k = get_address_from_sk_hex(sk_hex)
    if k[0:m] == target[0:m]:
        print(sk_hex)
        print(k)
        if k[0:n] == target:
            break
