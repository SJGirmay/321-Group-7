import pip._vendor.requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def stateataPrint(obj):
    resp = json.dumps(obj)
    text = json.loads(resp)
    print("State:" +text["state"])
    print("Population:" +text["population"])
    print("Active:" +text["active"])
    print("Cases:" +text["cases"])
    print("Cases Today:" +text["todayCases"])
    print("Cases Per One Million:" +text["casesPerOneMillion"])
    print("Deaths:" +text["deaths"]) 
    print("Deaths Today:" +text["todayDeaths"])
    print("Deaths Per One Million:" +text["deathsPerOneMillion"])
    print("Recovered:" +text["recovered"])
    print("Recovered Today:" +text["todayRecovered"])
    print("Recovered Per One Million:" +text["recoveredPerOneMillion"])


def nationalDataPrint(obj):
    resp = json.dumps(obj)
    text = json.loads(resp)
    print("Population:" + str(text["population"]))
    print("Active:" +str(text["active"]))
    print("ActivePerOneMillion:" +str(text["activePerOneMillion"]))
    
    print("Cases:" +str(text["cases"]))
    print("Cases Today:" +str(text["todayCases"]))
    print("Cases Per One Million:" +str(text["casesPerOneMillion"]))
    print("One Case Per People:" +str(text["oneCasePerPeople"]))
    
    print("Deaths:" +str(text["deaths"])) 
    print("Deaths Today:" +str(text["todayDeaths"]))
    print("Deaths Per One Million:" +str(text["deathsPerOneMillion"]))
    print("One Death Per People:" +str(text["oneDeathPerPeople"]))

    print("Recovered:" +str(text["recovered"]))
    print("Recovered Today:" +str(text["todayRecovered"]))
    print("Recovered Per One Million:" +str(text["recoveredPerOneMillion"]))

    print("Tests:" +str(text["tests"]))
    print("Tests Per One Million:" +str(text["testsPerOneMillion"]))
    print("One Test Per People:" +str(text["oneTestPerPeople"]))

    #print("Critical:" + str(text["critical"])
    #print(text["criticalPerOneMillion"])
    #"Critical Per One Million:" + 



    
    

    


    