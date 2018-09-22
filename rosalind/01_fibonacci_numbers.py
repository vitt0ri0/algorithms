def fibo(n):
    """Calculates n-th fibonacci number"""
    prev = 0
    curr = 1
    if n == 0:
        return prev
    if n == 1:
        return curr
    for i in range(n-1):
        prev, curr = curr, prev + curr
    return curr


if __name__ == "__main__":
    """Print first 20 fibonacci numbers"""
    for n in range(21):
        print("{}: {}".format(n, fibo(n)))
