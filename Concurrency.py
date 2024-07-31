import os
import threading
import time

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

    start_time = time.time()

    thread_1 = threading.Thread(target=sleep_5)
    thread_2 = threading.Thread(target=sleep_10)
    thread_1.start()
    thread_2.start()
    thread_1.join()  # 等待thread_1結束
    thread_2.join()  # 等待thread_2結束

    end_time = time.time()
    print('It costs ' + str(end_time - start_time) + ' s')