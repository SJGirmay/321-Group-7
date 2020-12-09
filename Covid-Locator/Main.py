from NationalMenu import NationalMenu
from StateMenu    import StateMenu
from CountyMenu  import *
def MainMenu():
  
  print("Main Menu")
  print("1: List National Averages")
  print("2: List State Averages")
  print("3: List County Averages")
  print("4: Quit")

  resp = input('Please Select an Option ')
  if(resp == "1"):
    NationalMenu()
  elif(resp == "2"):
    StateMenu()
  elif(resp == "3"):
    CountyMenu()
  elif(resp == "4"):
    quit()
  else:
    print("Not a valid option. Please select a Valid option (1,2,3,4).")

MainMenu()

