# musician-erdos-number

This project gives the degree of separation between two musicians based on their collaborations. It consists of two python scripts, musician erdos.py and musiciansearch.py. It takes two artists as inputs and attempts to find a connection between them through a sequence of shared songs.
Note that the song database used for this project contains many "unofficial" songs taken from soundcloud and similar sites, so as long as the two musician are credited in any work, it will count as a connection.

### Files
musician_erdos.py - This script reads a the data CSV file, parses through the data, separates artist names, maps songs to artists, and creates a dictionary linking artists with their respective collaborations. This dictionary is saved as a JSON file.
musician_search.py - This script loads the JSON file created by musician_erdos.py and creates a network graph using the NetworkX library. It takes two artist names as inputs and uses the graph to find and display the shortest path of collaborations between the two artists.

### Data
ther are two main CSV files are used in this project, but they were too big to be added to the repo. Data taken from https://musicbrainz.org/doc/MusicBrainz_Database:

artist_credit - Contains information about artists and their songs.
recording - Contains detailed information about song recordings.

This project requires the following packages:
pandas
csv
re
sys
json
networkx

### Usage
First, run musician_erdos.py to generate the artist_link_dict.json file:
Then, run musician_search.py and enter the names of two artists when prompted


Follow the prompts to enter the names of two artists. The script will display the shortest path of collaborations between the two artists, if such a path exists.

![musicianerdos](https://github.com/ThomasAdriaanse/musician-erdos-number/assets/62912008/c51485a8-718a-4ae7-952d-b9146c4bd689)

Limitations
This project assumes that all artist names and song names are correctly spelled and that each artist or song has a unique name. As with all data-driven projects, the results are only as good as the data. Please make sure to use clean, well-curated data for best results.
