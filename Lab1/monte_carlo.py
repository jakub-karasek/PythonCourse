import random
import math


def monte_carlo(n, k):
    counter = 0
    x = 0
    y = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            counter += 1

        if i % k == 0:
            print("k:", i, 4 * (counter / n))

    return 4 * (counter / n)


if __name__ == '__main__':
    print("przylizenie pi: ")
    moje_pi = monte_carlo(10000, 100)
    print("koncowy wynik: ", moje_pi)
    print("roznica miedzy math.pi: ", abs(math.pi - moje_pi))
