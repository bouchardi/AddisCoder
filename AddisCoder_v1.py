#
# AddisCoder.py
# Solutions for the Addis Coder application
# 2018-05-05
# Author: Isabelle Bouchard
#

import sys


def multiply_three(x):
    """
    Multiply a number (x) by three
    """
    return x * 3


def multiply_three_examples():
    examples = [2, 5, -1, 15647186, 15, -40]
    for ex in examples:
        print('{} * 3 = {}\n'.format(ex, multiply_three(ex)))


def get_min_coins_recursive(L, n):
    """
    Plain recursive solution to get min coins
    """
    count = sys.maxint

    if not n:
        return 0

    for coin in L:
        if coin > n:
            continue
        sub_count = get_min_coins_recursive(L, n - coin)
        if  sub_count < count -1 and sub_count != sys.maxint:
                count = sub_count + 1
    return count


def get_min_coins_recursive_mem(L, n, mem):
    """
    Memoization solution to get min coins
    """
    if mem[n] != sys.maxint:
        return mem[n]

    if mem[n] == -1:
        return -1

    if not n:
        mem[n] = 0
        return 0

    for coin in L:
        if coin > n:
            continue
        sub_count = get_min_coins_recursive_mem(L, n - coin, mem)
        if  sub_count < mem[n] - 1 and sub_count != -1:
            mem[n] = sub_count + 1

    if mem[n] == sys.maxint:
        mem[n] = -1

    return  mem[n]


def get_solution(solution):
    return solution if solution != sys.maxint else -1


def make_change():
    examples = [(14, [1, 5, 10, 25, 50, 100]),
                (3, [2, 5]),
                (8, [1, 4, 5])]

    for n, L in examples:
        mem = [sys.maxint for x in range(n + 1)]
        print('Plain recursion: {} solutions for {} with {}'.format(get_solution(get_min_coins_recursive(L, n)), n, L))
        print('Memoization: {} solutions for {} with {}\n'.format(get_solution(get_min_coins_recursive_mem(L, n, mem)), n, L))


if __name__ == '__main__':
    print('multiply_three() \n')
    multiply_three_examples()
    print('>>> make_change() \n')
    make_change()
