# CCC '21 S2 - Modern Art

**[Problem Link](https://dmoj.ca/problem/ccc21s2)**

**Intuition:**
At first, I wanted to simulate the whole grid which is rather simple to do. A operation would just be a traveral on the grid, changing B to G or G to B. Afterwards, I would count the number of 'G' cells and print that as the answer.

Well that didn't work

The potential input size is in the millions, so a quadratic runtime is definitely not ideal. So I had to think of a way to get the answer in a O(n) runtime or similar.

It was important to note that we are essentially toggling between B and G, so there was a relationship of having a odd number of operations and a even number of operations done on a particular cell.

We know that all cells are initially Black, so if we do perform a operation based on a row or column, that particular part turns Gold on the first operation.

So we can boil it down to:
Odd Operation: The cells are gold
Even Operation: The cells are black

However, how can we account for an intersection? For example, if I do these operations on a 3x3 grid:
R 1
C 1

The resulting grid will look like:
BGG
GBB
GBB

That one cell at the very top left corner is Black. How could we do this without simulating the whole grid?

**Solution**
f
