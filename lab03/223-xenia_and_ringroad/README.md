## Xenia and Ringroad

### Description

​	Xenia lives in a city that has *n* houses built along the main ringroad. The ringroad houses are numbered 1 through *n* in the clockwise order. The ringroad traffic is one way and also is clockwise.

​	Xenia has recently moved into the ringroad house number 1. As a result, she's got *m* things to do. In order to complete the *i*-th task, she needs to be in the house number *a*<sub>i</sub> and complete all tasks with numbers less than *i*. Initially, Xenia is in the house number 1, find the minimum time she needs to complete all her tasks if moving from a house to a neighboring one along the ringroad takes one unit of time.

### Input

The first line contains two integers *n* and *m* (2 ≤ *n* ≤ 10<sup>5</sup>, 1 ≤ *m* ≤ 10<sup>5</sup>). The second line contains *m* integers *a*<sub>1</sub>, *a*<sub>2</sub>, ..., *a*<sub>m</sub> (1 ≤ *a*<sub>i</sub> ≤ *n*). Note that Xenia can have multiple consecutive tasks in one house.

### Output

Print a single integer — the time Xenia needs to complete all tasks.

#### Input1

```
4 3
3 2 3
```

#### Output1

```
6
```

#### Input2

```
4 3
2 3 3
```

#### Output2

```
2
```

### Note

In the first test example the sequence of Xenia's moves along the ringroad looks as follows: 1 → 2 → 3 → 4 → 1 → 2 → 3. This is optimal sequence. So, she needs 6 time units.

