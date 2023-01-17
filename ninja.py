import sqlite3
from funs import get_address_from_sk_hex, roundac
from db_funs import read_block, block_up, add_keys

con = sqlite3.connect("ninja.db")

target = '1NiNja'
target_len = len(target)
block_size = 10 ** 5
prob_to_fail = 1 - 1 / 58 ** 6

print("Doing...")
last_block_done = read_block(con)
counter = 0

while True:
    sk_dec_start = last_block_done * block_size + int(last_block_done == 0)
    for sk_dec in range(sk_dec_start, sk_dec_start + block_size + 1):
        sk_hex = hex(sk_dec)[2:].zfill(64)
        k = get_address_from_sk_hex(sk_hex)
        if k[0:target_len] == target:
            print(k, "<-", sk_hex)
            add_keys(con, k, sk_hex)
            counter += 1
    last_block_done += 1
    block_up(con)
    print(last_block_done, "done ,",
          "found:", counter,
          ", accrued prob:", roundac(100 * (1 - prob_to_fail ** (last_block_done * block_size))), '%')





