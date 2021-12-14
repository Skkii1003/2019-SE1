"""write your code in method solve"""
def solve():

    # input
    n = int(input())
    numofpeople = list(map(int,input().split()))

    #process
    numof4 = numofpeople.count(4)
    numof3 = numofpeople.count(3)
    numof2 = numofpeople.count(2)
    numof1 = numofpeople.count(1)
    
    if numof3 >= numof1:
        print(numof3 + numof4 + numof2 // 2 + numof2 % 2)
        return
    else:
        numof1remain = numof1 - numof3
        print(numof4 + numof3 + (numof1remain // 2 + numof1remain % 2 + numof2) // 2 + (numof1remain // 2 + numof1remain % 2 + numof2) % 2)
        return
