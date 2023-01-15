import sqlite3
from funs import get_address_from_sk_hex
from db_funs import read_block, block_up, add_keys

con = sqlite3.connect("ninja.db")

target = '1NiNja1'
target_len = len(target)
block_size = 10 ** 5

blocks_to_do = int(input("Number of blocks to do: "))
print("Doing...")
last_block_done = read_block(con)
target_block = last_block_done + blocks_to_do

for _ in range(blocks_to_do):
    sk_dec_start = last_block_done * block_size + int(last_block_done == 0)
    for sk_dec in range(sk_dec_start, sk_dec_start + block_size + 1):
        sk_hex = hex(sk_dec)[2:].zfill(64)
        k = get_address_from_sk_hex(sk_hex)
        if k[0:target_len] == target:
            print(k, "<-", sk_hex)
            add_keys(con, k, sk_hex)
    last_block_done += 1
    block_up(con)
    print(last_block_done, "done ->", target_block)

con.close()
input("All done!")


