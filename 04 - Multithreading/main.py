"""
Use a lock if you want to use the thread until finished then release it
"""

import multiprocessing

import threading
import time

threading_lock = threading.Lock()


def timer(name, delay, repeat):
    print("Timer :", name, "Started")
    # Means I am the lock
    print(name, " has acquired the lock")
    threading_lock.acquire()

    while repeat > 0:
        time.sleep(delay)
        print(name, ":", str(time.ctime(time.time())))
        repeat -= 1

    print(name, "is releasing the lock")
    threading_lock.release()
    print("Timer :", name, "is completed")


def main():
    t1 = threading.Thread(target=timer, args=("Timer1", 1, 5))
    t2 = threading.Thread(target=timer, args=("Timer2", 3, 6))

    t1.start()
    t2.start()

    print("Main completed")


if __name__ == "__main__":
    cores = multiprocessing.cpu_count()
    print("\n\n***You only have", cores,
          "cpu cores. Dont make more threads "
          "than that for performance reasons***\n\n")
    main()
