import sqlite3
from bitcoinlib.services.services import Service
from db_funs_mult import read_addresses

con = sqlite3.connect("Z:\\minja\\minja2.db")
address_list = read_addresses(con)

srv = Service()
for a in address_list:
    print(a, ':', srv.getbalance(a) / 10**8)

con.close()
