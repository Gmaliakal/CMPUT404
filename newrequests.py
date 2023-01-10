import requests
r = requests.get("https://raw.githubusercontent.com/Gmaliakal/CMPUT404/master/newrequests.py")
con = r.text
print(con)