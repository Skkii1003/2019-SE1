python
Body mass index judgement

经常有这样的需求：看看某个值是不是在特定的范围内，并根据结果来修改程序的流程。

1. 用python编写一个程序，用一个人的身高(以英寸为单位)和体重(以磅为单位)来计算其体质指数(Body Mass Index，BMI)，然后给出相应的提示。
2. 程序从控制台接受输入，输入内容为：
	1. 身高height，整数。
	2. 体重weight，整数。
3. 计算公式为：bmi = (weight / (height * height)) * 703
4. 程序结果输出到控制台，输出内容为：
	1. 计算得到的BMI，浮点数，保留1位小数，向上舍入。
	2. 如果BMI在18.5和25之间(18.5<=bmi<=25)，显示这个人为正常体重。如果在该范围之外，则提示用户偏瘦或超重，建议就医咨询。

项目说明：

>src目录下为题目代码源文件，需要完成的内容为bmi_judge.py里的bmi()方法。
>src目录下的__init__.py文件不需要改动。
>
>test目录下为测试用例文件，不可进行修改。

示例：

	case1:
	输入：
	  What is your height? 68
	  What is your weight? 146
	输出：
	  Your BMI is 22.2.
	  You are within the ideal weight range.
	case2:
	输入：
	  What is your height? 68
	  What is your weight? 177
	输出：
	  Your BMI is 26.9.
	  You are overweight.You should see your doctor.
	  case3:
	输入：
	  What is your height? 67
	  What is your weight? 115
	输出：
	  Your BMI is 18.1.
	  You are underweight.You should see your doctor.
	

