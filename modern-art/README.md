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
We can have two arrays of size M and size N respectively initialized with 0's, representing the number of operations done for row X and col Y
When running through the operations done, we increase the count by 1 for the row/col and their position.

Example:
Given operation R/C Integer

R 1 would increase row_color(i-1) by 1.

After running through all operations, we count how many rows are odd and how many cols are odd by going through the two lists and performing a modulo operation.

And simply use this mathematical relationship to determine the total number of gold cells:
gold = odd_rows x (cols - odd_cols) + odd_cols x (rows - odd_rows)

**Why does this work?**
Think about it for a second.
When you paint a row, you paint a number of cols.
And vice versa, when you paint a col, you paint rows.
So there's a mathematical way to represent the number of gold cells there are.
The simplest case: paint a col once.
So you would have painted from the col side once, which implies you have painted a row gold.
But what if you performend an operation based on the row? That would mean you also painted a col gold.
So it becomes a math problem. Take a 3x3 grid for example.
I perform: R 1
That would mean the grid looks like:
GGG
BBB
BBB
I would have one odd row operaiton, and 0 odd col operations. So it would simply be 1 x 3 gold cells.
I perform: C 1
BGG
GBB
GBB
I would have one odd row operation and one odd col operaiton. How can we mathematically model this?
The number of gold cells based on odd rows is dependent on how many odd_cols there are as well. If you had odd_cols that was the same number as cols, then you would have effectively undid the row operation you've done.
So a mathy way to represent this is:
**odd_rows x (cols - odd_cols)** = Number of gold cells from row operations
And don't forget about the columns.
**odd_cols x (rows - odd_rows)** = Number of gold cells from col operations
Combining the two, you get the total number of gold cells.
