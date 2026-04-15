# playlist-vibe-builder
## Project chosen : Playlist Vibe Builder

This project will require me to create playlists based on songs energy levels and duration. I will use a sorting algorithm to sort the playlists based on these criteria. 

## Algorithm chosen : Merge Sort

I chose Merge Sort because it has a predictable time complexity of O(n log n) which means that unlike quick sort, there is no worst case scenario where the algorithm will run particulaly slowly. I also chose Merge Sort for this problem because I find it the easiest to visualise with it's swaps, and I think that will translate to a UI that runs smoothly and is easy for users to understand.

## Demo (video/gif/screenshot of at least one run)

[demo_screenshot](demo_screenshot.png)

## Problem Breakdown & Computational Thinking (include a flowchart + the 4 pillars as brief bullets)


START

↓

User inputs songs with title, artist, energy, and duration

↓

User chooses sorting category

↓

User chooses increasing or decreasing

↓

If input is valid?

→ 
YES: Split playlist until it’s in lists of 1

↓

Merge (either increasing or decreasing)

↓
    
Show visualization

↓

Display final playlist

↓

END

→ 
NO: Return to start

- **Decomposition** : This problem can be broken down into a few parts. First the code must find out which criteria it i sorting by, and then divide the list over and over again until t has lists of length one which it can merge. 
- **Pattern Recognition** : The pattern in merge sot is that the list will be epeatedly divided and then recombined one ordered pair at a time.
- **Abstraction** : The important details for the user to see are the processes of sorting. the division and reordering of the items in the list will help the user to understand the sorting process. they do not need to see how each individual pair is sorted or how the code differentiates between the different criteria such as energy or duration.
- **Algorithm Design** : 

## Steps to Run (local) + requirements.txt
- Download the repository
- Install gradio using `pip install -r requirements.txt`
- Run `app.py`

## Hugging Face Link

https://huggingface.co/spaces/ClaraTokarski/playlist-vibe-builder

## Testing (what you tried + edge cases)

For the testing of my project, I tried a few things. When I first created the most basic version of my code, it asked the user to input all the information about each song by typing it all at once into a text box with a specific format of "song, artist, energy, duration". After ceating this code I decided to change the entry strategy because it was defficult to screen for incorrect inputs. This is because certain parts of the the input (energy and duration) must be integers. To fix this, I changed the code so that the user inputs each piece of information one at a time, and then I was abloe to make each section screen to make sure that the proper type of variable had been provided. 
Secondly, while testing my code, I had to account for several edge cases. I made sure that the code accounts for if there is only one song provided, if there are identical songs or songs of the same duration/energy, and if there is no input. 

## Author & Acknowledgment (sources + AI use, if any)

Author :  Clara Tokarski

Resources : Stack Overflow to understand merge sort

AI : No AI was used.
