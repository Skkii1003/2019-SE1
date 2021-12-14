"""write your code in method get_max_number"""
def get_max_number():
    #输入三个整数
    num1 = int (input("Enter the first number:"))
    num2 = int (input("Enter the second number:"))
    num3 = int (input("Enter the third number:"))
    
    #判断是否相等
    if num1 == num2:
        print("Have the same number:{}".format(num1))
    elif num1 == num3:
        print("Have the same number:{}".format(num1))
    elif num2 == num3:
        print("Have the same number:{}".format(num2)) 
    else: # 判断大小
        if num1 > num2:
            if num1 > num3:
                print("The largest number is {}".format(num1))
            else:
                print("The largest number is {}".format(num3))
        else:
            if num2 > num3:
                print("The largest number is {}".format(num2))
            else:
                print("The largest number is {}".format(num3))
    return
