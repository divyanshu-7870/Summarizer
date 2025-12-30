# Rule-Based Extractive Text Summarizer

This project implements a rule-based extractive text summarizer in Python. 
It generates concise summaries from long texts by analyzing word frequency 
and scoring sentences based on their importance.

## The summarization process follows these steps:

1. Split the input text into individual sentences.
2. Normalize the text by converting it to lowercase and removing punctuation.
3. Remove common stop words to reduce noise.
4. Build a word frequency dictionary from the remaining words.
5. Score each sentence by summing the frequencies of the words it contains.
6. Select the top-ranked sentences based on score.
7. Reorder selected sentences to preserve original context.

## Technologies used

1. Python 3
2. Built-in Python libraries only

## How to Run the Project

1. Clone the repository.
2. Open the Python file.
3. Paste the text in myText variable quotes. 
4. Run the script using:
   python summarizer.py
5. The generated summary will be printed in the terminal.

## EXAMPLE

### Input 
The clock on Elias’s mantle didn’t just tick; it inhaled. Every sixty seconds, the brass gears let out a soft, rhythmic sigh that seemed to pull the warmth right out of the room. Elias, a man who had spent forty years repairing timepieces, knew better than anyone that time wasn’t a river—it was a predator. He sat at his workbench, squinting through a jeweler’s loupe at a pocket watch that had stopped in 1912, its hands frozen like a silent plea.

As he nudged a microscopic escapement wheel, the shop grew unnervingly still. The street noise of the city outside vanished, replaced by a low, melodic humming that vibrated in his teeth. He realized with a jolt of adrenaline that his own heart was beating in perfect synchronization with the rhythmic sigh of the mantle clock. He reached out to touch the frozen pocket watch, and as his fingertip brushed the cold gold casing, the hands began to whirl backward at an impossible speed.

Suddenly, the scent of saltwater and old perfume filled the air. The dim light of his shop flickered, casting shadows that looked less like furniture and more like people in long-forgotten fashions. Elias pulled his hand back, gasping, as the ticking returned to its normal, steady pace. The pocket watch was ticking now, too, but the face no longer showed the time—it showed a reflection of a sunlit deck and a sea that hadn't been crossed in a century. He hadn't just fixed the watch; he had reopened a door he wasn't sure he was ready to walk through.

### Output 
Suddenly, the scent of saltwater and old perfume filled the air. The dim light of his shop flickered, casting shadows that looked less like furniture and more like people in long-forgotten fashions. Elias pulled his hand back, gasping, as the ticking returned to its normal, steady pace. The pocket watch was ticking now, too, but the face no longer showed the time—it showed a reflection of a sunlit deck and a sea that hadn't been crossed in a century. He hadn't just fixed the watch; he had reopened a door he wasn't sure he was ready to walk through.

# Limitations:
1. This is an extractive summarizer, not an abstractive one.
2. It relies on word frequency and does not understand semantics.
3. Sentence splitting is basic and may not handle complex punctuation perfectly.
