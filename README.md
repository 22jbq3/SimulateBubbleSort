# SimulateBubbleSort
A simple simulation of the bubble sort algorithm on a randomly generated list of size twenty. Made with Gradio.

The bubble sort algorithm was selected because it offers a beginner-friendly introduction to sorting in performing swaps whilst iterating through a list. It provides a basis for algorithmic thinking and comprehending other sorting algorithms.

## Demonstration Screenshot
![Bubble sort, visualized.](/SimulateBubbleSort_Visualization.png)


### Sample Test Cases and Example Runs
#### Example Run 1 and its Results
![SimulateBubbleSort - Example Run 1 Initialized](/SimulateBubbleSort_Example_Run_1.png)
![SimulateBubbleSort - Example Run 1 Finished](/SimulateBubbleSort_Example_Run_1_Finished.png)

#### Example Run 2 and its Results
![SimulateBubbleSort - Example_Run_2_Initialized](/SimulateBubbleSort_Example_Run_2.png)
![SimulateBubbleSort - Example_Run_2_Finished](/SimulateBubbleSort_Example_Run_2_Finished.png)

*Please note that we include further test cases in the Python file itself, prior to defining functions.*


## Breakdown and Computational Thinking
We briefly describe the bubble sort algorithm utilizing the four pillars of computational thinking.

### Decomposition
**Input Handling:** read a list of integers.

**Data Processing:** 
* We begin by storing the length of the list.
* This bubble sort implementation shall include early-exit functionality, so a `swapped = True` variable is initialized.
* We iterate while `swapped` is `True`.
* We begin iterating by setting  `swapped = False` (for early exit).
* We iterate through index `0` of the list to the conclusion of the list, swapping consecutive values in the list if an item at a lower index is greater than an item at a higher index. Additionally, if this is the case, we set `swapped = True` to continue iterating through the list.
* We note that if `swapped` is never reset to `True`, then the outer loop condition fails and we may exit the bubble sort algorithm early.

**Output Display:** we return a sorted version of the input list in nondecreasing order.

### Pattern Recognition
We notice that we can sort the list by applying the same swapping strategy on consecutive items. As such, we apply this technique (swapping consecutive items if the lower-index item is greater in value than the next higher-index item) as we iterate through the list until all items in the list are completely sorted.

### Abstraction
We focus on the list passed into the function and ensuring that it becomes sorted in nondecreasing order. As such, we must consider the values of consecutive items in the list and whether they are greater than or less than each other (the case where they are equal can belong to either of the aforementioned categories).

As the list of integers is the only input, there are relatively few details that we may neglect. We may neglect details such as whether the integers are already in sorted order (as this is what the bubble sort algorithm shall accomplish), and other minute details such as the parity of individual integers in the list.


The user shall be shown the values in the list that are being swapped as they step through the bubble sort algorithm. The user shall have the ability to step through individual steps of the bubble sort algorithm. 
Details not shown to the user can include the particular code implementation (such as the list indices being tracked, the state of the `swapped` variable, and so forth).

### Algorithmic Thinking
* **Input:** a list of integers.
* **Output:** the same list of integers, now sorted in nondecreasing order.
* **Constraints:** the list size shall be limited to 20 items. Each integer in the list shall be between the values of 1 and 30 (inclusive).

#### Flowchart
![SimulateBubbleSort Flowchart.](/SimulateBubbleSort_Flowchart.png)

## Steps to Run
1. Navigate to the below Hugging Face Link.
2. Press the "STEP" button to see individual steps/swaps that occur in bubble sort.
3. Continue to press "STEP" until the randomly generated list is completely sorted!

## Hugging Face Link
https://huggingface.co/spaces/22jbq3/SimulateBubbleSort

## Author and Acknowledgement
This project was created by Robbie Podrebarac, a student. It was created for CISC 121: Introduction to Computing Science I taught in Fall 2025.
