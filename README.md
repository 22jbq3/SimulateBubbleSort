# SimulateQuickSort
A simple simulation of the quicksort algorithm. 

The quicksort algorithm was selected because one seeks to better understand the algorithm's implementation and its recursive nature. This will aid in visualizing the algorithm and provide a better understanding of recursion and recursive sorting algorithms. 

## Demonstration Screenshot
[TODO!]

## Breakdown and Computational Thinking
We briefly describe the quicksort algorithm utilizing the four pillars of computational thinking.

### Decomposition
**Input Handling:** read a list of integers.

**Data Processing:** 
* The base case occurs when the input list has a length less than 2. We return this list.
* We calculate the pivot utilizing a random value in the list.
* We track the items in the list in a sublist that contains all items less than the pivot, all items equal to the pivot, and all items greater than the pivot.
* We recursively call quicksort on the three sublists.
* We return the three sublists concatenated together.

**Output Display:** we return a sorted version of the input list in nondecreasing order.

### Pattern Recognition
We notice that we can sort the list by applying the same pivoting strategy on each sublist. As such, we apply the same sorting technique (selecting a random pivot and dividing the list into sublists where all elements are less than the pivot, equal to the pivot, and greater than the pivot) and sort each of the said three sublists in the same manner (that is, selecting a pivot for each of the sublists and repeating the same dividing steps).

### Abstraction
[!TODO HERE!]

### Algorithm Design

#### Flowchart

## Steps to Run

## Hugging Face Link

## Author and Acknowledgement
This project was created by Robbie Podrebarac, a student. It was created for CISC 121: Introduction to Computing Science I taught in Fall 2025.
