##  题目要求   
#### 找出一个数组中两个元素相加之和等于给定的target。
#### 返回这两个元素的下标。
#### 答案一定存在且唯一。


##  示例
>输入：

> nums = [2, 7, 11, 15], target = 9

>输出：

>  [0, 1]



```java

import static org.junit.Assert.*;

import org.junit.Test;

public class TwoSumTest {

	@Test
	public void testTwoSumA() {
		assertArrayEquals(new int[]{0, 1}, TwoSum.twoSum(new int[]{2, 7, 11, 15}, 9));
	}
	
	@Test
	public void testTwoSumB() {
		assertArrayEquals(new int[]{1, 2}, TwoSum.twoSum(new int[]{7, 2, 4, 1}, 6));
	}
	
	@Test
	public void testTwoSumC() {
		assertArrayEquals(new int[]{0, 3}, TwoSum.twoSum(new int[]{9, 8, 5, 1}, 10));
	}
}

```

