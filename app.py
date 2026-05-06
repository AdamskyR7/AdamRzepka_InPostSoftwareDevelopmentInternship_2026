import pandas as pd
from dataHandler import getData
from dataMapper import generateMap

####    settings    ####

# if fetchFromAPI is set to True the app redownloads the data from API (it will take a while), when set to False the app works with the latest download of the data (if it exists)
fetchFromAPI = False

####    settings    ####

data = getData(fetchFromAPI)

generateMap(data)