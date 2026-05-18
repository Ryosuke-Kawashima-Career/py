import threading
def multithread():
    for i in range(10):
        th = threading.Thread(target=powerOfTwo, args=(i, ))
        print(th.name)
        th.start()
        print(threading.active_count())

def powerOfTwo(num: int) -> int:
    if num == 0:
        return 1
    return 2 * powerOfTwo(num - 1)

def main():
    multithread()

if __name__ == '__main__':
    main()
