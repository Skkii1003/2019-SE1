package cn.edu.nju.TicTacToe;
public class Board {
	/**
	 * 成员变量的初始化代码请修改，请灵活选择初始化方式
	 * 必要时可添加成员变量
	 */
	protected char[][] cells;
	protected GameChessStrategy chessStrategy = new GameChessStrategy();
	protected anothoerGameChessStrategy anothoerStrategy = new anothoerGameChessStrategy();
	protected GameWinStrategy_HVD winStrategyhvd = new GameWinStrategy_HVD();
	protected GameWinStrategy_HV winStrategyhv = new GameWinStrategy_HV();
	protected Player player = Player.X;

	/**
	 * 请修改构造方法，并添加合适的构造方法
	 */

	public Board(int boardSize){
		cells = new char[boardSize][boardSize];
		for(int i=0; i<boardSize; i++){
			for(int j=0; j<boardSize; j++){
				cells[i][j] = '_';
			}
		}
	}

	/**
	 * @param move 下棋的位置
	 * @return 落棋之后的结果
	 */
	public Result nextMove(String move,String gamemode, String[] moves) {
		if(gamemode=="00"){
			chessStrategy.putChess(cells, nextPlay(), move);
			return winStrategyhvd.check(cells);
		}
		else if(gamemode=="01"){
			chessStrategy.putChess(cells, nextPlay(), move);
			return winStrategyhv.check(cells);
		}
		else if(gamemode=="10"){
			anothoerStrategy.putChess(cells, nextPlay(), move, moves);
			return winStrategyhvd.check(cells);

		}
		else{
			anothoerStrategy.putChess(cells, nextPlay(), move, moves);
			return winStrategyhv.check(cells);
		}
	}
	
	/**
	 * @return 下一个落棋的玩家
	 */
	protected Player nextPlay(){
		Player res = player;
		player = player == Player.X ? Player.O : Player.X;
		return res;
	}
	
	/**
	 * 棋盘的输出方法，根据需要进行修改
	 */
	public void print(int size){
		String[] word = {"A","B","C","D","E","F","G","H","I"};
		System.out.print(" ");

		for(int i = 0 ;i<size;i++){
			System.out.print(" "+word[i]);
		}
		System.out.println("");

		for(int i=0 ;i<size; i++){
			System.out.print(i+1);
			for(int j=0; j<size; j++){
				System.out.print(" "+cells[i][j]);
			}
			System.out.println();
		}
	}
}