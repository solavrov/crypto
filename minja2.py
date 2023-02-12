import sqlite3
import keyboard
import time
import multiprocessing
from db_funs_mult import get_status, add_block_taken, mark_block_done, add_keys, \
    clean_block_done, count_found, cut_block_done
from funs import get_address_from_sk_hex, roundac


def task(minja_number):
    con = sqlite3.connect("Z:\\minja\\minja2.db")
    found0 = count_found(con)
    target = '1NiNja'
    target_len = len(target)
    block_size = 10 ** 5
    prob_to_fail = 1 - 1 / 58 ** 6
    print("Hello from Minja #" + str(minja_number) + "! Working...")
    while True:
        s = get_status(con, fair=0)
        add_block_taken(con, s.block_to_do)
        sk_dec_start = (s.block_to_do - 1) * block_size + 1
        for sk_dec in range(sk_dec_start, sk_dec_start + block_size):
            sk_hex = hex(sk_dec)[2:].zfill(64)
            k = get_address_from_sk_hex(sk_hex)
            if k[0:target_len] == target:
                print(k)
                add_keys(con, k, sk_hex)
            if keyboard.is_pressed('windows+F12'):
                con.close()
                return 0
        mark_block_done(con, s.block_to_do)
        cut_block_done(con)
        found = count_found(con)
        print(str(s.block_to_do) + " done by Minja #" + str(minja_number) +
              ", found: " + str(found - found0) +
              ", accrued prob: " + str(roundac(100 * (1 - prob_to_fail ** (s.block_to_do * block_size)))) + '%')


if __name__ == '__main__':
    n = int(input("Number of minjas: "))
    processes = []
    for i in range(n):
        p = multiprocessing.Process(target=task, args=(i,))
        processes.append(p)
        p.start()
        time.sleep(40/n)
    for p in processes:
        p.join()
    con_clean = sqlite3.connect("Z:\\minja\\minja2.db")
    print("Cleaning minja2.db...")
    clean_block_done(con_clean)
    con_clean.close()
    print("Cleaned!")
    input("Press any key to close window")
