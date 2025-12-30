# Rule-Based Extractive Text Summarizer

This project implements a rule-based extractive text summarizer in Python. 
It generates concise summaries from long texts by analyzing word frequency 
and scoring sentences based on their importance.

The summarization process follows these steps:

1. Split the input text into individual sentences.
2. Normalize the text by converting it to lowercase and removing punctuation.
3. Remove common stop words to reduce noise.
4. Build a word frequency dictionary from the remaining words.
5. Score each sentence by summing the frequencies of the words it contains.
6. Select the top-ranked sentences based on score.
7. Reorder selected sentences to preserve original context.

Technologies used:
1. Python 3
2. Built in Python libraries only

1. Clone the repository.
2. Open the Python file.
3. Run the script using:
   python summarizer.py
4. Input any long text.
5. The generated summary will be printed in the terminal.
