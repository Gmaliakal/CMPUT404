import requests

r = requests.get("http://www.google.com/")
con = r.content
print(con)

#2.28.1
#.text option at the end of request library