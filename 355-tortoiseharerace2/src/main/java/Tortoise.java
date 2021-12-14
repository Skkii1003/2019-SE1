public class Tortoise extends AnimalRacer{
    int x;
    Tortoise(int s){
        //add some codes here
        x = s;
    }

    //add codes here
    public double race(int distance) {
        double time = (double) distance / (double) x;
        return time;
    }

    //add codes here
    public void win() {
        System.out.print("Tortoise Win!");
    }
}
