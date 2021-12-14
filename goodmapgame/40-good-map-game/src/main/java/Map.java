/**
 * Created by Shifang on 2017/10/24.
 * 地图，请补全部分方法的代码，如有必要，你可以添加一些属性和方法
 */
public class Map {
    private final String MAP_DEFAULT = "-";
    private int size;
    private Player d1;
    private Player d2;

    public Map(int size, Player d1, Player d2) {
        this.size = size;
        this.d1 = d1;
        this.d2 = d2;
    }

    /**
     * 请在此方法中编辑代码，参数由你自己定义
     * 返回是移动后的游戏结果
     * 若玩家都没有死亡，则返回 Result.DRAW；若 X 死亡，则返回 Result.Y_WIN；否则返回 Result.X_WIN
     * 在每一步移动后，
     * 1. 打印当前地图，玩家未隐身时用 X 或 Y 表示，隐身时用 x 或 y 表示，两个玩家不会重合，也不会移动到地图范围之外
     * 2. 打印当前两个玩家的血量
     *
     * @return
     */
    public Result move() {
        if(d1.getHealthPoint()==0)
            return Result.Y_WIN;
        else if(d2.getHealthPoint()==0)
            return Result.X_WIN;
        else
            return Result.DRAW;
    }

    /**
     * 请在此方法中编辑代码
     * 打印地图信息和玩家血量，输出格式请参见 README
     */
    public void print() {
        String[][] gamemap = new String[size][size];
        for(int i=0;i<size;i++){
            for(int j=0;j<size;j++){
                gamemap[i][j] = MAP_DEFAULT;
            }
        }

        gamemap[d1.getX()][d1.getY()] = d1.getSymbol();
        gamemap[d2.getX()][d2.getY()] = d2.getSymbol();

        System.out.print(" ");
        for(int i=0;i<size;i++){

            System.out.print(" " + i);
        }

        System.out.println("");

        for(int i = 0;i<size;i++){
            System.out.print(i);
            for(int j =0;j<size;j++){
                System.out.print(" "+gamemap[i][j]);
            }
            System.out.println("");
        }
        System.out.println("X : "+d1.getHealthPoint());
        System.out.println("Y : "+d2.getHealthPoint());
    }


}
