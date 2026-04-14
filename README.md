# playlist-vibe-builder
## Project chosen : Playlist Vibe Builder

This project will require me to create playlists based on songs energy levels and duration. I will use a sorting algorithm to sort the playlists based on these criteria. 

## Algorithm chosen : Merge Sort

I chose Merge Sort because it has a predictable time complexity of O(n log n) which means that unlike quick sort, there is no worst case scenario where the algorithm will run particulaly slowly. I also chose Merge Sort for this problem because I find it the easiest to visualise with it's swaps, and I think that will translate to a UI that runs smoothly and is easy for users to understand.

## Demo (video/gif/screenshot of at least one run)

[demo_screenshot](image-url)

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



## Hugging Face Link

https://huggingface.co/spaces/ClaraTokarski/playlist-vibe-builder

## Testing (what you tried + edge cases)

## Author & Acknowledgment (sources + AI use, if any)
