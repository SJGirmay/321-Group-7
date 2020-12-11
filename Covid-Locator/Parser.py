import pip._vendor.requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def nationalDataPrint(obj):
    resp = json.dumps(obj)
    text = json.loads(resp)
    print(text["active"])
    print(text["activePerOneMillion"])
    print(text["cases"])
    print(text["casesPerOneMillion"])
    print(text["critical"])
    print(text["criticalPerOneMillion"])
    print(text["deaths"])
    print(text["deathsPerOneMillion"])
    print(text["oneCasePerPeople"])
    print(text["oneDeathPerPeople"])
    print(text["oneTestPerPeople"])
    print(text["population"])
    print(text["recovered"])
    print(text["recoveredPerOneMillion"])
    print(text["tests"])
    print(text["testsPerOneMillion"])
    print(text["todayCases"])
    print(text["todayDeaths"])
    print(text["todayRecovered"])
    print(text["recoveredPerOneMillion"])
    print(text["todayCases"])
    print(text["todayRecovered"])
    print(text["todayDeaths"])

def stateDataPrint(obj):
    resp = json.dumps(obj)
    text = json.loads(resp)
    print(text["active"])
    print(text["cases"])
    print(text["casesPerOneMillion"])
    print(text["deaths"])
    print(text["deathsPerOneMillion"])
    print(text["population"])
    print(text["recovered"])
    print(text["tests"])
    print(text["testsPerOneMillion"])
    print(text["todayCases"])
    print(text["todayDeaths"])

#def countyDataPrint(obj):
    ##resp = json.dumps(obj)
    #text = json.loads(resp)
    #print(text["province"])
    #print(text["county"])
    #print(text["confirmed"])
    #print(text["deaths"])
    #print(text["updatedAt"])

    


    