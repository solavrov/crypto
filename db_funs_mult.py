def del_tuples(list_of_tuples):
    just_list = list()
    for t in list_of_tuples:
        just_list.append(t[0])
    return just_list


def add_tuples(just_list):
    list_of_tuples = list()
    for e in just_list:
        list_of_tuples.append((e, 1))
    return list_of_tuples


def read_block_done(connection, fair):
    cursor = connection.cursor()
    if fair == 0:
        b = del_tuples(cursor.execute("SELECT blockDone FROM BlockDone").fetchall())
    else:
        b = del_tuples(cursor.execute("SELECT blockDone FROM BlockDone WHERE fair=1").fetchall())
    b = list(set(b))
    b.sort()
    return b


class Status:
    def __init__(self, block_to_do, blocks_done):
        self.block_to_do = block_to_do
        self.blocks_done = blocks_done


def get_status(connection, fair):
    blocks_done = read_block_done(connection, fair)
    b0 = blocks_done[0] + 1
    if len(blocks_done) == 1:
        return Status(b0, blocks_done)
    else:
        for i in range(1, len(blocks_done)):
            if blocks_done[i] != b0:
                return Status(b0, blocks_done[(i - 1):])
            b0 += 1
        return Status(b0, [b0 - 1])


def clean_block_done(connection):
    s = get_status(connection, fair=1)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM BlockDone")
    cursor.executemany("INSERT INTO BlockDone (blockDone, fair) VALUES (?, ?)", add_tuples(s.blocks_done))
    connection.commit()


def add_block_taken(connection, block):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO BlockDone (blockDone, fair) VALUES (" + str(block) + ", 0);")
    connection.commit()


def mark_block_done(connection, block):
    cursor = connection.cursor()
    cursor.execute("UPDATE BlockDone SET fair=1 WHERE blockDone=" + str(block) + ";")
    connection.commit()


def add_keys(connection, pub_key, pvt_key):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Keys (pubKey, pvtKey) VALUES ('" + str(pub_key) + "', '" + str(pvt_key) + "');")
    connection.commit()


def count_found(connection):
    cursor = connection.cursor()
    return cursor.execute("SELECT COUNT(pubKey) FROM Keys;").fetchone()[0]

