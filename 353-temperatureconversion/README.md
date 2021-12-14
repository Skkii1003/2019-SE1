python
Temperature Conversion

我们经常需要确定程序的哪一部分应该根据用户的输入或其他事件来运行。

1. 使用python编写一个程序，将温度从华氏温度(F)转换成摄氏温度(C)，或者相反。
2. 程序从控制台接受输入，输入内容为：
	1. 温度转换类型convert_type，字符串。有以下两个可能的输入：
		1. 'C'，表示将温度从华氏温度(F)转换成摄氏温度(C)。
		2. 'F'，表示将温度从摄氏温度(C)转换成华氏温度(F)。
	2. 对应温度类型的温度temperature，整数。
3. 转换公式为：
	1. 华氏温度(F)转换成摄氏温度(C)：C=(F-32)*5/9
	2. 摄氏温度(C)转换成华氏温度(F)：F=(C*9/5)+32
4. 程序结果输出到控制台，输出内容为：
	1. 转换后的温度。结果保留整数，向下取整。

项目说明：

>src目录下为题目代码源文件，需要完成的内容为temperature_conversion.py里的convert_temperature()方法。
>src目录下的__init__.py文件不需要改动。
>
>test目录下为测试用例文件，不可进行修改。

示例：

	case1:
	输入：
	  Your choice: C
	  Please enter the temperature in Fahrenheit: 32
	输出：
	  The temperature in Celsius is 0.
	case2:
	输入：
	  Your choice: F
	  Please enter the temperature in Celsius: 8
	输出：
	  The temperature in Fahrenheit is 46.

```python
import unittest
import sys
from src import temperature_conversion


class Test(unittest.TestCase):
    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test_temperature_one(self):
        self.stream_in.write('C')
        self.stream_in.write('32')
        temperature_conversion.convert_temperature()
        expect = 'The temperature in Celsius is 0.\n'
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_temperature_two(self):
        self.stream_in.write('F')
        self.stream_in.write('8')
        temperature_conversion.convert_temperature()
        expect = 'The temperature in Fahrenheit is 46.\n'
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_temperature_three(self):
        self.stream_in.write('C')
        self.stream_in.write('0')
        temperature_conversion.convert_temperature()
        expect = 'The temperature in Celsius is -18.\n'
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_temperature_four(self):
        self.stream_in.write('C')
        self.stream_in.write('100')
        temperature_conversion.convert_temperature()
        expect = 'The temperature in Celsius is 37.\n'
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_temperature_five(self):
        self.stream_in.write('F')
        self.stream_in.write('100')
        temperature_conversion.convert_temperature()
        expect = 'The temperature in Fahrenheit is 212.\n'
        result = ''
        for i in range(2, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def tearDown(self):
        sys.stdout = self.out_stream
        sys.stdin = self.in_stream
        pass


class MyStream:
    def __init__(self):
        self.buff = []
        self.write_count = 0

    def write(self, output_stream):
        self.buff.append(output_stream)
        if len(self.buff) > 10000:
            sys.exit("Too many outputs, error! There may be an endless loop in your code!")

    def readline(self):
        if len(self.buff) > 0:
            cur = self.buff[0]
            del self.buff[0]
            return cur

```



