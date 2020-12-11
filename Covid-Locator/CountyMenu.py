import json
import requests
#This Data comes from John Hopkins
baseURL = "https://disease.sh/v3/covid-19/jhucsse/counties/"

StateAbv= ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA",
"KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NE","NH","NJ","NM","NY","NC",
"ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC","DC"]

StatesLower = ["alabama","alaska","arizona","arkansas","california","colorado","connecticut",
"delaware","florida","georgia","hawaii","idaho","illinois","indiana","iowa","kansas","kentucky","louisiana",
"maine","maryland","massachusetts","michigan","minnesota","mississippi","missouri","montana","nebraska",
"nevada","new hampshire","new jersey","new mexico","new york","north carolina","north dakota","ohio",
"oklahoma","oregon","pennsylvania","rhode island","south carolina","south dakota","tennessee","texas",
"utah","vermont","virginia","washington","west virginia","wisconsin","wyoming","district of columbia","washington dc"]

States = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut",
"Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana",
"Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska",
"Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio",
"Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas",
"Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming","District of Columbia","District of Columbia"]

#Returns confrimed, deaths, recovered, and cases for a given state and county
#Returns null if state/county are invalid
def CountyMenu():
    inputState = parserLower(input('Please enter a valid state or state Abreviation. To quit, enter q or quit. '))
    inputCounty = input('Please enter a valid County. To quit, enter q or quit. ')
    url = baseURL + inputCounty
    resp = requests.get(url)
    try: 
        for county in resp.json():
            if county["province"] == inputState:
                print("Updated on " + county["updatedAt"])
                print("State is " + county["province"])
                print("County is " + county["county"])
                print(county["stats"])
                return county["stats"]
    except:
        return print("No Counties Found")
    return None

def parserLower(resp):
    if(resp in States):
        return(resp)
    elif(resp in StatesLower):
        return(States[StatesLower.index(resp)])
    elif(resp in StateAbv):
        return(States[StateAbv.index(resp)])
    elif(resp == 'q' or resp == 'quit'):
        return None
    else:
        resp = input('Invalid Input. Please Enter valid State or State Abreviation or q/quit ')
        return(parserLower(resp))
