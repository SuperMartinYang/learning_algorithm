class Fib:
    def __init__(self, mx):
        self.mx = mx
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self
    def __next__(self):
        fib = self.a
        if fib > self.mx:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

for n in Fib(100):
    print(n,end=' ')