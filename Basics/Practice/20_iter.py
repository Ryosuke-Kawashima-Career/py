def fibonacci(limit: int):
    num1, num2 = 1, 1
    while num1 <= limit:
        yield num1
        num1, num2 = num2, num1 + num2

class Fibonacci:
    def __init__(self, limit):
        self.num1 = 1
        self.num2 = 1
        self.n = 0
        self.limit = limit
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < self.limit:
            result = self.num1
            self.num1 = self.num2
            self.num2 = result + self.num1
            self.n += 1
            return result
        else:
            raise StopIteration

def main():
    fib_iter = iter(Fibonacci(10))
    while True:
        try:
            print(next(fib_iter))
        except StopIteration:
            break

if __name__ == '__main__':
    main()
