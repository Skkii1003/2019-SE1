"""write your code in method solve"""

def timeofA(a,time):
    sec = 0
    for i in range(0,a):
        sec += time[i]
    return sec
def timeofB(b,time):
    sec = 0
    for i in range(0,b):
        sec += time[len(time)-i-1]
    return sec

def solve():
    #input
    n = int(input())
    time = list(map(int,input().split(" ")))
    a = 0
    b = 0

    #process
    while (a+b) < n:
        timeA = timeofA(a,time)
        timeB = timeofB(b,time)
        # print('timea',timeA)
        # print('timeb',timeB)
        if timeB < timeA:
            while timeB <= timeA:
                if (a+b)>=n:
                    break
                b += 1
                timeB = timeofB(b,time)

            if (a+b) == n:
                break
            a += 1

        elif timeA < timeB:
            while timeA <= timeB:
                if (a+b)>=n:
                    break
                a += 1
                timeA = timeofA(a,time)

            if (a + b) == n:
                break
            b += 1

        elif timeB == timeA:
            if (n-a-b) == 1:
                a += 1
                break
            else:
                a += 1
                b += 1
    print(a, end='')
    print(' ', end='')
    print(b)
    return
