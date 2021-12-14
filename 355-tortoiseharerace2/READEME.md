一只兔子和一只乌龟进行赛跑，请判断出兔子和乌龟谁能获得胜利。
其中Hare为兔子的类，Tortoise为乌龟的类。在等长的赛跑(distance)途中，乌龟和兔子同时出发。兔子会先跑一段，然后进入一次的睡眠(sleepDuration)，然后再跑到终点。而乌龟会一刻不停地跑下去。乌龟和兔子的速度(speed)是不等的。
请在相应的类方法和TortoiseHareRace类中game方法中补上相应的代码。
如果兔子胜利，则输出Hare Win!;乌龟胜利，则输出Tortoise Win!;平局则输出Draw!。（最后无"\n"）



输入：
    //Game的定义 public void game(int hareSpeed, int hareSleepDuratioon, int tortoiseSpeed, int distance)
    game(5,80,1,100)

输出：
    Draw！

输入：
    //Game的定义 public void game(int hareSpeed, int hareSleepDuratioon, int tortoiseSpeed, int distance)
    game(5,79,1,100)

输出：
    Hare Win！



```java
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static org.junit.Assert.assertEquals;

public class TortoiseHareRaceTest {
    InputStream in = null;
    PrintStream out = null;

    InputStream inputStream = null;
    OutputStream outputStream = null;

    @Before
    public void setUp() {
        in = System.in;
        out = System.out;

        outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

    }

    @After
    public void tearDown() {
        System.setIn(in);
        System.setOut(out);
    }

    @Test
    public void test1() {
        check(5, 79, 1, 100, "Hare Win!");
    }

    @Test
    public void test2(){
        check(5,80,1,100,"Draw!");
    }

    @Test
    public void test3(){
        check(5,81,1,100,"Tortoise Win!");
    }

    @Test
    public void test4(){
        check(5,30,2,99,"Tortoise Win!");
    }

    private void check(int hareSpeed, int hareSleepDuration, int tortoiseSpeed, int distance, String expected) {

        TortoiseHareRace thr = new TortoiseHareRace();
        thr.game(hareSpeed, hareSleepDuration, tortoiseSpeed, distance);

        String output = outputStream.toString();

        assertEquals(expected, output);

    }

}

```

