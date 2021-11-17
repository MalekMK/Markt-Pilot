# Markt Pilot Challenge

This script gets the data to scraping from /csv/data.csv and returns wollplatz.csv file in csv folder which contains (Brand/Name/Result) from every item to search in: https://www.wollplatz.de/

This is a temporary solution and could be maintained !

## Instructions

### clone the repo and then go the main folder.

#### Create a virtual env via 

`virtualenv marktPlatz`

#### Then activate the env :

##### for MacOS/Linux: 
`source marktPlatz/bin/activate`
##### for Windows: 
`marktPlatz\Scripts\activatee`


#### Install requirements 

`pip3 install -r requirements.txt`

#### To run the script: 

`python3 main.py`

#### To run the tests: 

`python3 -m unittest`

#### Once finished Desactivate the env via: 

`deactivate`
