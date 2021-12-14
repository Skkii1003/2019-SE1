public class TortoiseHareRace {
    public void game(int hareSpeed, int hareSleepDuratioon, int tortoiseSpeed, int distance){
        //add some codes here
        Hare hare = new Hare(hareSpeed,hareSleepDuratioon);
        Tortoise tortoise = new Tortoise(tortoiseSpeed);

        double haretime = (double) hare.race(distance);
        double tortoisetime = (double) tortoise.race(distance - hareSleepDuratioon * tortoiseSpeed);

        if(haretime - tortoisetime > 0.0){
            tortoise.win();
        }
        else if((haretime - tortoisetime) == 0.0){
            System.out.print("Draw!");
        }
        else
            hare.win();
    }
}
