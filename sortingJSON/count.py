import json

Center = open("./../secrets/3442QJ0PNZ.json")
CenterData = json.load(Center)
Office = open("./../secrets/0Y47ZDONX0.json")
OfficeData = json.load(Office)


lenCenter = len(CenterData)
lenOffice = len(OfficeData)


print ("Center Compromised: " + str(lenCenter))
print ("Office Compromised: " + str(lenOffice))