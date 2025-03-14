import threading
import time

# 创建互斥锁
lock = threading.Lock()


# 根据下标去取值， 保证同一时刻只能有一个线程去取值
def try_obtain_value(num):
    # 上锁
    lock.acquire()
    try:
        print(threading.current_thread())
        candidates = [10, 30, 50, 70, 90]
        # 判断下标释放越界
        if num not in candidates:
            print("discard:", num)
            return
        value = num
        print("success get value:", value)
        time.sleep(1.0)
    finally:
        # 释放锁
        lock.release()


if __name__ == '__main__':
    # 模拟大量线程去执行取值操作
    for num in range(100):
        sub_thread = threading.Thread(target=try_obtain_value, args=(num,), name=f'thread-{num}')
        sub_thread.start()
