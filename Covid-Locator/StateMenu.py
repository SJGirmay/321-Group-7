import pip._vendor.requests
import json
from Parser import *
#This Data comes from Worldometers
baseUrl = "https://disease.sh/v3/covid-19/states/"

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
"Nevada","New%20Hampshire","New%20Jersey","New%20Mexico","New%20York","North%20Carolina","North%20Dakota","Ohio",
"Oklahoma","Oregon","Pennsylvania","Rhode%20Island","South%20Carolina","South%20Dakota","Tennessee","Texas",
"Utah","Vermont","Virginia","Washington","West%20Virginia","Wisconsin","Wyoming","District%20of%20Columbia","District%20of%20Columbia"]

def parser(resp):
     while 1:   
        resp1 = resp.lower()
        resp2 = resp.upper()
        if(resp1 in StatesLower):
            return(States[StatesLower.index(resp1)])
        elif(resp2 in StateAbv):
            return(States[StateAbv.index(resp2)])
        elif(resp1 == 'q' or resp1 == 'quit'):
            return 0
        else:
            resp = input('Invalid Input. Please Enter valid State or State Abreviation or q/quit ')

def parserLower(resp):
     while 1:   
        resp1 = resp.lower()
        resp2 = resp.upper()
        if(resp1 in StatesLower):
            return(StatesLower.index(resp1))
        elif(resp2 in StateAbv):
            return(StatesLower[StateAbv.index(resp2)])
        elif(resp1 == 'q' or resp1 == 'quit'):
            return 0
        else:
            resp = input('Invalid Input. Please Enter valid State or State Abreviation or q/quit ')

def StateMenu():
    resp = input('Please enter a valid state or state Abreviation. To quit, enter q or quit. ')
    inputState = parser(resp)
    if inputState != 0: 
        result = (baseUrl + inputState)
        response = pip._vendor.requests.get(result)
        jprint(response.json())
    if inputState == 0:
        return 0
