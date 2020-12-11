import pip._vendor.requests
import json
from Parser import jprint
#This Data comes from Worldometers
natURL = "https://disease.sh/v3/covid-19/countries/USA?yesterday=true&twoDaysAgo=true&strict=true"
def NationalMenu():
    response = pip._vendor.requests.get(natURL)
    y = json.loads(response)

    jprint(response.json())

NationalMenu()


#"flag": "https://disease.sh/assets/img/flags/us.png", Keep this
#int active
#int activePerOneMillion
#int cases
#int casesPerOneMillion
#int countryInfo 
#int critical
#int criticalPerOneMillion
#int deaths
#int deathsPerOneMillion 
#int oneCasePerPeople 
#int oneDeathPerPeople
#int oneTestPerPeople 
#int population  
#int recovered 
#int recoveredPerOneMillion  
#int tests 
#int testsPerOneMillion 
#int todayCases 
#int todayDeaths 
#int todayRecovered 
#int updated 