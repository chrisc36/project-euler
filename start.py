__author__ = 's1351418'

import math
import numpy as np


def get_primes():
    """ Yields sequential primes numbers. """
    yield 2
    primes = [2]
    num = 1
    while True:
        num += 2
        root_num = math.sqrt(num)
        is_prime = True
        for prime in primes:
            if prime > root_num:
                break
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num


def p20():
    total = 0
    for digit in str(math.factorial(100)):
        total += int(digit)
    print(total)


def p19():
    from datetime import date
    sundays = 0;
    for year in xrange(1901, 2001):
        for month in xrange(1, 13):
            if date(year, month, 1).weekday() == 6:
                sundays += 1
    print(sundays)


def p18():
    data = []
    max_totals = []
    with open("data/p18_numbers.txt") as f:
        for line in f:
            data.append(list(map(int, line.split(" "))))
            max_totals.append([None] * len(data[-1]))

    max_totals[0][0] = data[0][0]
    for y in range(1, len(data)):
        max_totals[y][0] = max_totals[y - 1][0] + data[y][0]
        max_totals[y][-1] = max_totals[y - 1][-1] + data[y][-1]
        for x in range(1, len(max_totals[y]) - 1):
            max_totals[y][x] = max(
                max_totals[y - 1][x - 1],
                max_totals[y - 1][x]
            ) + data[y][x]
    print(max(max_totals[-1]))


def p17():
    teens =["", "one", "two", "three",
        "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven",
        "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"]
    tens_prefix = [None, None,
        "twenty", "thirty", "forty", "fifty", "sixty",
        "seventy", "eighty", "ninety"]

    total = 0
    for hundreds in range(10):
        for tens in range(10):
            for ones in range(10):
                s = ""
                if hundreds != 0:
                    if ones == 0 and tens == 0:
                        s = teens[hundreds] + " hundred"
                        print(s)
                        s = s.replace(" ", "")
                        total += len(s)
                        continue
                    else:
                        s += teens[hundreds] + " hundred and "
                if tens < 2:
                        s += teens[tens * 10 + ones]
                else:
                    s += tens_prefix[tens] + " "
                    s += teens[ones]
                print(s)
                total += len(s.replace(" ", ""))
    print(total + len("onethousand"))


def p16():
    l = str(2 ** 1000)
    total = 0
    for d in l:
        total += int(d)
    print(total)


def p15():
    np.set_printoptions(linewidth=500)
    grid = np.zeros((21, 21), dtype=np.int64)
    grid[grid.shape[0] - 1, :] = 1
    grid[:, grid.shape[1] - 1] = 1
    for y in range(grid.shape[0] - 2, -1, -1):
        for x in range(grid.shape[0] - 2, -1, -1):
            grid[y, x] = grid[y + 1, x] + grid[y, x + 1]
    print(grid)


def p14():
    chain_lengths = np.zeros(1000001)
    # chain_lengths = np.zeros(14)
    chain_lengths[1] = 1
    for i in range(2, chain_lengths.shape[0]):
        starting_i = i
        length = 0
        while True:
            if i % 2 == 0:
                i /= 2
            else:
                i = 3 * i + 1
            length += 1
            if i < starting_i:
                length += chain_lengths[i]
                break
        chain_lengths[starting_i] = length
    print(np.argsort(-chain_lengths)[0:10])


def p13():
    nums = []
    with open("data/p13_numbers.txt") as f:
        for line in f:
            nums.append(int(line.strip()))
    total = 0
    print(len(nums))
    for num in nums:
        total += num
    print(total)


def p12():
    t = np.int64(1)
    nums = np.arange(1000000, dtype=np.int64) + 1
    rs = np.ones(1000000, dtype=np.int64)
    next_num = 2
    while True:
        np.mod(t, nums, rs)
        zeros = rs.shape[0] - np.count_nonzero(rs)
        print(t)
        if zeros >= 500:
            print(next_num)
            print(t)
            exit()
        t += next_num
        next_num += 1


def p11():

    def product_in_direction(grid, dir, position):
        product = int(grid[position[0], position[1]])
        for _ in range(3):
            position += dir
            if np.any(position < 0) or np.any(position >= 20):
                return None
            product *= grid[position[0], position[1]]
        return product

    grid = np.array(map(int,
"""
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
""".split()), dtype=np.int16).reshape(20, 20)
    best = -1
    for x in range(20):
        for y in range(20):
            for dir in [np.array([0, 1]), np.array([1, 0]), np.array([1, 1]), np.array([-1, 1])]:
                best = max(best, product_in_direction(grid, dir, np.array([x, y])))
    print(best)


def p10():
    s = 0
    prime_iter = get_primes()
    prime = prime_iter.next()
    while prime < 2000000:
        s += prime
        prime = prime_iter.next()
    print(s)


def p9():
    for a in range(500):
        for b in range(500):
            c =  math.sqrt(a*a + b*b)
            if c == int(c) and a + b + c == 1000:
                print(a*b*c)
                return


def p8():
    digits = map(lambda x: int(x), ''.join(("""
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
""").split()))
    best = -1
    for i in range(len(digits)):
        product = 1
        for j in range(5):
            product *= digits[i + j]
        best = max(best, product)
    print(best)


def p7():
    prime_iter = get_primes()
    for _ in range(10001):
        prime = prime_iter.next()
    print(prime)


def p6():
    total = 0
    for x in range(1, 101):
        for y in range(1, 101):
            if x != y:
                total += x * y
    print(total)


def p5():
    # Target number must have these factors to be valid
    increment = 4 * 9 * 5 * 7 * 11 * 13 * 17 * 19
    i = 0
    done = False
    while not done:
        i += increment
        done = True
        for j in range(2, 21):
            if i % j != 0:
                done = False
                break
    print(i)


def p4():
    largest = 0
    for x in range(1000):
        for y in range(1000):
            total = str(x * y)
            palindrone = True
            for i in range(len(total) / 2 + 1):
                if total[i] != total[-i - 1]:
                    palindrone = False
                    break
            if palindrone:
                largest = max(largest, int(total))
    print(largest)


def p3():
    i = 600851475143.0
    prime_iter = get_primes()
    primes = list(prime_iter.next() for _ in range(10000))
    for factor in primes:
        if int(i) % factor == 0:
            print(factor)
            print(i / factor)
            break


def p2():
    t0 = 1
    t1 = 2
    total = 0
    while t1 < 4000000:
        if t1 % 2 == 0:
             total += t1
        old_t1 = t1
        t1 = t1 + t0
        t0 = old_t1
    print(total)


def p1():
    total = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
             total += i
    print(total)

if __name__ == "__main__":
    p20()
