/**
 * 矩阵类，实现矩阵的加法，矩阵乘法，点乘以及转置方法
 * 其中加法和点乘方法需要有两种实现方式
 * 1.传入一个MyMatrix对象进行2个矩阵的操作
 * 2.从控制台（console）读入一个矩阵数据，再进行操作
 * 所有的数据均为int型
 * 输入数据均默认为正确数据，不需要对输入数据进行校验
 * @author Ray Liu & Qin Liu
 *
 */
import java.util.*;

public class MyMatrix {
	private int[][] data;
	
	/**
	 * 构造函数，参数为2维int数组
	 * a[i][j]是矩阵中的第i+1行，第j+1列数据
	 * @param a
	 */
	public MyMatrix(int[][] a){
		this.data = a;
	}

	public int[][] getData() {
		return data;
	}

	/**
	 * 实现矩阵加法，返回一个新的矩阵
	 * @param B
	 * @return
	 */
	public MyMatrix plus(MyMatrix B){
		MyMatrix A = new MyMatrix(getData());

		for(int i = 0;i<A.getData().length;i++){
			for(int j = 0; j < A.getData()[0].length; j++){
				A.getData()[i][j] = A.getData()[i][j] + B.getData()[i][j];
			}
		}
		return  A;
	}

	
	/**
	 * 实现矩阵乘法，返回一个新的矩阵
	 * @param B
	 * @return
	 */
	public MyMatrix times(MyMatrix B){
		int[][] b = B.getData();

		if(data.length==0||b.length==0){
			return new MyMatrix(new int[0][0]);
		}
		int[][] result =new int[data.length][b[0].length];

		for(int i = 0;i<data.length;i++){
			for(int j = 0;j<b[0].length;j++){
				int temp = 0;
				for(int x = 0; x < data[0].length;x++){
					temp += data[i][x] * b[x][j];
				}
				result[i][j] = temp;
			}
		}
		return new MyMatrix(result);
	}
	
	/**
	 * 实现矩阵的点乘，返回一个新的矩阵
	 * @param b
	 * @return
	 */
	public MyMatrix times(int b){
		int[][] result =new int[data.length][data[0].length];

		for(int i=0;i<data.length;i++){
			for(int j=0;j<data[0].length;j++){
				result[i][j] = b * data[i][j];
			}
		}

		return new MyMatrix(result) ;
	}
	
	/**
	 * 实现矩阵的转置，返回一个新的矩阵
	 * @return
	 */
	public MyMatrix transpose(){
		int[][] result = new int[data[0].length][data.length];

		for(int i=0;i<data[0].length;i++){
			for(int j=0;j<data.length;j++){
				result[i][j] = data[j][i];
			}
		}
		return new MyMatrix(result);
	}
	
	/**
	 * 从控制台读入矩阵数据，进行矩阵加法，读入数据格式如下：
	 * m n
	 * m * n 的数据方阵，以空格隔开
	 * example:
	 * 4 3
	 * 1 2 3 
	 * 1 2 3
	 * 1 2 3
	 * 1 2 3
	 * 返回一个新的矩阵
	 * @return
	 */
	public MyMatrix plusFromConsole(){
		Scanner in = new Scanner(System.in);

		int m1 = in.nextInt();
		int n1 = in.nextInt();

		if(m1==0 || n1==0){
			return new MyMatrix(new int[0][0]);
		}
		int[][] result = new int[m1][n1];
		for(int i =0;i<m1;i++){
			for(int j=0;j<n1;j++){
				result[i][j] = in.nextInt();
			}
		}
		return plus(new MyMatrix(result));
	}
	
	/**
	 * 输入格式同上方法相同
	 * 实现矩阵的乘法
	 * 返回一个新的矩阵
	 * @return
	 */
	public MyMatrix timesFromConsole(){
		Scanner in = new Scanner(System.in);

		int m1 = in.nextInt();
		int n1 = in.nextInt();

		if(m1==0 || n1==0){
			return new MyMatrix(new int[0][0]);
		}
		int[][] result = new int[m1][n1];
		for(int i =0;i<m1;i++){
			for(int j=0;j<n1;j++){
				result[i][j] = in.nextInt();
			}
		}
		return times(new MyMatrix(result));
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
	public void print(){
		System.out.println("");

		for(int i = 0;i < data.length;i++){
			for(int j = 0;j<data[0].length;j++){
				if(j != 0){
					System.out.print(" ");
				}
				System.out.print(data[i][j]);
			}
			System.out.println("");
		}
		System.out.println("");
	}
}
