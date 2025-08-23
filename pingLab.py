from pathlib import Path
import subprocess
import requests
import pprint
import shutil

#Test connections with ping and requests

result = subprocess.run(
    ["ping", "google.com"],
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    text=True,
    check=True
)
response = requests.get("https://www.google.com")

html = response.text

#Exception handling for error/ status codes 

try:
    print(result, "\n", response)
   

except subprocess.CalledProcessError as e:
    print(result.stderr, {e})
    print(response.status_code, {e})

#Cleanly print Huge data and save it to a .txt
pprint.pprint(data)


path = C:\Users\Dell\OneDrive\Documents\py
folder / urloutput.txt

with open("html", "w", encoding="UTF-8") as urloutput:
    datalog.write(f"Status: {response.status_code}")
   







