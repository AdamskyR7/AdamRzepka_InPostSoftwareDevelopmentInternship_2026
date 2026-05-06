# Interactive Paczkomat location map built with Python, Pandas and Folium

## Author

- **Name:** Adam Rzepka
- **Email:** adamrzepka.kontakt@gmail.com

## Overview

This project is a simple Python mapper. It takes the data from API and puts each point on the map, there are two modes: first is a normal map with markers for each point and the second is a heatmap showing areas with no/low coverage.

## Demo & Description

The project is split into two scripts. First is the dataHandler which is responsible for loading the data and the second is dataMapper which genereates the map.
DataHandler's function getData can work in two ways geting the data from local json file (if the file is available) or straight from the API, after getting the data from API the scripts saves it to the local json file to cut the data download time for the next time it's needed. The data is then returned as Pandas DataFrame for easier modification.
DataMapper's function generateMap is the script responsible for generating the .html file with the interactive map. It uses Folium with it's built in plugins FastMarkerCluster, to cluster the points on the map when zoomed out and HeatMap, to create a heat map. The function has two arguments a Pandas DataFrame and an optional string filename. The map is generated in an html file with the name provided in the function (or the default if not provided).


[Link to the site](https://adamskyr7.github.io/AdamRzepka_InPostSoftwareDevelopmentInternship_2026/PaczkomatMap.html)
<img width="1264" height="920" alt="image" src="https://github.com/user-attachments/assets/db7b4208-a558-4288-936d-1d7e99236a1a" />

<img width="1571" height="1292" alt="image" src="https://github.com/user-attachments/assets/bfccb041-9e9d-4b9f-b431-f9dcabdeae8a" />

<img width="1652" height="1234" alt="image" src="https://github.com/user-attachments/assets/8fcca359-6e9d-4208-8efa-80d6c0c7ac75" />


## Technologies

Python - great for quick projects
Pandas - better data containers
Folium - built in map visualization
JavaScript - can handle more operations than python at once

## How to run

### Prerequisites

Python 3.13
Web browser
internet access

Python Bibliotheques
Pandas
Folium
Requests

### Build & run

```bash
git clone https://github.com/AdamskyR7/AdamRzepka_InPostSoftwareDevelopmentInternship_2026.git
cd AdamRzepka_InPostSoftwareDevelopmentInternship_2026/
python -m pip install pandas folium requests
python app.py
start PaczkomatMap.html
```

## What I would do with more time

implement finding the closest point to the provided location by road/pedestrian path - a standard map feature that would add more functionality to the existing project

## AI usage

Google Gemini pro - better web browser to look up how certain things can be done and debugging help to show possible fixes

## Anything else?

