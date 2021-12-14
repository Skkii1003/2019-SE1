python
Karvonen heart rate calculation

>1.计算卡蒙内心率，公式如下：
>
>TargetHeartRate=((220-age)-RestingHR)*intensity+RestingHR。
>
>其中，intensity在0到1之间。
	
>2.程序从控制台接受输入，输入内容为：
>
>安静时心率RestingHR，和年龄age，类型均为整数。
>
>程序结果输出到控制台，输出内容为：
>
>强度intensity（百分数，从55%到95%，间隔5%），和对应的心率TargetHeartRate（**保留到整数位，舍去小数位，即向下取整，同时要求在计算完表达式后再取整**，单位bpm）。
>
>输出要以示例中的表格样式输出，分为两列，并以'|'分隔。左侧列为Intensity，列宽为9，靠左对齐；右侧列为Rate，列宽为6，靠右对齐。


项目说明：

>src目录下为题目代码源文件，需要完成的内容为heart_rate_cal.py里的方法。
>src目录下的__init__.py文件不需要改动。
>
>test目录下为测试用例文件，不可进行修改。


示例：

	输入：
	  RestingHR:65
	  Age:22

	输出：(不包含每行开头的‘* ’部分；不要输出额外的内容，否则会影响结果判断的正确性)
	* Intensity|  Rate
	* ---------|------
	* 55%      |138bpm
	* 60%      |145bpm
	* 65%      |151bpm
	* 70%      |158bpm
	* 75%      |165bpm
	* 80%      |171bpm
	* 85%      |178bpm
	* 90%      |185bpm
	* 95%      |191bpm
