🎯 AP. Organizing Frame Ranges

Task Objective

In this task, you will:

Work with a list of frame ranges stored as tuples (shot_name, start_frame, end_frame).

Use list comprehension to extract the names of shots that have more than 150 frames.

Use dictionary comprehension to map each shot to the total number of frames in its range.

Print the results to verify your solution.

Instructions

Create a list of tuples, where each tuple contains (shot_name, start_frame, end_frame).

Use a list comprehension to filter only the shots where (end_frame - start_frame) > 150.

Use a dictionary comprehension to map each shot to its total frame count (end_frame - start_frame + 1).

Print the filtered list of long shots.

Print the dictionary showing the frame counts of all shots.

Sample Output

Shots with more than 150 frames:
['shot002', 'shot004']

Frame Counts:
{'shot001': 101, 'shot002': 201, 'shot003': 121, 'shot004': 301}


