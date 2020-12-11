import pip._vendor.requests
import json
#This Data comes from John Hopkins
baseURL = "https://disease.sh/v3/covid-19/jhucsse/counties/"

#Returns confrimed, deaths, recovered, and cases for a given state and county
#Returns null if state/county are invalid
def CountyMenu():
    inputCounty = input('Please enter a valid County. To quit, enter q or quit. ')
    url = baseURL + inputCounty
    resp = pip._vendor.requests.get(url)
    print(resp.json())
    inputState = input('Please enter a valid State. To quit, enter q or quit. ')
    for county in resp.json():
        if county["province"] == inputState:
            print(county["province"])
            return county["stats"]
    #return NULL

CountyMenu()