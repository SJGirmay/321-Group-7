import pip._vendor.requests
import json
from Parser import *
#This Data comes from Worldometers
natURL = "https://disease.sh/v3/covid-19/countries/USA"
def NationalMenu():
    response = pip._vendor.requests.get(natURL)
    jprint(response.json())

NationalMenu()