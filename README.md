# CitiesServed
Pinned served cities on a map from a list of cities.

## What do you need to install?
1. sudo apt install python3-pip
2. pip install pandas
3. pip install folium
4. pip install geopy
5. pip install tk

## How to use it?
**You only need main.py and served_cities.md (or your own cities's list) to run the programm**

Open the code at code editor and choose between the real list (you can find the list of almost 300 cities at 'served_cities.md') and the test list (the list of 8 cities is already at the code).

This software need to have delay because the GeoPy's API blocks access if you run all 300 cities at once.

When the map will be created, this is will be their appearence:

![Served Cities](https://raw.githubusercontent.com/cesar-rolli/CitiesServed/main/served_cities.png)
