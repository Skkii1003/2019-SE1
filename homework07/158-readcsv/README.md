Python
Read CSV

编写一个程序，读取一个CSV文件并格式化输出

CSV文件即逗号分隔值文件，示例：

    Ling,Mai,55900
    Johnson,Jim,56500
    ......
    Zarnecki,Sabrina,51500
    
输出格式为表格形式，以四个空格为间隔，示例：

    Last    Fisrt    Salary
    Ling    Mai    55900.00
    Johnson    Jim    56500.00
    ......
    Zarnecki    Sabrina    51500.00
    
注意：

1. 要读取的文件名将以参数的形式传递到待编写的函数中
2. Salary输出到小数点后两位