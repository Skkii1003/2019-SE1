public class Game {
    
    //游戏主方法playGame
    //输入为对弈双方轮番落子的位置，以英文逗号为间隔，X先走
    public boolean straight_win(String[][] line,String tar){
        for(int i=0;i<line[0].length;i++){
            if(line[0][i]== tar && line[1][i] == tar && line[2][i] == tar){
                return true;
            }
        }
        return false;
    }

    public boolean row_win(String[] line,String tar){
        if(line[0]==tar &&line[1]==tar && line[2]==tar){
            return true;
        }
        return false;
    }

    public boolean cross_win(String[][] line,String tar){
        if(line[0][0]==tar && line[1][1]== tar && line[2][2] == tar){
            return true;
        }
        if(line[2][0]==tar && line[1][1]==tar && line[0][2] == tar){
            return true;
        }
        return false;
    }

    public void output(String[][] line){
        System.out.println("  A B C");
        for(int i = 0;i<3;i++){
            System.out.print(i+1);
            for(int j=0;j<3;j++){
                System.out.print(" "+line[i][j]);
            }
            System.out.println("");
        }
    }

    public Result playGame(String s){
        String[][] chess = {{"_" , "_" , "_"} , {"_" , "_" , "_"} , {"_" , "_" , "_"}};
        s = s.replace("A","0");
        s = s.replace("B","1");
        s = s.replace("C","2");

        String[] order = s.split(",");
        //System.out.println(s);

        for(int i =0;i<order.length;i++){
            int row = Integer.parseInt(String.valueOf(order[i].charAt(1))) - 1;
            int line = Integer.parseInt(String.valueOf(order[i].charAt(0)));

            if(i%2==0){
                chess[row][line] = "X";
                output(chess);
                if(straight_win(chess,"X")||row_win(chess[row],"X")||cross_win(chess,"X")){
                    return Result.X_WIN;
                }
            }
            else{
                chess[row][line] = "O";
                output(chess);
                if(straight_win(chess,"O")||row_win(chess[row],"O")||cross_win(chess,"O")){
                    return Result.O_WIN;
                }
            }
        }
        return Result.DRAW;
    }

    
    public static void main(String[] args){
        Game game = new Game();
        Result result = game.playGame("B2,C2,C1,A3,B3,B1,A2,B2,C3,A1,A3,B3,C2,B1,B2,A2,A1,C1,C3");
        System.out.println(result);
    }
}
