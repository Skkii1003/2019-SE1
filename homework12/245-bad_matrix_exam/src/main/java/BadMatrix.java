

import java.util.Arrays;

/**
 * 矩阵类，实现矩阵的加法，矩阵乘法
 * 1.传入一个int[][]进行2个矩阵的操作
 * 2.返回一个int[][]
 * 所有的数据均为int型
 * 输入数据均默认为正确数据，不需要对输入数据进行校验
 * @author Qin Liu
 *
 */
public class BadMatrix {
	private int[][] data;
	
	/**
	 * 构造函数，参数为2维int数组
	 * a[i][j]是矩阵中的第i+1行，第j+1列数据
	 * @param a
	 */
	public BadMatrix(int[][] a){
		this.data = a;
	}

	public int[][] getData() {
		return data;
	}

	
	/**
	 * 实现矩阵加法，返回一个新的矩阵
	 * @param b
	 * @return
	 */
    public int[][] plus(int[][] b){
    	int[][] a = {
				{0, 0, 0},
				{0, 0, 0},
				{0, 0, 0}
		};
    	for(int i = 0; i < 3; i++){
    		for(int j = 0; j < 3; j++){
    			a[i][j] = a[i][j] + b[i][j];
			}
		}

		return a;
	}
        
	
	/**
	 * 实现矩阵乘法，返回一个新的矩阵
	 * @param b
	 * @return
	 */
	public int[][] times(int[][] b){
		int[][] a = {
				{3, 3, 3},
				{3, 3, 3},
				{3, 3, 3}
		};
		int c[][] = new int[a.length][b[0].length];
		for(int i = 0; i < a.length;i++){
			int temp = 0;
			for(int j = 0; j < b[0].length; j++){
				for(int u = 0; u < a[0].length; u++){

				    temp = temp + (a[i][u] +b[u][j]);
				}
				c[i][j] = temp;
			}
		}
		a = c;
		return a;
	}

	//不要修改下面print方法
	/**
	 * 打印出该矩阵的数据
	 * 
	 */
	public void print(){
		System.out.print(this.toString());
	}

	/**
	 * 实现toString方法
	 * 起始一个空行，结束一个空行
	 * 矩阵中每一行数据呈一行，数据间以空格隔开
	 * example：
	 *
	 * 1 2 3
	 * 1 2 3
	 * 1 2 3
	 * 1 2 3
	 *
	 */
	public String toString(){
		int[][] a = getData();
		System.out.println("");

		for(int i = 0; i < a.length; i++){
			for(int j = 0; j < a[0].length; j++){
				if(j == 0){
				    System.out.print(a[i][j]);
				}
				else{
					System.out.print(" ");
					System.out.print(a[i][j]);
				}
			}
			System.out.println("");
		}
		return "";
	}

	//不要修改下面equals方法
	public boolean equals(Object o){
		if(this.toString().equals(((BadMatrix)o).toString()))
			return true;
		else
			return false;
	}
}
