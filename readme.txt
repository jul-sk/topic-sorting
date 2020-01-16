
This program is designed for the Heiligkreuztal Retreat run by GTC.

This program addresses the problem of assigning papers to students for the HKT retreat presentations. 
Students indicate which papers and general categories interest them in a Google form. 
Each student chooses five papers and ranks them based on their preferences. Additionally, each student ranks the categories
based on their preferences. The program will try to find the assignment of papers to students that maximizes the overall
satisfaction. The sorting is performed based on a genetic algorithm, described below.

To run the program, make sure that you have the Anaconda Python distribution installed.
Then execute the command 'python assign_GUI.py' from the Anaconda Prompt in the directory containing the scripts.

--------------google form------------------------------------

Currently the Google form creation process is manual, but could be improved by automatically entering
paper authors/titles from a spreadsheet into the google form. 

The form needs to follow this template to work properly with the code.

(A) What is your name? -> short answer text
(B) Please rank the categories -> multiple choice grid
	Rows: 
		1. [Name of Topic 1]
		2. [Name of Topic 2]
		3. [Name of Topic 3]
	Columns:
		Choice 1
		Choice 2
		Choice 3
(C) Please rank the individual papers -> multiple choice grid
	Rows:
		1. Some descriptor, e.g. Author's last name, title of first paper in Topic 1
		2. ....
		N. Author's last name, title of last paper in Topic 3
	Columns:
		Choice 1
		Choice 2
		Choice 3
		Choice 4
		Choice 5

** The list of papers in (C) should be organized according to
their topic (keeping the same order as (B)). Sorting within topics doesn't matter.

--------------input file------------------------------------

The input file can be obtained by downloading the responses from google forms (.csv)
The format should not be changed, i.e :
	- Rows are individual student responses
	- 1st column is a timestamp
	- 2nd column contains student names
	- 3rd to 5th columns contain category rankings
	- 6th to final columns contain paper rankings

--------------assignment algorithm---------------------------------

The genetic algorithm starts with a population of random assignment of papers to students.
Each assignment specifies which paper is assigned to each student, and each assignment is 
associated with a cost that measures the overall satisfaction of students with the assignment set 
(lower cost = higher satisfaction, details below). 

In each iteration, half of the population with the lowest costs is kept while the other half is discarded.
Each assignment in the selected half is mutated by swapping a random pair of papers in the set. 
The mutated assignments are combined with the original selected half to form a new population. 
The process is repeated for a specific number of iterations. Likewise, the entire process from generating
a random population to iteratively improving it is repeated a set number of times. Finally, the best
assignment is selected and saved in a file.

Cost definition:
For each student, each ranked paper is associated with the rank they chose for it (a number
from 1-5). Papers that were not ranked 1-5 are assigned a number greater than the last rank (6). 
For each assignment, the cost is defined as the sum of the numbers assigned to all of the papers.
Additionally, unselected papers are weighted differently based on the category rankings. This is 
set explicitly so that papers in the last-choice category receive a heavy penalty (e.g. 300), and 
in the second-choice category receive a smaller penalty (9). 
 
The code for this algorithm is defined in the file 'sorting_algorithm.py'.

--------------assignment GUI------------------------------------
The assignment GUI is based on the PyQt library and is defined in the file assign_GUI.py

--------------advanced options------------------------------------
Population size (default 100)
Number of iterations (default 50)
Number of full-algorithm repeats (default 50)

--------------limitations------------------------------------
Make sure Google form spelling matches code.. mainly for category options e.g. "Choice 1"
Let people know to rank 5 papers and all categories, even if they want fewer - results with fewer rankings are
untested
Double-check the number of papers per category as input to the sorting hat (errors crash the program)
Make sure this input (# papers per category) is entered in the same order as in the form

--------------output file------------------------------------
Just 2 columns, student's name and which paper they should present

--------------output graph------------------------------------
bar chart showing how the algorithm performed
Rank 1 = 1st choice
"1st choice topic" etc. indicates that the student didn't get any of their selected papers, 
but will get to present a paper in their 1st (or other) choice of seminar.