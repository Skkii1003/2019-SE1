public class Hare extends AnimalRacer {
    int sleepDuration;
    int x;

    Hare(int s, int d ){
        x = s;
        sleepDuration = d;
        //add some codes here
    }

    //add codes here
    public double race(int distance) {
        double time = (double) distance / (double) x;
        return time;
    }

    //add codes here
    public void win() {
        System.out.print("Hare Win!");
    }
}
