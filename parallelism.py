import time
import multiprocessing as mp


def sleep_5():
    for i in range(0, 5):
        print(i)
        time.sleep(1)
    return


def sleep_10():
    for i in range(0, 10):
        print(i)
        time.sleep(1)
    return


if __name__ == '__main__':
    p1 = mp.Process(target=sleep_5)
    p2 = mp.Process(target=sleep_10)
    start_time = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end_time = time.time()
    print('It costs ' + str(end_time - start_time) + ' s')