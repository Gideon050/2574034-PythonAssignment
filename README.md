# 2574034-PythonAssignment
The program is designed to process an input file containing text data (in this case, trees.txt). It generates three-letter abbreviations for words in each line of the input text and computes scores for these abbreviations based on specific rules for letter positions and values. The program then writes the original lines from the input file along with their corresponding abbreviations and scores to an output file.

The script processes the input data and computes the abbreviation, considering word positions and conditions for letter values. If a letter is the first letter of a word, its value is 0. For the last letter of a word, if it's 'E', the score is set to 20; otherwise, it's set to 5.

It identifies duplicates in the generated abbreviations and handles them by altering the last character of the abbreviation to ensure unique abbreviations.

Additionally, it calculates a score for each abbreviation based on specific rules regarding letter positions and values. If a letter is neither the first nor last letter of a word, its value is the sum of a position value (1 for the second letter of a word, 2 for the third letter, and 3 for any other position), its value is calculated based on its position and the provided values from the ‘values.txt’ file. This result is displayed in the shell window.

Finally, it writes both the original lines from the input file and their corresponding abbreviations to the output file.
The code successfully generates three-letter abbreviations for input text, handles duplicate abbreviations, and calculates scores based on specified rules for letter positions and values. The resulting outcome is the list of tree and abbreviations with the lowest possible scoring derived after computations.

The useful-testing-results.docx is a file that consists of two tables, which have been populated to display some of the results of the abbreviations and corresponding scoring obtained during the code testing phase.
