import sqlite3
import keyboard
import time
import multiprocessing
from db_funs_mult import get_status, add_block_taken, mark_block_done, add_keys, cut_block_done
from funs import get_address_from_sk_hex, roundac


def task(minja_number):
    con = sqlite3.connect("Z:\\minja\\minja2.db")
    target = '1NiNja'
    target_len = len(target)
    block_size = 10 ** 5
    prob_to_fail = 1 - 1 / 58 ** 6
    counter = 0
    closing = False
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
                counter += 1
            if keyboard.is_pressed('windows+F12') and not closing:
                print("Minja #" + str(minja_number) + " is closing...")
                closing = True
        mark_block_done(con, s.block_to_do)
        cut_block_done(con)
        print(str(s.block_to_do) + " done by Minja #" + str(minja_number) +
              ", found: " + str(counter) +
              ", prob: " + str(roundac(100 * (1 - prob_to_fail ** (s.block_to_do * block_size)))) + '%')
        if closing:
            con.close()
            print("Minja #" + str(minja_number) + " is closed!")
            return 0


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
    print("All is finished correctly!")
    input("Press any key to close window\n")
