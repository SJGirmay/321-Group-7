import pip._vendor.requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def nationalDataPrint(obj):
    resp = json.dumps(obj)
    text = json.loads(resp)
    print(text["population"])
    print(text["active"])#Total
    print(text["activePerOneMillion"])
    
    print(text["cases"])#Total
    print(text["todayCases"])
    print(text["casesPerOneMillion"])
    print(text["oneCasePerPeople"])
    
    print(text["deaths"]) #Total
    print(text["todayDeaths"])
    print(text["deathsPerOneMillion"])
    print(text["oneDeathPerPeople"])

    print(text["recovered"])#Total
    print(text["todayRecovered"])
    print(text["recoveredPerOneMillion"])

    print(text["tests"])#Total
    print(text["testsPerOneMillion"])
    print(text["oneTestPerPeople"])

    print(text["critical"])#Total
    print(text["criticalPerOneMillion"])

def stateDataPrint(obj):
    resp = json.dumps(obj)
    text = json.loads(resp)
    
    print(text["state"])
    print(text["population"])#Total
    print(text["active"])#Total
    
    print(text["cases"])#Total
    print(text["todayCases"])
    print(text["casesPerOneMillion"])

    print(text["deaths"])#Total
    print(text["todayDeaths"])
    print(text["deathsPerOneMillion"])
    
    print(text["recovered"])#Total
    print(text["tests"])#Total
    print(text["testsPerOneMillion"])
    
    

#def countyDataPrint(obj):
    ##resp = json.dumps(obj)
    #text = json.loads(resp)
    
    #print(text["province"])
    #print(text["county"])
    
    #print(text["confirmed"])
    #print(text["deaths"])
    
    #print(text["updatedAt"])

    


    