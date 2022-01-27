# bs4 used for web scrapping, pip install bs4
from bs4 import BeautifulSoup as BS
# do http requests to the web
import requests
import csv

page = requests.get("https://doctor.webmd.com/find-a-doctor/specialty/obstetrics-gynecology/tennessee/nashville")
soup = BS(page.content, features="lxml")
content = soup.find('ul', class_='resultslist-content')
doctorslist = content.find_all('span', class_='addr-text')
# print(doctorslist)

#save into csv file
with open('doctors.csv', mode='w', newline='') as outputFile:
    doctorsCSV = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    doctorsCSV.writerow(['street', 'city', 'state', 'zip'])

    #need to loop thru doctorslist and save it to the csv
    for address in doctorslist:
      street = address.text.split(",")[0]
      city = address.text.split(", ")[1]
      state = address.text.split(", ")[2]
      doctorsCSV.writerow([street, city, state])

