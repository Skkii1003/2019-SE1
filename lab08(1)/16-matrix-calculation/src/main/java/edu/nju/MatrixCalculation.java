package edu.nju;
import java.util.*;
/**
 * 实现矩阵的加法、乘法以及控制台输出
 * 其中加法和乘法需要有两种实现方式
 * 1.传入一个矩阵进行2个矩阵的操作
 * 2.从控制台（console）读入一个矩阵，再进行操作
 * 所有的数据均为int型
 * 输入数据均默认为正确数据，不需要对输入数据进行校验
 * @author Ray Liu & Qin Liu
 */
public class MatrixCalculation {
	
	/**
	 * 实现矩阵加法，返回一个新的矩阵
	 * @return result matrix = A + B
	 */
	public int[][] plus(int[][] A, int[][] B){
		// TODO
		for(int i = 0;i<A.length;i++){
			for(int j = 0; j < A[0].length; j++){
				A[i][j] = A[i][j] + B[i][j];
			}
		}
		return A;
	}
	
	/**
	 * 实现矩阵乘法，返回一个新的矩阵
	 * @return result matrix = A * B
	 */
	public int[][] times(int[][] A, int[][] B){
		// TODO
		if(A.length==0){
			int[][] result = new int[0][0];
			return result;
		}
		int[][] c = new int[A.length][B[0].length];




		for(int i = 0;i<A.length;i++){
			for(int j = 0;j<B[0].length;j++){
				int temp = 0;
				for(int x = 0;x<A[0].length;x++){
					temp += A[i][x] * B[x][j];
				}
				c[i][j] = temp;
			}
		}
		return c;
	}
	
	/**
	 * 从控制台读入矩阵数据，进行矩阵加法，读入数据格式如下：
	 * m n
	 * m * n 的数据方阵，以空格隔开
	 * 连续读入2个矩阵数据
	 * example:
	 * 4 3
	 * 1 2 3
	 * 1 2 3
	 * 1 2 3
	 * 1 2 3
	 * 4 3
	 * 1 2 3
	 * 1 2 3
	 * 1 2 3
	 * 1 2 3
	 * 返回一个新的矩阵
	 */
	public static int[][] input(){
		Scanner in = new Scanner(System.in);

		int m = in.nextInt();
		int n = in.nextInt();

		if(m==0 || n==0){
			return new int[0][0];
		}
		int[][] matrix = new int[m][n];

		for(int i =0;i<m;i++){
			for(int j=0;j<n;j++){
				matrix[i][j] = in.nextInt();
			}
		}
		return matrix;
	}

	public int [][] plusFromConsole(){
		// TODO
		Scanner in = new Scanner(System.in);

		int m1 = in.nextInt();
		int n1 = in.nextInt();

		if(m1==0 || n1==0){
			return new int[0][0];
		}
		int[][] a = new int[m1][n1];
		for(int i =0;i<m1;i++){
			for(int j=0;j<n1;j++){
				a[i][j] = in.nextInt();
			}
		}

		int m2 = in.nextInt();
		int n2 = in.nextInt();

		if(m2==0 || n2==0){
			return new int[0][0];
		}
		int[][] b = new int[m2][n2];
		for(int i =0;i<m2;i++){
			for(int j=0;j<n2;j++){
				b[i][j] = in.nextInt();
			}
		}
		return plus(a,b);
	}

	/**
	 * 输入格式同上方法相同
	 * 实现矩阵的乘法
	 * 返回一个新的矩阵
	 */
	public int[][] timesFromConsole(){
		// TODO
		Scanner in = new Scanner(System.in);

		int m1 = in.nextInt();
		int n1 = in.nextInt();

		if(m1==0 || n1==0){
			return new int[0][0];
		}
		int[][] a = new int[m1][n1];
		for(int i =0;i<m1;i++){
			for(int j=0;j<n1;j++){
				a[i][j] = in.nextInt();
			}
		}

		int m2 = in.nextInt();
		int n2 = in.nextInt();

		if(m2==0 || n2==0){
			return new int[0][0];
		}
		int[][] b = new int[m2][n2];
		for(int i =0;i<m2;i++){
			for(int j=0;j<n2;j++){
				b[i][j] = in.nextInt();
			}
		}

		return times(a,b);
	}

	/**
	 * 打印出该矩阵的数据
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
	public void print(int[][] A){
		// TODO
		System.out.println("");

		for(int i = 0;i < A.length;i++){
			for(int j = 0;j<A[0].length;j++){
				if(j != 0){
					System.out.print(" ");
				}
				System.out.print(A[i][j]);
			}
			System.out.println("");
		}
	}
}
