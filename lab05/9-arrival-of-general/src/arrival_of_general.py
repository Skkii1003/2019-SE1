"""write your code in method"""


def calculate():

    #input
    numofsoiders = int (input())
    height = []
    for i in range(numofsoiders):
        height.append(int(input()))
    #print(height)

    times = 0

    # process

    for i in range(numofsoiders):
        if height[i] == max(height):
            times += i
            #print(i, height[i], times, max(height))
            height.remove(height[i])
            break
    for i in range(numofsoiders-2,-1,-1):
        if height[i] == min(height):
            times += (numofsoiders - i - 2)
            #print(i)
            break


    print(times)
    pass


if __name__ == "__main__":
    calculate()

