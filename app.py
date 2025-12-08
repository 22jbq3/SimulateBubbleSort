from random import randint


# BubbleSort implementation.
class SimulateBubbleSort():
    """A simulation of the bubble sort algorithm.
    """
    
    def __init__(self, lst: list[int]):
        """Return a SimulateBubbleSort object.

        >>> q1 = SimulateBubbleSort([1, 1, 1])
        >>> q1.lst
        [1, 1, 1]
        >>> q2 = SimulateBubbleSort([3, 2, 1])
        >>> q2.lst
        [3, 2, 1]
        >>> q3 = SimulateBubbleSort([4, 9, 2, 4])
        >>> q3.lst
        [4, 9, 2, 4]
        """
        self.lst = lst
        self.original_lst = lst.copy()


    def get_lst(self) -> list[int]:
        """Return this object's original lst attribute.

        >>> q1 = SimulateBubbleSort([1, 1, 1])
        >>> q1.get_lst()
        [1, 1, 1]
        >>> q2 = SimulateBubbleSort([3, 2, 1])
        >>> q2.get_lst()
        [3, 2, 1]
        >>> q3 = SimulateBubbleSort([4, 9, 2, 4])
        >>> q3.get_lst()
        [4, 9, 2, 4]
        """
        return self.original_lst


    def bubble_sort(self) -> list[tuple[int]]:
        """Return a list of indices which correspond to the sequence of swaps after bubble sort iterates
        on self.lst.

        >>> q1 = SimulateBubbleSort([4, 2, 7, 4])
        >>> q1.bubble_sort() == [(0, 1), (2, 3)]
        True
        >>> q2 = SimulateBubbleSort([1, 1, 1, 1])
        >>> q2.bubble_sort() == []
        True
        >>> q3 = SimulateBubbleSort([4, 3, 2, 1])
        >>> q3.bubble_sort() == [(0, 1), (1, 2), (2, 3), (0, 1), (1, 2), (0, 1)]
        True
        >>> q4 = SimulateBubbleSort([1, 2, 3, 5, 4])
        >>> q4.bubble_sort() == [(3, 4)]
        True
        """
        sequence = []

        # Store the length of the list and create a variable for early-exit.
        n = len(self.lst)
        swapped = True

        # Continue to iterate while swaps have occurred (that is, while the list is unsorted).
        while swapped:
            swapped = False
            j = 0

            # Iterate through all values in the list.
            while j < len(self.get_lst()) - 1:
                # Swap items and record their indices if a lower-index item is greater
                # in value than a higher-index item.

                # Additionally, set swapped = True to indicate that the list remains unsorted.
                if self.lst[j] > self.lst[j + 1]:
                    self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]
                    sequence.append((j, j + 1))
                    swapped = True
                j += 1

        # Return the sequence of swaps that must occur to sort the list.
        return sequence


    def perform_swap(self, index1: int, index2: int) -> None:
        """Swap the values in lst.original_lst at index1 and index2.

        >>> q1 = SimulateBubbleSort([1, 2, 5, 4])
        >>> q1.perform_swap(2, 3)
        >>> q1.get_lst() == [1, 2, 4, 5]
        True
        >>> q2 = SimulateBubbleSort([1, 1, 1, 1])
        >>> q2.perform_swap(2, 3)
        >>> q2.get_lst() == [1, 1, 1, 1]
        True
        >>> q3 = SimulateBubbleSort([5, 4, 3, 2, 1])
        >>> q3.perform_swap(0, 1)
        >>> q3.get_lst() == [4, 5, 3, 2, 1]
        True
        """
        self.original_lst[index1], self.original_lst[index2] = self.original_lst[index2], self.original_lst[index1]


# Gradio Implementation.
import gradio as gr
import pandas as pd
import random


# Generate a random list.
def generate_data():
    global df, random_list, bubble_sort_demo, display_list, sequence, sequence_index
    
    random_list = []
    for i in range(20):
        random_list.append(random.randint(1, 30))
        
    bubble_sort_demo = SimulateBubbleSort(random_list)
    display_list = random_list.copy()

    # Obtain the indices to swap.
    sequence = bubble_sort_demo.bubble_sort()
    sequence_index = 0

    # Setup the visualization.
    df = pd.DataFrame({
        "horizontal-values": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        "values": bubble_sort_demo.get_lst()
    })


generate_data()


with gr.Blocks() as demo:
    gr.HTML(
    """
    <body>
        <h1 style="font-size: 5vh; margin-bottom: 0.25%"><b><i>SimulateBubbleSort</i></b></h1>
        <h3 style="margin-top: 0px; margin-bottom: 20px;"><i>CISC 121: Introduction to Computing Science I</i></h3>
    
        <p style="margin-bottom: 50px;"><i>Press <b>STEP</b> below to begin sorting.</i></p>
    </body>
    """
    )

    
    # Implement the sorting functionality (the ability to update the bar graph).
    def swap_bars(swap: tuple[int]):
        # print('Original:', df)
        bubble_sort_demo.perform_swap(swap[0], swap[1])

        _df = pd.DataFrame({
            "values": bubble_sort_demo.get_lst()
        })
            
        df.update(_df)


    # Create the "STEP" button.
    plot = gr.BarPlot(df, height="65vh", x_title=" ", y_title=" ", x_axis_labels_visible=False, x="horizontal-values", y="values")
    with gr.Row():
        original_list = gr.HTML(
        f"""
        <p align="center" id="random-list">The Original List: {display_list}</p>
        """
        )
    with gr.Row():
        render_plot_button = gr.Button("STEP", variant="primary")
        restart_button = gr.Button("RESTART", variant="primary")


    @render_plot_button.click(outputs=plot)
    def display_bubble_sort():
        """Display the bubble sort algorithm visualization for the user. Called every button click.
        """
        global sequence_index
        
        # Swap the indices.
        if sequence_index < len(sequence):
            swap_bars(sequence[sequence_index])
            sequence_index += 1

            # Display the result for the user.
            return gr.BarPlot(df, height="65vh", x_title=" ", y_title=" ", x_axis_labels_visible=False, x="horizontal-values", y="values")
        else:
            gr.Markdown(
            """
            The list has been sorted!
            """
            )
            return gr.BarPlot(df, height="65vh", x_title=" ", y_title=" ", x_axis_labels_visible=False, x="horizontal-values", y="values")


    @restart_button.click(outputs=[original_list, plot])
    def restart():
        """Restart and regenerate the list and bar plots.
        """
        generate_data()
        display_bubble_sort()
        return [
            gr.HTML(
                f"""
                <p align="center" id="random-list">The Original List: {display_list}</p>
                """
            ),
            gr.BarPlot(df, height="65vh", x_title=" ", y_title=" ", x_axis_labels_visible=False, x="horizontal-values", y="values")
        ]


demo.launch(theme=gr.themes.Default(primary_hue="yellow"))


# Testing.
if __name__ == '__main__':
    import doctest
    doctest.testmod()

