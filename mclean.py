import sqlite3
from db_funs_mult import clean_block_done

con = sqlite3.connect("Z:\\minja\\minja2.db")
print("Cleaning minja2.db...")
clean_block_done(con)
print("Cleaned!")
input("Press any key to close window\n")
con.close()
