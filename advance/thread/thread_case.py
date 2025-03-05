import threading
import time

# 创建互斥锁
lock = threading.Lock()


# 根据下标去取值， 保证同一时刻只能有一个线程去取值
def get_value(index):
    # 上锁
    lock.acquire()
    try:
        print(threading.current_thread())
        my_list = [3, 6, 8, 1]
        # 判断下标释放越界
        if index >= len(my_list):
            print("discard:", index)
            return
        value = my_list[index]
        print("success get value:", value)
        time.sleep(1.0)
    finally:
        # 释放锁
        lock.release()


if __name__ == '__main__':
    # 模拟大量线程去执行取值操作
    for i in range(30):
        sub_thread = threading.Thread(target=get_value, args=(i,))
        sub_thread.start()
