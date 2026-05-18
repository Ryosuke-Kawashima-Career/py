def square_generator():
    cur = 1
    while True:
        yield cur * cur
        cur += 1

def main():
    sq_gen = square_generator()
    for _ in range(10):
        print(next(sq_gen))

if __name__ == '__main__':
    main()
