"""write your code in method solve"""
def solve():
    n,m = map(int,input().split())
    a = [int(i) for i in input().split()]

    times = 0
    for i in range(0,m):
        if i == 0:
            times = a[0] - 1
            continue
        if a[i] == a[i-1]:
            continue
        if a[i] > a[i-1]:
            times += (a[i]-a[i-1])
        if a[i] < a[i-1]:
            times += (n - a[i-1] + a[i])
    print(times)
    return