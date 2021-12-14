/**
 * Created by lujxu on 2017/10/25.
 */
public class Map {
    private final String MAP_DEFAULT="-";
    private  int size;
    private Player d1;
    private Player d2;

    public Map(int size, Player d1, Player d2){
        setSize(size);
        this.d1=d1;
        this.d2=d2;
    }

    /**
     * 请在此方法中编辑代码
     * 返回当前地图中两个player的位置信息，或二者位置重合，则返回枚举类Result中的ENCOUNTER; 否则，返回DRAW
     * @return
     */
    public Result resultEvaluation(){
        if(d1.getX()==d2.getX()&&d1.getY()==d2.getY())
            return Result.ENCOUNTER;
        else
            return Result.DRAW;
    }

    /**
     * 请在此方法中编辑代码
     * 打印地图信息
     * player的位置用Player.getSymbol()表示，其余位置用MAP_DEFAULT表示，注意每个位置之间都用空格隔开
     * 若x,y二者重合则优先输出x
     */
    public void  print(){
        String[][] gamemap = new String[size][size];
        for(int i=0;i<gamemap.length;i++){
            for(int j=0;j<gamemap[0].length;j++){
                gamemap[i][j] = MAP_DEFAULT;
            }
        }
        gamemap[d1.getX()][d1.getY()] = d1.getSymbol();
        if(resultEvaluation()==Result.DRAW){
            gamemap[d2.getX()][d2.getY()] = d2.getSymbol();
        }
        for(int i = 0;i<gamemap.length;i++){
            for(int j =0;j<gamemap[0].length;j++){
                if(j==0)
                    System.out.print(gamemap[i][j]);
                else
                    System.out.print(" "+gamemap[i][j]);
            }
            System.out.println("");
        }
    }

    public void setSize(int size) {
        this.size = size;
    }

}
