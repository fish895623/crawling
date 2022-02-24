import time
from multiprocessing import Pool


def count(process):
    for i in range(1, 1001):
        print(process, i)


if __name__ == "__main__":
    start_time = time.time()
    p_list = ["p1", "p2", "p3", "p4"]
    pool = Pool(processes=8)
    pool.map(count, p_list)
    pool.close()
    pool.join()

    print(time.time() - start_time)
