import requests
import bs4
from datetime import datetime

datestr = str(datetime.today().strftime("%d/%m/%y"))
now = datetime.now()
time = str(now.strftime("%H:%M"))

req = requests.get("https://myanimelist.net/profile/ScopicHD")
soup = bs4.BeautifulSoup(req.text, "lxml")
soupText = soup.getText()

dstart = soupText.find("Days: ")
numstart = dstart + 6
daynum = ""

NumList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]

while soupText[numstart] in NumList:
    daynum = daynum + soupText[numstart]
    numstart = numstart + 1

data = soup.select("span")


Days = float(daynum)
TotalEntries = int(data[40].getText())
Episodes = int(data[44].getText().replace(",", ""))
Completed = int(data[35].getText())
Watching = int(data[34].getText())
Planned = int(data[38].getText())
Rewatched = int(data[42].getText())
MeanScore = float(data[28].getText())


print(datestr + " @ " + time)
print("Days:", Days)
print("Total Entries:", TotalEntries)
print("Episodes:", Episodes)
print("Completed:", Completed)
print("Watching:", Watching)
print("Plan To Watch:", Planned)
print("Rewatched:", Rewatched)
print("Mean Score:", MeanScore)
