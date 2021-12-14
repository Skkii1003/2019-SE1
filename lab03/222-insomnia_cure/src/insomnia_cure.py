"""write your code in method sove"""
def solve():
    k = int (input())
    l = int (input())
    m = int (input())
    n = int (input())
    d = int (input())
    sum = 0

    if k == 1 or l == 1 or m == 1 or n == 1:
        print(d)
        return

    for i in range(1,d+1):
        if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
            sum += 1

    print(sum)
    return






