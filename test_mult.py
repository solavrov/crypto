import sqlite3
from funs import get_address_from_sk_hex, roundac
from db_funs_mult import get_status, add_block_taken, mark_block_done, add_keys, clean_block_done, add_tuples

con = sqlite3.connect("minja.db")

# add_block_taken(con, 2)
# add_block_taken(con, 3)
# add_block_taken(con, 4)
# mark_block_done(con, 2)
# mark_block_done(con, 4)

clean_block_done(con)

# s = get_status(con, 1)
# print(s.blocks_done)
# print(add_tuples(s.blocks_done))



