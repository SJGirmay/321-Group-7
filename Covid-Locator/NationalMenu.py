import pip._vendor.requests
import json
from Parser import jprint,nationalDataPrint
#This Data comes from Worldometers
natURL = "https://disease.sh/v3/covid-19/countries/USA?yesterday=true&twoDaysAgo=true&strict=true"
#"https://disease.sh/assets/img/flags/us.png", Keep this for HTML
def NationalMenu():
    response = pip._vendor.requests.get(natURL)
    nationalDataPrint(response.json())

