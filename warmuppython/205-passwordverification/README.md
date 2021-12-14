python
Password Verification

1. 编写一个简单程序，验证用户登录凭证。
2. 程序接受一个函数参数，参数如下：
	1. user，系统已知的用户名，字符串。
	2. pwd，系统已知的密码，字符串。
3. 程序从控制台接受输入，输入内容为：
	1. 用户给出的用户名username，字符串。
	2. 用户给出的密码password，字符串。
4. 程序结果输出到控制台，输出内容为：
	1. 如果用户名不匹配或者密码不匹配，则输出：I don't know you.
	2. 如果用户名和密码都匹配，则输出：Welcome!

项目说明：

>src目录下为题目代码源文件，需要完成的内容为verification.py里的password_verification()方法。
>src目录下的__init__.py文件不需要改动。
>
>test目录下为测试用例文件，不可进行修改。


示例：

	case1:
	函数参数：
	  user='user01',pwd='abc$123'
	输入：
	  What is the user name? user01
	  What is the password? 12345
	输出：
	  I don't know you.
	case2:
	函数参数：
	  user='user01',pwd='abc$123'
	输入：
	  What is the user name? user01
	  What is the password? abc$123
	输出：
	  Welcome!