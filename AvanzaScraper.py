import urllib.request
from bs4 import BeautifulSoup
import csv
import datetime


companies = [
    "https://www.avanza.se/aktier/om-aktien.html/3986/amazon-com-inc",
    "https://www.avanza.se/aktier/om-aktien.html/5369/kinnevik-b",
    "https://www.avanza.se/aktier/om-aktien.html/425935/victoria-park-pref"
    
    
    
    
    ] 
for data in companies:
    Page = urllib.request.urlopen(data)
    Soup = BeautifulSoup(Page, "html.parser")
    lastPrice = Soup.find("span", attrs={"class":"lastPrice SText bold"})
    companyName = Soup.find("h1", attrs={"class":"large marginBottom10px"})
    finishedCompanyName = companyName.text.strip()
    finishedLastPrice = lastPrice.text.strip()
    print("{} Data has been collected".format(finishedCompanyName))

    with open("index.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([finishedCompanyName, finishedLastPrice, datetime.date.today()])


