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
We focus on the list passed into the function and ensuring that the list becomes appropriately sorted recursively in taking into consideration its pivot. As such, we must consider each value in the list of integers and whether or not they are sorted relative to the chosen pivot.

As the list of integers is the only input, there are relatively few details that we may neglect. We may neglect details such as whether the integers are positive or negative (that is, whether the values themselves are positive or negative). 

(We note that we must still consider whether some values are greater than or less than each other (and hence whether or not the list of integers is sorted), the number of values in the list, and so forth.)

### Algorithmic THinking
* **Input:** a list of integers.
* **Output:** the same list of integers, now sorted in nondecreasing order.
* **Constraints:** the list size shall be limited to 100 items. Each integer in the list shall be less than the largest integer Python's integer data type can store.

#### Flowchart
![SimulateQuickSort flowchart.](/SimulateQuickSort_Flowchart.png)

## Steps to Run


## Hugging Face Link

## Author and Acknowledgement
This project was created by Robbie Podrebarac, a student. It was created for CISC 121: Introduction to Computing Science I taught in Fall 2025.
