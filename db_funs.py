import sqlite3


def read_block(connection):
    cursor = connection.cursor()
    return cursor.execute("SELECT lastBlock FROM Progress").fetchone()[0]


def block_up(connection):
    last_block = read_block(connection)
    cursor = connection.cursor()
    cursor.execute("UPDATE Progress SET lastBlock = " + str(last_block + 1) + " WHERE id = 0;")
    connection.commit()


def add_keys(connection, pub_key, pvt_key):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Keys (pubKey, pvtKey) VALUES ('" + str(pub_key) + "', '" + str(pvt_key) + "');")
    connection.commit()



# tests
# con = sqlite3.connect("ninja.db")
# print(read_block(con))
#
# block_up(con)
# print(read_block(con))
#
# add_keys(con, "1FCpevDKrWFixFaD6pPMRHP5NAZDTPduKb", "L4KMd2ta8uMoBR8jrGRrF5v1DVfYPajMyjzzATWjG46E4ukjgUgW")
#
# con.close()
