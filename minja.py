import sqlite3
import keyboard
import sys
from db_funs_mult import get_status, add_block_taken, mark_block_done, add_keys
from funs import get_address_from_sk_hex, roundac

con = sqlite3.connect("Z:\\minja\\minja.db")

target = '1NiNja'
target_len = len(target)
block_size = 10 ** 5
prob_to_fail = 1 - 1 / 58 ** 6

print("Hello from Minja!")
print("Doing...")
counter = 0

while True:
    s = get_status(con, fair=0)
    add_block_taken(con, s.block_to_do)
    sk_dec_start = (s.block_to_do - 1) * block_size + 1
    for sk_dec in range(sk_dec_start, sk_dec_start + block_size):
        sk_hex = hex(sk_dec)[2:].zfill(64)
        k = get_address_from_sk_hex(sk_hex)
        if k[0:target_len] == target:
            print(k, "<-", sk_hex)
            add_keys(con, k, sk_hex)
            counter += 1
        if keyboard.is_pressed('windows+F12'):
            con.close()
            sys.exit()
    mark_block_done(con, s.block_to_do)
    print(s.block_to_do, "done ,",
          "found:", counter,
          ", accrued prob:", roundac(100 * (1 - prob_to_fail ** (s.block_to_do * block_size))), '%')
