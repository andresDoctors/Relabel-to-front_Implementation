# Relabel-to-front_Implementation

**Relabel-to-front** is a type of push-relabel algorithm used for solving the **maximum flow problem** in a directed graph. The maximum flow problem involves finding the maximum amount of flow that can be sent from a source node to a sink node in the graph, subject to capacity constraints on the edges.

The relabel-to-front algorithm has a runtime of O(V^3), where V is the number of nodes in the graph. However, it has been shown to be faster in practice than other push-relabel algorithms, such as the generic push-relabel algorithm and the highest-label algorithm.

## Input

Networks are represented in text files with a DIMACS-like format:

* At the top you can have comment lines that start with a `c`
  ```
  c This line is a comment.
  ```

* Then comes the *problem line*, which starts with a `p` and then says how many arcs and vertexes there are. For instance, here is a problem line that says this is a MAX problem with 6 vertexes and 8 arcs:
  ```
  p max 6 8
  ```

* Then there are 2 lines that start with `n` and indicates the name of `sink`, `source` vertexes.
These two lines mean that the `source` is called `s` and `sink` is called `t`:
  ```
  n s s
  n t t
  ```

* Finally the arcs are listed. They start an `a`, followed by the end-points names and capacity
  ```
  a  s  a  5
  a  s  b  2
  a  a  b  2
  a  a  c  3
  a  b  d  4
  a  c  d  1
  a  c  t  2
  a  d  t  5
  ```

Putting it all together.

![alt text](https://raw.githubusercontent.com/andresDoctors/Relabel-to-front_Implementation/main/readme-media/ExampleFlowNetwork.png)

## Output

The output has pretty much the same format, we just add:
  * a new column when describing the arcs with de actual flow
  ```
  a  s  a  5  5
  a  s  b  2  2
  a  a  b  2  2
  a  a  c  3  3
  a  b  d  4  4
  a  c  d  1  1
  a  c  t  2  2
  a  d  t  5  5
  ```

  * a new line with the maximum flow
  ```
  7
  ```

  * a new line to check the returned Network holds flow restriction
  ```
  holds restrictions:True
  ```

  * a new line per vertex starting with `u` and showing their excess
  ```
  u s -7
  u t 7
  u a 0
  u b 0
  u c 0
  u d 0
  ```

![alt text](https://raw.githubusercontent.com/andresDoctors/Relabel-to-front_Implementation/main/readme-media/ExampleFlowNework2.png)

## How to use

Just write an input file in the `.\in` folder with the format decribed above and run
```console
python .\excecute.py
```
You can find the response in `.\out`