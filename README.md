# csv-json-converter
Convert initial scraped shelter information from csv to json

* Python version 3.6.5
* [googlemaps api](https://github.com/googlemaps/google-maps-services-python)
* [CSV Shelter Data](https://docs.google.com/spreadsheets/d/1Vsk33ZdNWaJfQ87bDCPtWqUKmWg0PBaeY3mp8xPf4zA/edit#gid=0)

1. Download the code
2. Set up a Google API Account
3. Rename ```settings.py.example``` to ```settings.py```
4. Set value of the Google API Key in ```settings.py```
5. Delete the files in the data folder. They were used to test and demonstrate the code.
6. Download the Shelter CSV from the linked Google Drive
7. Copy the Downloaded Shelter CSV into the Data folder
   - Alternatively, change the file path in ```settings.py``` to whereever you would like to place the data
8. Run the program
9. Go into the data folder and retrieve the newly created JSON file
