
## Stolen.... re-purposed.... form Stack Overflow
## https://stackoverflow.com/questions/19697846/how-to-convert-csv-file-to-multiline-json


# Google Maps Services
## https://github.com/googlemaps/google-maps-services-python

## Field Names: Double commented fields need to be looked up from the Google API ()
#  t.string "county"
#  t.string "shelter"      # the shelter name
#  t.string "address"
#  t.string "phone"
#  t.boolean "ada"
#  t.boolean "allow_pets"
#  t.boolean "open"
#  t.boolean "accepting" 
#  t.boolean "active"      # set this to true
##  t.string "city" 
##  t.float "longitude"
##  t.float "latitude"
##  t.string "address_name"       # not sure what this means
##  t.string "state"
##  t.string "zip"
##  t.string "google_place_id"     # this comes from google geocoding api

import csv
import json
import googlemaps
import settings


## Set gmaps
gmaps = googlemaps.Client(key=settings.Google_API_Key)

## Set files
local_file_path = settings.file_path
csv_file_name="North Carolina Shelters - Sheet1.csv"
json_file_name="initial-shelter-data.json"

csv_file = local_file_path + csv_file_name
json_file = local_file_path + json_file_name

csv_file_read = open(csv_file, 'r')
json_file_write = open(json_file, 'w')

fieldnames = ("county","shelter", "address", "phone", "ada", 
"allow_pets", "open", "accepting", "active", "city", "longitude",
"latitude", "address_name", "state", "zip","google_place_id")

# Read all off the data from the CSV as a dict
csv_reader = csv.DictReader(csv_file_read)
for row in csv_reader:
    # For the address dict, lookup its value in the Google API
    row_address = row.get('address')
    geocode_result = gmaps.geocode(row_address)
    print(len(geocode_result))


# Append the returned API value to the dict
# write the dict to JSON

# Address Fields
## 